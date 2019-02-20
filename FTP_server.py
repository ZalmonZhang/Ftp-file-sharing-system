#!/usr/bin/env python3
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
"""
FTP Server
"""
import os
import sys
import multiprocessing
import time
import pymysql
from socket import SOL_SOCKET, SO_REUSEADDR, socket


class TftpServer:
    """'创建ftpServer的类"""

    def __init__(self, order_conn):
        """
        在中间还会创建的属性有
        套接字类
        self.order_conn  处理一切命令有关的套接字通信
        self.file_conn_socket 创建的文件传输套接字
        self.file_conn_port 被动模式下客户端传递用来链接文件传输套接字的端口号
        self.file_conn  文件传输套接字accept()后所分配的套接字
        其他类
        self.pvalue 权限值
        self.username 用户名
        self.file_path 文件所在的目录位置
        """
        self.order_conn = order_conn
        self.file_path = PATH

    def login(self, data):  # 处理登录请求的方法
        sql1 = "select passwd from user where name='%s';" % (data[1])
        # 判断用户名是否存在
        self.cursor.execute(sql1)
        result = self.cursor.fetchone()
        if result:
            # sql2 = "select passwd from user where passwd='%s';" % (data[2])
            # 判断密码是否正确
            # self.cursor.execute(sql2)
            if result[0] == data[2]:
                return 2  # 登录成功
            else:
                return 1  # 密码错误
        else:
            return 0  # 用户名不存在

    def register(self, data):  # 处理注册请求的方法

        sql = "select name from user where name='%s';" % data[1]
        self.cursor.execute(sql)
        if self.cursor.fetchone():
            return 0
        else:
            sql = "insert into user(name,passwd,permission) values('%s','%s','普通会员');" % (
                data[1], data[2])

            self.cursor.execute(sql)
            self.conn_mysql.commit()
            return 1

    def get_pvalue(self, username):  # 获得权限的方法
        sql = "select permission from user where name='%s';" % username
        self.cursor.execute(sql)
        r = self.cursor.fetchone()
        return r[0]

    def show_directory(self):  # 处理展现目录的方法
        l = os.listdir(os.getcwd())
        folder = []
        files = []
        dicts = {}
        for i in l:
            if os.path.isdir(i) and i[0] != '.':
                # if os.isdir(i):  # linux 环境
                folder.append(i)
        for i in l:
            if os.path.isfile(i) and i[0] != '.':
                # if os.file(i):  # linux 环境
                files.append(i)
        dicts['file'] = files
        dicts['directory'] = folder
        return dicts

    def change_directory(self, change_path, initial_path):  # 处理切换目录的方法
        if change_path == '../':
            if os.getcwd() == initial_path:
                return 0
            else:
                os.chdir('../')
                self.file_path = os.getcwd()
                return 1
        elif change_path == 'home':
            os.chdir(initial_path)
            self.file_path = os.getcwd()
            return 1
        else:
            folder_path = './%s' % change_path
            try:
                os.chdir(folder_path)
                self.file_path = os.getcwd()
            except:
                return 2
            else:
                return 1

    def create_directory(self, directory_name):  # 处理创建目录的方法
        self.pvalue = self.get_pvalue(self.username)
        if self.pvalue == '管理员':
            if directory_name in os.listdir():
                return 1
            else:
                os.mkdir(directory_name)
                return 2
        else:
            return 0

    def create_file_conn(self):  # 创建文件传输套接字的方法,采取的被动模式
        self.file_conn_socket = socket()
        while True:
            try:
                self.file_conn_port = int(self.order_conn.recv(
                    1024).decode())  # 接收客户端传递的文件传输端口号
                self.file_conn_socket.bind(('0.0.0.0', self.file_conn_port))
                self.file_conn_socket.listen(10)
                self.order_conn.send(b'OK')  # 发送告知客户端文件传输套接字创建完成,等待客户端的链接
                return
            except:
                self.order_conn.send(b'NO')

    def file_download(self, filename):
        self.create_file_conn()  # 创建新的传 输文件套接字
        self.file_conn, self.file_conn_addr = self.file_conn_socket.accept()  # 等待客户端的链接
        data = self.order_conn.recv(1024).decode().split()  # 'N' 'C 已存文件大小'
        local_file_size = os.path.getsize(filename)
        if data[0] == 'N':  # 服务端不存在该文件,直接传输文件
            if len(self.file_path) != 1:
                filename = '/' + filename
            try:
                f = open(self.file_path + filename, 'rb')
                data_of_file_size = '1 %s' % local_file_size
                # 找到文件,告知客户端开启文件传输套接字,准备接收
                self.order_conn.send(data_of_file_size.encode())
                for line in f:
                    self.file_conn.send(line)  # 发送文件内容,以二进制方式
                f.close()
                # time.sleep(0.1)
                # self.file_conn.send(b'##')  # 传输完文件以##结束
            except IOError:
                self.order_conn.send(b'0')  # 未找到文件
            except Exception as e:
                print(e)
                f.close()
            self.file_conn.close()
            self.file_conn_socket.close()
        elif data[0] == 'E':  # 服务端存在该文件,进行断点续传
            if local_file_size == int(data[1]):
                self.order_conn.send(b'2')
                return
            if len(self.file_path) != 1:
                filename = '/' + filename
            try:
                f = open(self.file_path + filename, 'rb')
                data_of_file_size = '1 %d' % local_file_size
                # 找到文件,告知客户端开启文件传输套接字,准备接收
                self.order_conn.send(data_of_file_size.encode())
                f.seek(int(data[1]), 0)
                for line in f:
                    self.file_conn.send(line)  # 发送文件内容,以二进制方式
                f.close()
                # time.sleep(0.1)
                # self.file_conn.send(b'##')  # 传输完文件以##结束
            except IOError:
                self.order_conn.send(b'0')  # 未找到文件
            except Exception as e:
                print(e)
                f.close()
                self.file_conn.close()
                self.file_conn_socket.close()
            self.file_conn.close()
            self.file_conn_socket.close()

    def file_upload(self, filename):
        self.pvalue = self.get_pvalue(self.username)
        if self.pvalue in ['高级会员', '管理员']:
            self.order_conn.send(b'1')
            time.sleep(0.1)
            self.create_file_conn()  # 创建新的传输文件套接字
            self.file_conn, self.file_conn_addr = self.file_conn_socket.accept()  # 等待客户端的链接
            if filename in os.listdir('./'):  # 如果目录下存在文件则进行断点续传
                exists_size = os.path.getsize(filename)  # 获取文件的大小
                self.order_conn.send(('E %s' % exists_size).encode())  # 传递给客户端
                file_checkExists = self.order_conn.recv(1024).decode()
                if file_checkExists == '2':
                    return
                if len(self.file_path) != 1:
                    filename = '/' + filename
                try:
                    f = open(self.file_path + filename, 'ab')
                    while True:
                        data = self.file_conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                except Exception as e:
                    print(e)
                else:
                    f.close()
                    # self.order_conn.send(b'OK')
                self.file_conn.close()
                self.file_conn_socket.close()
            else:
                self.order_conn.send(b'N')
                if len(self.file_path) != 1:
                    filename = '/' + filename
                try:
                    f = open(self.file_path + filename, 'wb')
                    while True:
                        data = self.file_conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                except Exception as e:
                    print(e)
                else:
                    f.close()
                    # self.order_conn.send(b'OK')
                self.file_conn.close()
                self.file_conn_socket.close()
        else:
            self.order_conn.send(b'0')  # 权限不足,无法操作上传

    def file_delete(self, filename):
        self.pvalue = self.get_pvalue(self.username)
        if self.pvalue == '管理员':
            if len(self.file_path) != 1:
                filename = '/' + filename
            try:
                os.remove(self.file_path + filename)
            except:
                return 1  # 文件不存在
            else:
                return 2  # 文件删除成功
        else:
            return 0  # 权限不足,无法操作删除

    def get_all_permission(self):
        # 从数据库获取所有用户信息，以字典的方式存储
        self.cursor.execute('select name,permission from user')
        data = self.cursor.fetchall()
        self.cursor.close()
        self.conn_mysql.close()
        self.connect_to_mysql()
        user_permission = {}
        for i in data:
            user_permission[i[0]] = i[1]
        return user_permission

    def change_permission(self, data):
        self.pvalue = self.get_pvalue(self.username)
        if self.pvalue == '管理员':
            userList_dict = self.get_all_permission()
            if len(data) == 1:
                userList_dict = str(userList_dict)
                self.order_conn.send(userList_dict.encode())
                return 3
            else:
                if data[1] not in userList_dict.keys():  # 用户名不存在
                    return 0
                else:  # 修改权限，修改成功返回2
                    sql = 'update user set permission="%s" where name="%s"' % (data[
                                                                               2], data[1])
                    self.cursor.execute(sql)
                    self.conn_mysql.commit()
                    self.cursor.close()
                    self.conn_mysql.close()
                    self.connect_to_mysql()
                    return 2
        else:
            return 1

    def connect_to_mysql(self):  # 开始链接数据库
        self.conn_mysql = pymysql.connect(host="localhost", user="root", password="123456",
                                          database="FTP", charset="utf8")
        self.cursor = self.conn_mysql.cursor()


def client_handle(order_conn):
    """客户端的命令进行处理"""
    print('connect from', order_conn.getpeername())
    tftp = TftpServer(order_conn)
    # tftp.order_conn.send(b'220 Service ready for new user.\r\n')
    tftp.connect_to_mysql()
    while True:
        # login event
        data = tftp.order_conn.recv(1024).decode()
        data = data.split()
        if not data:  # 客户端退出，关闭套接字和数据库连接
            tftp.file_path = PATH
            try:
                tftp.order_conn.close()
            except:
                pass
            try:
                tftp.file_conn.close()
            except:
                pass
            try:
                tftp.file_conn_socket.close()
            except:
                pass
            try:
                tftp.cursor.close()
            except:
                pass
            try:
                tftp.conn_mysql.close()
            except:
                pass
            sys.exit()
        if data[0] == 'L':  # login
            result = tftp.login(data)
            if result == 1:  # 用户名或者密码错误,请重试
                tftp.order_conn.send(
                    b'1')
            elif result == 0:  # 用户名不存在请进行注册
                tftp.order_conn.send(
                    b'0')
            else:
                tftp.username = data[1]  # 对象添加username属性
                tftp.pvalue = tftp.get_pvalue(data[1])
                # 登录成功
                tftp.order_conn.send(
                    b'2')
        if data[0] == 'R':  # register
            result = tftp.register(data)
            if result == 0:  # 用户名已经被注册
                tftp.order_conn.send(b'0')
            elif result == 1:  # 注册成功
                tftp.order_conn.send(b'1')
        if data[0] == 'SWD':  # show directory
            send_data = str(tftp.show_directory())
            tftp.order_conn.send(send_data.encode())
        if data[0] == 'CGD':  # change directory
            result = tftp.change_directory(data[1], PATH)
            if result == 0:  # 已经达到根目录
                tftp.order_conn.send(b'0')
            elif result == 2:
                tftp.order_conn.send(b'2')
            else:
                send_data = str(tftp.show_directory())
                tftp.order_conn.send(send_data.encode())
        if data[0] == 'CTD':  # create directory
            result = tftp.create_directory(
                data[1])  # 传入目录名 和 权限值
            if result == 0:  # 没有权限进行创建文件夹
                tftp.order_conn.send(b'0')
            elif result == 1:  # 文件夹名已经被占用
                tftp.order_conn.send(
                    b'1')
            elif result == 2:  # 创建文件夹成功
                send_data = str(tftp.show_directory())
                tftp.order_conn.send(send_data.encode())
        if data[0] == 'FDL':  # file download
            tftp.file_download(data[1])
        if data[0] == 'FUL':  # file upload
            tftp.file_upload(data[1])
        if data[0] == 'FDT':  # file delete
            result = tftp.file_delete(data[1])
            if result == 0:  # 没有权限进行删除
                tftp.order_conn.send(
                    b'0')
            elif result == 1:  # 文件不存在，请刷新文件列表
                tftp.order_conn.send(
                    b'1')
            elif result == 2:  # 文件成功被删除
                tftp.order_conn.send(b'2')
        if data[0] == 'CHP':  # change permission
            result = tftp.change_permission(data)
            if result == 0:  # 用户名不存在
                tftp.order_conn.send(
                    b'0')
            elif result == 1:  # 没有权限进行权限管理
                tftp.order_conn.send(
                    b'1')
            elif result == 2:  # 权限更改成功
                tftp.order_conn.send(b'2')
            else:
                pass


def create_sql():
    """
    生成默认用户数据库
    库名:FTP
    表名:user
    字段: id, name, passwd, permission
    """
    conn_sql = pymysql.connect(
        host="localhost", user="root", password="123456", charset="utf8")
    cursor1 = conn_sql.cursor()
    try:
        cursor1.execute('use FTP')
    except pymysql.err.InternalError:  # 如果没有FTP库则创建
        # except:
        cursor1.execute('create database FTP character set utf8')
        cursor1.execute('use FTP')
    try:
        cursor1.execute('desc user;')
    except pymysql.err.ProgrammingError:  # 如果没有user表则创建
        # except:
        cursor1.execute('create table user(\
                id int primary key auto_increment,\
                name varchar(32) not null,\
                passwd varchar(10) not null default "000000",\
                permission varchar(16) not null default "普通用户")\
                character set utf8;')
        cursor1.execute('insert into user values(null,"admin","admin","管理员");')
    conn_sql.commit()
    cursor1.close()
    conn_sql.close()


def main():
    """主函数"""
    HOST = '0.0.0.0'
    PORT = 2121
    ADDR = (HOST, PORT)
    if len(sys.argv) < 2:
        print('please give a path for start')
        return
    global PATH
    PATH = sys.argv[1]  # 获取初始目录路径
    os.chdir(PATH)
    order_socket = socket()
    order_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    order_socket.bind(ADDR)
    order_socket.listen(10)
    print('Listen to the port 2121')
    create_sql()
    # 开始处理客户端链接
    while True:
        try:
            client_connect, address = order_socket.accept()
        except KeyboardInterrupt:
            client_connect.close()
            order_socket.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        # 多线程处理客户端链接
        process_client = multiprocessing.Process(
            target=client_handle, args=(client_connect,))
        process_client.daemon = True
        process_client.start()


if __name__ == '__main__':
    main()

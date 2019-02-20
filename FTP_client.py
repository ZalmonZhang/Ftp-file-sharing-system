#!/usr/bin/env python3
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import os
import sys
import time
import random
from socket import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette, QBrush
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QProgressDialog, QMessageBox)
# IP连接界面


class start(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # 本地文件创建
        try:
            os.mkdir("history")
        except Exception as e:
            pass

        try:
            self.addrs = open('history/address.txt', 'x')
            self.addrs.write('["127.0.0.1"]')
            self.addrs.close()
        except Exception as e:
            pass

        self.btn = PyQt5.QtWidgets.QPushButton('连接')
        self.btn.setToolTip('请输入你的IP地址进行连接')
        # self.btn.resize(btn.sizeHint())   #调整按钮大小并在屏幕显示sizeHint提供默认的按钮大小
        self.btn.setGeometry(QRect(560, 300, 100, 35))
        self.path()

    def path(self):

        # 背景图片
        self.window_pale = QPalette()
        self.window_pale.setBrush(
        self.backgroundRole(), QBrush(QPixmap('./img/连接界面2.JPG')))
        self.setPalette(self.window_pale)

        # 设置字体大小
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("楷体")

        self.resize(800, 600)  # 窗口的大小
        # self.move(300,300)           #窗口在window上的位置
        self.center()
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('FTP登录界面')  # 窗口的标题名字
        self.setWindowIcon(QIcon('./img/enf.JPG'))  # 窗口的图标

        PyQt5.QtWidgets.QToolTip.setFont(QFont('SanSerif', 10))  # 设置提示框的字体和大小
        self.setToolTip('are you ok?')  # 创建了提示框并且添加内容

        self.btn = PyQt5.QtWidgets.QPushButton('连接', self)  # 创建界面的连接按钮
        # self.btn.setToolTip('请输入你的IP地址进行连接')
        # self.btn.resize(btn.sizeHint())   #调整按钮大小并在屏幕显示sizeHint提供默认的按钮大小
        self.btn.setGeometry(QRect(560, 300, 100, 35))
        self.btn.font()
        self.btn.setFont(font)
        # QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()
        # 创建了一个它的实例。QCoreApplication是在QApplication里创建的。
        # 点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        # 在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        # btn.clicked.connect(QCoreApplication.instance().quit)

        title = PyQt5.QtWidgets.QLabel('请输入服务器IP:', self)
        title.setFont(QFont('楷体', 15))
        title.setGeometry(QRect(120, 300, 180, 35))
        # title.setText(_translate("MainWindow", "输入IP地址:"))

        # ?干啥用
        maps = PyQt5.QtWidgets.QLabel('', self)
        maps.setGeometry(QRect(40, 60, 491, 181))

        # 地址输入框
        self.paswod = PyQt5.QtWidgets.QComboBox(self)
        self.paswod.setEditable(True)
        self.paswod.setGeometry(QRect(300, 300, 200, 35))
        self.paswod.font()
        self.paswod.setFont(font)
        self.address = open('history/address.txt')
        addlist1 = eval(self.address.read())
        for ad in addlist1:
            self.paswod.addItem(ad)
        self.address.close()

    def center(self):
        qr = self.frameGeometry()
        cp = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def slot1(self, data):
        PyQt5.QtWidgets.QMessageBox.information(self, "提示",
                                                self.tr(data))

    # 登录界面


class cool(PyQt5.QtWidgets.QWidget):
    # 创建信号
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.EVA()

    def EVA(self):
        # 背景图片

        # 设置字体大小
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)

        self.resize(800, 600)
        self.centen()
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('FTP登录界面')  # 窗口的标题名字
        self.setWindowIcon(QIcon('./img/enf.JPG'))  # 窗口的图标

        self.end = PyQt5.QtWidgets.QPushButton('登录', self)  # 创建界面的连接按钮
        self.end.setGeometry(QRect(200, 430, 100, 35))
        self.end.font()
        self.end.setFont(font)

        self.ando = PyQt5.QtWidgets.QPushButton('注册', self)
        self.ando.setGeometry(QRect(500, 430, 100, 35))
        self.ando.font()
        self.ando.setFont(font)

        name = PyQt5.QtWidgets.QLabel('用户名:', self)
        name.setGeometry(QRect(200, 230, 100, 35))

        self.named = PyQt5.QtWidgets.QLineEdit(self)
        self.named.setGeometry(QRect(200, 270, 400, 35))
        self.nons = ""
        self.named.setText(self.nons)
        self.named.font()
        self.named.setFont(font)

        password = PyQt5.QtWidgets.QLabel('密码:', self)
        password.setGeometry(QRect(200, 310, 100, 35))

        self.passwords = PyQt5.QtWidgets.QLineEdit(self)
        self.passwords.installEventFilter(self)
        self.passwords.setGeometry(QRect(200, 350, 400, 35))
        self.passwords.setText(self.nons)
        self.passwords.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.passwords.font()
        self.passwords.setFont(font)

        # 创建一个图片对象
        self.png1 = QPixmap('./img/1.JPG')
        self.png2 = QPixmap('./img/2.JPG')
        self.ato1 = QPixmap('./img/3.JPG')
        self.ato2 = QPixmap('./img/4.JPG')
        # 创建一个标签
        self.mapt1 = PyQt5.QtWidgets.QLabel('', self)
        self.mapt1.setGeometry(QRect(500, 60, 561, 201))
        # 把图片放进标签
        self.mapt1.setPixmap(self.png1)
        # 创建第二个标签
        self.mapt2 = PyQt5.QtWidgets.QLabel('', self)
        self.mapt2.setGeometry(QRect(135, 60, 561, 201))
        # 把图片放进标签
        self.mapt2.setPixmap(self.png2)
        vb = PyQt5.QtWidgets.QVBoxLayout()
        vb.addWidget(self.passwords)
        # 收到信号执行函数
        self.clicked.connect(self.showData)

    def eventFilter(self, widget, event):
        if widget == self.passwords:
            if event.type() == QEvent.FocusOut:
                # 当未选中密码框的时候显示的图片
                self.mapt1.setPixmap(self.png1)
                self.mapt2.setPixmap(self.png2)
            elif event.type() == QEvent.FocusIn:
                self.clicked.emit()  # 当焦点再次落到edit输入框时，发送clicked信号出去
            else:
                pass
        return False

    def showData(self):
        # 当密码框被选中同时执行该函数将标签显示变成该图片
        self.mapt1.setPixmap(self.ato1)
        self.mapt2.setPixmap(self.ato2)

    def centen(self):
        qr = self.frameGeometry()
        cp = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def slot0(self):
        PyQt5.QtWidgets.QMessageBox.information(
            self, "提示", self.tr("用户不存在请注册"))

    def slot1(self):
        PyQt5.QtWidgets.QMessageBox.information(
            self, "提示", self.tr("用户密码错误请重新输入"))

    def slot2(self):
        PyQt5.QtWidgets.QMessageBox.information(
            self, "提示", self.tr("用户密码不能为空"))

    # 注册界面


class tend(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.motd()

    def motd(self):

        self.resize(600, 500)  # 窗口的大小
        # self.move(300,300)           #窗口在window上的位置
        self.cented()
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('FTP注册界面')  # 窗口的标题名字
        self.setWindowIcon(QIcon('./img/enf.JPG'))

        # 背景图片
        self.window_pale = QPalette()
        self.window_pale.setBrush(
            self.backgroundRole(), QBrush(QPixmap('./img/注册界面.JPG')))
        self.setPalette(self.window_pale)

        # 设置字体
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("楷体")

        self.sest = PyQt5.QtWidgets.QPushButton('注册', self)
        self.sest.setGeometry(QRect(250, 380, 100, 35))
        self.sest.font()
        self.sest.setFont(font)

        name = PyQt5.QtWidgets.QLabel('用户名:', self)
        name.setGeometry(QRect(150, 200, 100, 35))

        self.named = PyQt5.QtWidgets.QLineEdit(self)
        self.named.setGeometry(QRect(250, 200, 200, 35))
        self.named.setText("")
        self.named.font()
        self.named.setFont(font)

        password = PyQt5.QtWidgets.QLabel('密码:', self)
        password.setGeometry(QRect(150, 260, 100, 35))

        self.passwords = PyQt5.QtWidgets.QLineEdit(self)
        self.passwords.setGeometry(QRect(250, 260, 200, 35))
        self.passwords.setText("")
        self.passwords.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.passwords.font()
        self.passwords.setFont(font)

        pwod = PyQt5.QtWidgets.QLabel('确认密码:', self)
        pwod.setGeometry(QRect(150, 320, 100, 35))

        self.paswod = PyQt5.QtWidgets.QLineEdit(self)
        self.paswod.setGeometry(QRect(250, 320, 200, 35))
        self.paswod.setText("")
        self.paswod.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.paswod.font()
        self.paswod.setFont(font)

    def slot1(self):
        PyQt5.QtWidgets.QMessageBox.information(
            self, "提示", self.tr("用户名和密码不能有空格"))

    def slot2(self):
        PyQt5.QtWidgets.QMessageBox.information(self, "提示", self.tr("两次密码不一致"))

    def slot3(self):
        PyQt5.QtWidgets.QMessageBox.information(self, "提示", self.tr("用户名已存在"))

    def slot4(self):
        PyQt5.QtWidgets.QMessageBox.information(self, "提示", self.tr("注册成功"))

    def slot5(self):
        PyQt5.QtWidgets.QMessageBox.information(
            self, "提示", self.tr("用户名和密码不能为空"))

    def cented(self):
        qr = self.frameGeometry()
        cp = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def reset(self):
        self.named.clear()
        self.passwords.clear()
        self.paswod.clear()
        self.show()


class FTP_Client():

    def __init__(self):
        sockfd = socket()
        self.sockfd = sockfd

    def conn_server(self, address):
        try:
            self.sockfd.connect((address, 2121))
        except:
            return 0
        else:
            self.ip_addr = address
            return 1

    def login(self, usename, passwd):
        msg = "L {} {}".format(usename, passwd)
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        return data

    def register(self, name, password, pwd):
        if (' ' in name) or (' ' in password):
            return 1  # "用户名或密码不能有空格"
        elif password != pwd:
            return 2  # "两次密码不一致"
        elif not name or not password or not pwd:
            return 3  # "用户名,或者密码为空"

        # 将注册信息发送给服务器
        msg = 'R {} {}'.format(name, password)
        self.sockfd.send(msg.encode())

        data = self.sockfd.recv(1024).decode()
        return data

    # 返回上一层
    def return_up(self):
        msg = 'CGD ../'
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        return data

    # 切换目录
    def change_menu(self, dir_name):
        msg = 'CGD %s' % dir_name
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        return data

    # 返回主目录
    def return_home(self):
        msg = 'CGD home'
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        return data

    # 创建文件夹
    def create_menu(self, directorys):
        msg = 'CTD %s' % directorys
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        return data

    # 刷新目录列表
    def new_menu(self):
        msg = 'SWD'
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        # print(data, 2)
        return data

    def create_file_socket(self):
        while True:
            random_port = str(random.randrange(20000, 40000, 1))
            self.sockfd.send(random_port.encode())
            connect_ready = self.sockfd.recv(1024).decode()
            if connect_ready == 'NO':
                continue
            else:
                break
        self.file_sockfd = socket()
        self.file_sockfd.connect((self.ip_addr, int(random_port)))

    def download_file(self, file_name, dir_path):
        msg = 'FDL %s' % file_name
        self.sockfd.send(msg.encode())
        time.sleep(0.1)
        self.create_file_socket()
        return_path = os.getcwd()
        os.chdir(dir_path)
        dir_path = dir_path + '/' + file_name
        if file_name in os.listdir('./'):  # 本地存在文件，进行断点续传
            exists_size = os.path.getsize(file_name)
            self.sockfd.send(('E %s' % exists_size).encode())
            file_checkExists = self.sockfd.recv(1024).decode().split()
            if file_checkExists[0] == '1':
                try:
                    progress = self.show_Dialog(0, int(file_checkExists[1]))
                    f = open(dir_path, 'ab')
                    trans_size = exists_size
                    while True:
                        data = self.file_sockfd.recv(1024)
                        transing_size = len(data)
                        if not data:
                            break
                        f.write(data)
                        trans_size += transing_size
                        progress.setValue(trans_size)
                        if progress.wasCanceled():
                            msgBox = PyQt5.QtWidgets.QMessageBox(
                                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '下载中断')
                            msgBox.setIconPixmap(QPixmap())
                            msgBox.exec_()
                            self.file_sockfd.close()
                            self.sockfd.recv(1024)
                            f.close()
                            os.chdir(return_path)
                            return
                    f.close()
                except Exception as e:
                    print(e)
                os.chdir(return_path)
                return 1
            elif file_checkExists[0] == '2':
                os.chdir(return_path)
                return 2
            else:
                os.chdir(return_path)
                return 0
            self.file_sockfd.close()
        else:  # 本地不存在文件，直接全部发送
            time.sleep(0.1)
            self.sockfd.send(b'N')
            file_checkExists = self.sockfd.recv(1024).decode().split()
            if file_checkExists[0] == '1':
                try:
                    progress = self.show_Dialog(0, int(file_checkExists[1]))
                    f = open(dir_path, 'wb')
                    trans_size = 0
                    while True:
                        data = self.file_sockfd.recv(1024)
                        transing_size = len(data)
                        if not data:
                            break
                        f.write(data)
                        trans_size += transing_size
                        progress.setValue(trans_size)
                        if progress.wasCanceled():
                            msgBox = PyQt5.QtWidgets.QMessageBox(
                                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '下载中断')
                            msgBox.setIconPixmap(QPixmap())
                            msgBox.exec_()
                            # self.file_sockfd.send(b'')
                            self.file_sockfd.close()
                            self.sockfd.recv(1024)
                            f.close()
                            os.chdir(return_path)
                            return
                    f.close()
                except Exception as e:
                    print(e)
                os.chdir(return_path)
                return 1
            else:
                os.chdir(return_path)
                return 0
            self.file_sockfd.close()

    def upload_file(self, file_path):
        file_name = file_path.split('/')[-1]
        msg = 'FUL %s' % file_name
        self.sockfd.send(msg.encode())
        response = self.sockfd.recv(1024).decode()
        if response == '0':  # 权限不足，无法上传
            return 0
        else:
            self.create_file_socket()
            file_exists = self.sockfd.recv(1024).decode().split()
            local_file_size = os.path.getsize(file_path)
            if file_exists[0] == 'E':
                server_file_size = int(file_exists[1])
                if local_file_size == server_file_size:
                    self.sockfd.send(b'2')
                    return 2
                else:
                    self.sockfd.send(b'1')
                    try:
                        progress = self.show_Dialog(0, local_file_size)
                        f = open(file_path, 'rb')
                        trans_size = server_file_size
                        f.seek(server_file_size, 0)
                        for line in f:
                            transing_size = len(line)
                            self.file_sockfd.send(line)
                            trans_size += transing_size
                            progress.setValue(trans_size)
                            if progress.wasCanceled():
                                msgBox = PyQt5.QtWidgets.QMessageBox(
                                    PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '上传中断')
                                msgBox.setIconPixmap(QPixmap())
                                msgBox.exec_()
                                self.file_sockfd.close()
                                f.close()
                                return
                    except Exception as e:
                        print(e)
                    else:
                        f.close()
                    self.file_sockfd.close()
                    return 1  # 上传成功
            else:
                try:
                    progress = self.show_Dialog(0, local_file_size)
                    f = open(file_path, 'rb')
                    trans_size = 0
                    for line in f:
                        transing_size = len(line)
                        self.file_sockfd.send(line)
                        trans_size += transing_size
                        progress.setValue(trans_size)
                        if progress.wasCanceled():
                            msgBox = PyQt5.QtWidgets.QMessageBox(
                                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '上传中断')
                            msgBox.setIconPixmap(QPixmap())
                            msgBox.exec_()
                            self.file_sockfd.close()
                            f.close()
                            return
                except Exception as e:
                    print(e)
                else:
                    f.close()
                self.file_sockfd.close()
                return 1  # 上传成功

    # 显示进度条
    def show_Dialog(self, start, end):
        progress = QProgressDialog()
        # 弹窗标题
        progress.setWindowTitle("请稍等")
        # 弹窗显示文字
        progress.setLabelText("正在传输...")
        # 取消按钮
        progress.setCancelButtonText("取消")
        # 如任务小于设置值则弹窗不显示
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(start, end)
        return progress

    # 权限更改
    def change_power(self, uname, text):
        msg = 'CHP {} {}'.format(uname, text)
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        # data = str(data)
        return data

    # 获取权限名单
    def getperminfo(self):
        # 套接字获取名单
        msg = "CHP"
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(20480).decode()
        data = eval(data)
        return data
        # 添加会员名单
        # 向表格中添加

    def delete_file(self, file_name):
        msg = 'FDT %s' % file_name
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        return data


class connect_f1Tof2():

    def __init__(self):
        self.client = FTP_Client()
    # IP连接

    def check_addr(self):
        ip_addr = ex.paswod.currentText()
        number = self.client.conn_server(ip_addr)
        if number == 1:
            self.addrs = open("history/address.txt")
            add = eval(self.addrs.read())
            self.addrs.close()
            if ip_addr not in add:
                add.append(ip_addr)
                q = open('history/address.txt', 'w')
                q.write(str(add))
                q.close()

            ex.close()
            ac.show()
            return
        ex.slot1('输入IP错误')
    # 登录窗口

    def check_log(self):
        name = ac.named.text()
        password = ac.passwords.text()
        if not name or not password:
            ac.slot2()
        elif len(name) >= 32 or len(password) >= 10:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '用户名或者密码过长,请不要超过10位')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
        else:
            result = self.client.login(name, password)
            if result == '0':
                ac.slot0()
            if result == '1':
                ac.slot1()
            if result == '2':
                self.run_main_menu()
                mains.initTextStatus(name)

    # 注册窗口
    def check_register(self):
        name = bt.named.text()
        passwords = bt.passwords.text()
        paswod = bt.paswod.text()
        if len(name) >= 32 or len(passwords) >= 10:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '用户名或者密码过长,请不要超过10位')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
        else:
            register = self.client.register(name, passwords, paswod)
            if register == 1:
                bt.slot1()
            if register == 2:
                bt.slot2()
            if register == 3:
                bt.slot5()
            if register == '0':
                bt.slot3()
            if register == '1':
                bt.slot4()
                bt.close()
                return

    # 初始显示文件目录
    def init_show_menu(self):
        dicts = self.client.new_menu()
        mains.labeladress.setText('当前服务器路径为: /')
        return dicts

    # 显示、刷新文件夹
    def show_menu(self, dicts):
        mains.table_files.clear()
        mains.table_file.clear()
        mains.table_files.setHorizontalHeaderLabels(['文件名'])
        dicts_list = dicts
        for file_name in dicts_list['directory']:
            mains.table_file.addItem(file_name)
        # 为文件表格添加目录
        # self.table_file.setItem(0,0,QTableWidgetItem("123456789456123"))
        files = dicts_list['file']
        x = len(files)
        mains.table_files.setRowCount(x)
        for i in range(x):
            mains.table_files.setItem(
                i, 0, PyQt5.QtWidgets.QTableWidgetItem(files[i]))

    # 切换目录
    def change_dir(self, path_way):
        dicts = self.client.change_menu(path_way)
        if dicts == 2:
            mains.change_dir_info()
            data = '切换目录 : 目录切换失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        else:
            self.show_menu(dicts)
            data = '切换目录 : 已切换到' + path_way + ' , 操作时间 : ' + str(time.ctime())
            server_path = mains.labeladress.text() + path_way + '/'
            mains.labeladress.setText(server_path)
            mains.TextStatus.append(data)

    # 返回上一层文件夹
    def return_up(self):
        dicts = self.client.return_up()
        if dicts == 0:
            mains.back_up_info()
            data = '切换目录 : 目录切换失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        else:
            self.show_menu(dicts)
            data = '切换目录 : 已切换到上一级目录 , 操作时间 : ' + str(time.ctime())
            server_path = mains.labeladress.text().split('/')
            path_len = len(server_path)
            new_server_path = ''
            for i in range(0, path_len - 2):
                new_server_path = new_server_path + server_path[i] + '/'
            mains.labeladress.setText(new_server_path)
            mains.TextStatus.append(data)

    # 返回主目录
    def return_home(self):
        dicts = self.client.return_home()
        self.show_menu(dicts)
        data = '切换目录 : 已返回主目录 , 操作时间 : ' + str(time.ctime())
        mains.labeladress.setText('当前服务器路径为: /')
        mains.TextStatus.append(data)

    # 刷新目录列表
    def refresh_dir_method(self):
        dicts = self.client.new_menu()
        self.show_menu(dicts)

    # 运行主目录窗口
    def run_main_menu(self):
        mains.show()
        ac.close()
        dicts = self.init_show_menu()
        data = '显示目录 : 获取服务器目录列表 , 获取时间 : ' + str(time.ctime())
        mains.TextStatus.append(data)
        self.show_menu(dicts)  # 初始展示目录
        data = '显示目录 : 获取成功 , 获取时间 : ' + str(time.ctime())
        mains.TextStatus.append(data)

    # 文件上传
    def upload_file(self, file_path, file_name):
        result = self.client.upload_file(file_path)
        if result == 0:  # 权限不足,无法操作上传
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '您没有权限进行文件上传')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '文件上传 : ' + file_name + \
                '文件上传失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        elif result == 2:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '文件已经完整上传过了,请不要重复上传')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '文件上传 : ' + file_name + \
                '文件上传失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        elif result == 1:  # 上传成功
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '上传成功')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            self.refresh_dir_method()
            data = '文件上传 : ' + file_name + \
                '文件上传成功 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        else:
            pass

    # 文件下载
    def download_file(self, file_name, dir_path):
        result = self.client.download_file(file_name, dir_path)
        if result == 0:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '文件未找到，请刷新文件目录后重试')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '文件下载 : ' + file_name + \
                '文件下载失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        elif result == 2:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '文件已经完整下载过了,请不要重复下载')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '文件下载 : ' + file_name + \
                '文件下载失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        elif result == 1:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '文件下载成功')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '文件下载 : ' + file_name + \
                '文件下载成功 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        else:
            pass

        # 添加会员名单
    def getinfo(self):

        data = self.client.getperminfo()

        # 7.16 权限确认
        if data == 1:
            # permUi.close()
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '您没有权限进行权限操作')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '修改权限 : 没有相应权限进行权限管理 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        else:
            permUi.show()
            getinfo = []
            for i in data:
                getinfo.append([i, data[i]])

            x = len(data)

            permUi.Userinfo.setRowCount(x)
            for i in range(x):
                permUi.Userinfo.setItem(
                    i, 0, PyQt5.QtWidgets.QTableWidgetItem(str((getinfo[i])[0])))
                permUi.Userinfo.setItem(
                    i, 1, PyQt5.QtWidgets.QTableWidgetItem(str((getinfo[i])[1])))
            # 权限更改

    def changepower(self, uname, text):
        data = self.client.change_power(uname, text)

        if data == "0":
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '用户名单中没有这个人,请重新确认')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '修改权限 : 修改权限失败 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)
        if data == "2":
            self.getinfo()
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '修改成功')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
            data = '修改权限 : 修改权限成功 , 操作时间 : ' + str(time.ctime())
            mains.TextStatus.append(data)

    def text_none(self):
        ac.named.setText(ac.nons)
        ac.passwords.setText(ac.nons)

    def premission_text_none(self):
        change.changeText.setText(ac.nons)


class Mywindow(PyQt5.QtWidgets.QWidget):

    def __init__(self, c):
        super(Mywindow, self).__init__()
        self.c = c  # 传递f1tof2 创建的对象，提供方法
        # 创建主界面 设置宽高
        self.setObjectName("Mywindow")
        self.resize(1000, 600)
        # 文件夹下拉选框
        # 界面标题
        self.setWindowTitle("FTP文件传输系统")

        # 两个文件位置操作按钮
        # 返回上一层按钮
        self.back = PyQt5.QtWidgets.QPushButton(self)
        self.back.setGeometry(QRect(80, 330, 100, 35))
        self.back.setObjectName("back")
        self.back.setText("返回上一层")
        self.back.clicked.connect(self.back_up)

        # 返回主目录
        self.backhome = PyQt5.QtWidgets.QPushButton(self)
        self.backhome.setGeometry(QRect(250, 330, 100, 35))
        self.backhome.setObjectName("backhome")
        self.backhome.setText("返回根目录")
        self.backhome.clicked.connect(self.back_home)

        # 文件夹操作
        # 创建文件夹

        self.mkdir_ = PyQt5.QtWidgets.QPushButton(self)
        self.mkdir_.setText("创建文件夹")
        self.mkdir_.setObjectName("mkdir_")
        self.mkdir_.setGeometry(QRect(80, 385, 100, 35))
        # self.mkdir_.clicked.connect(self.mkdir_method)

        # 刷新文件夹

        self.rfdir_ = PyQt5.QtWidgets.QPushButton(self)
        self.rfdir_.setText("刷新目录")
        self.rfdir_.setGeometry(QRect(250, 385, 100, 35))
        self.rfdir_.setObjectName("rfdir_")
        self.rfdir_.clicked.connect(self.refresh_dir_method)

        # 表格显示文件

        # 标签
        self.label_file = PyQt5.QtWidgets.QLabel("文件夹", self)
        self.label_file.font()
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        self.label_file.setFont(font)
        self.label_file.setGeometry(170, 5, 100, 35)

        # 标签 显示文件夹路径
        self.labeladress = PyQt5.QtWidgets.QLabel(self)
        self.labeladress.setGeometry(50, 40, 320, 140)
        self.labeladress.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.labeladress.setFont(font)

        # 文件夹 下拉选框
        self.table_file = PyQt5.QtWidgets.QComboBox(self)
        self.table_file.setGeometry(QRect(50, 180, 320, 50))
        self.table_file.setObjectName("table_file")
        self.table_file.setEditable(False)
        self.table_file.font()
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.table_file.setFont(font)
        self.table_file.activated[str].connect(self.change_dir)

        # 文件表
        # 标签
        self.label_files = PyQt5.QtWidgets.QLabel("文件", self)
        self.label_files.font()
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        self.label_files.setFont(font)
        self.label_files.setGeometry(650, 0, 100, 35)

        self.table_files = PyQt5.QtWidgets.QTableWidget(self)

        self.table_files.setColumnCount(1)
        # 设置初始行数
        # self.table_files.setRowCount(10)
        self.table_files.setGeometry(QRect(420, 40, 520, 250))
        # 读取表头
        # self.table_files.setHorizontalHeaderLabels(horizontalHeader_files)
        self.table_files.setObjectName("table_files")
        # 改变列宽
        self.table_files.setColumnWidth(0, 500)

        # 设置不可变
        # self.table_files.setEditTriggers(QAbstractItemView.NoEditTriggers
        self.table_files.setEditTriggers(
            PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)
        # 设置只选中一行
        self.table_files.setSelectionBehavior(
            PyQt5.QtWidgets.QAbstractItemView.SelectRows)
        # 允许右键产生子菜单
        self.table_files.setContextMenuPolicy(Qt.CustomContextMenu)
        # 右键菜单
        self.table_files.customContextMenuRequested.connect(self.generateMenu)

        # 两个个权限按钮
        #  上传   权限管理

        # 上传
        self.Upload = PyQt5.QtWidgets.QPushButton(self)
        self.fileLineEdit = PyQt5.QtWidgets.QLineEdit()

        self.Upload.setGeometry(QRect(80, 440, 100, 35))
        self.Upload.setText("上传")
        self.setObjectName("Upload")
        self.Upload.clicked.connect(self.upload_file)

        # 权限管理 弹窗
        self.permission = PyQt5.QtWidgets.QPushButton(self)
        self.permission.setGeometry(QRect(250, 440, 100, 35))
        self.permission.setObjectName("permission")
        self.permission.setText("权限管理")

        # 显示状态文本框
        self.TextStatus = PyQt5.QtWidgets.QTextBrowser(self)
        self.TextStatus.setObjectName("TextStatus")
        self.TextStatus.setGeometry(QRect(420, 320, 520, 175))

        self.TextStatus.font()
        font = QtGui.QFont()
        # font.setFamily("黑体")
        font.setPointSize(12)
        # font.setBold(True)
        font.setFamily('楷体')
        self.TextStatus.setFont(font)

        # 返回登录界面按钮
        self.back_login = PyQt5.QtWidgets.QPushButton(self)
        self.back_login.setGeometry(QRect(840, 510, 100, 35))
        self.back_login.setText("返回登录界面")
        self.back_login.setObjectName("back_login")

    def initTextStatus(self, name):
        Nowtime = time.ctime()
        Nowtime = Nowtime.split(" ")
        # 获取当前的小时数
        NowHour = int((Nowtime[3].split(":"))[0])
        if 0 <= NowHour < 10:
            data = '尊敬的' + name + '早上好!'
            self.TextStatus.setText(data)
        elif 10 <= NowHour < 14:
            data = '尊敬的' + name + '中午好!'
            self.TextStatus.setText(data)
        elif 14 <= NowHour < 18:
            data = '尊敬的' + name + '下午好!'
            self.TextStatus.setText(data)
        else:
            data = '尊敬的' + name + '晚上好!'
            self.TextStatus.setText(data)
        self.TextStatus.append("欢迎使用FTP文件传输管理系统!")

    # 文件夹上label显示当前文件夹
    def change_dir(self, path_way):
        self.c.change_dir(path_way)

    def change_dir_info(self):
        msgBox = PyQt5.QtWidgets.QMessageBox(
            PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '无法找到该目录，请刷新目录后重试')
        msgBox.setIconPixmap(QPixmap())
        msgBox.exec_()

    # 刷新文件夹函数
    def refresh_dir_method(self):
        self.c.refresh_dir_method()

    # 返回上一层函数
    def back_up(self):
        self.c.return_up()

    # 提示返回至最上层
    def back_up_info(self):
        msgBox = PyQt5.QtWidgets.QMessageBox(
            PyQt5.QtWidgets.QMessageBox.NoIcon, '提示', '已达到目录顶端')
        msgBox.setIconPixmap(QPixmap())
        msgBox.exec_()

        # 返回主目录函数
    def back_home(self):
        self.c.return_home()

    def upload_file(self):
        path = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "选择文件")
        if not path[0]:
            return
        file_path = str(path[0])
        file_name = file_path.split('/')[-1]
        self.c.upload_file(file_path, file_name)

    def generateMenu(self, pos):
        # 重设菜单显示位置
        new_posX = pos.x() + 22
        new_posY = pos.y() + 25
        pos.setX(new_posX)
        pos.setY(new_posY)

        selections = self.table_files.selectionModel()
        selectedslist = selections.selectedRows()
        selectedOne = selectedslist[0].row()
        cmenu = PyQt5.QtWidgets.QMenu(self)
        #     # 右键下载选项
        downloadAct = cmenu.addAction("下载")
        #     # 右键删除选型
        deleteAct = cmenu.addAction("删除")
        #  点击右键时，在鼠标位置显示菜单列表
        action = cmenu.exec_(self.table_files.mapToGlobal(pos))

        if action == deleteAct:
            file_name = self.table_files.item(selectedOne, 0).text()
            choose_result = self.info('您确认是否删除文件？')
            if choose_result == 1:
                result = self.c.client.delete_file(file_name)
                if result == '0':
                    PyQt5.QtWidgets.QMessageBox.information(
                        self, "提示", self.tr("您没有删除文件的权限"))
                elif result == '1':
                    PyQt5.QtWidgets.QMessageBox.information(
                        self, "提示", self.tr("文件不存在,请刷新文件列表后再进行操作"))
                elif result == '2':
                    PyQt5.QtWidgets.QMessageBox.information(
                        self, "提示", self.tr("删除文件成功"))
                    self.refresh_dir_method()
        elif action == downloadAct:
            file_name = self.table_files.item(selectedOne, 0).text()
            dir_path = PyQt5.QtWidgets.QFileDialog.getExistingDirectory(
                self, "请选择文件夹")
            if not dir_path:
                return
            self.c.download_file(file_name, dir_path)

    def info(self, message):
        reply = PyQt5.QtWidgets.QMessageBox.information(
            self, '提示', message, PyQt5.QtWidgets.QMessageBox.Ok | PyQt5.QtWidgets.QMessageBox.Close, PyQt5.QtWidgets.QMessageBox.Close)
        if reply == PyQt5.QtWidgets.QMessageBox.Ok:
            return 1
        else:
            return 0


class permissionUI(PyQt5.QtWidgets.QWidget):

    def __init__(self, c):
        super(permissionUI, self).__init__()
        self.c = c  # 传递f1tof2 创建的对象，提供方法
        # 创建主界面 设置宽高
        # 界面标题
        self.setWindowTitle("权限管理")
        self.setObjectName("权限管理")
        self.resize(800, 600)

        # 权限管理 由会员列表-会员名 和权限等级
        self.Userinfo = PyQt5.QtWidgets.QTableWidget(self)
        self.Userinfo.setGeometry(QRect(100, 20, 600, 500))
        # 表头
        info_header = ["用户名", "用户等级"]
        self.Userinfo.setColumnCount(2)
        # self.Userinfo.setRowCount(100)
        self.Userinfo.setObjectName("Userinfo")
        self.Userinfo.setHorizontalHeaderLabels(info_header)
        # 更改列宽
        self.Userinfo.setColumnWidth(0, 400)
        self.Userinfo.setColumnWidth(1, 173)

        # 将表格设置为不可改变
        self.Userinfo.setEditTriggers(
            PyQt5.QtWidgets.QAbstractItemView.NoEditTriggers)

        # 返回上一层按钮
        self.back_to_main = PyQt5.QtWidgets.QPushButton(self)
        self.back_to_main.setObjectName("back_to_main")
        self.back_to_main.setGeometry(QRect(600, 550, 100, 35))
        self.back_to_main.setText("返回主界面")

        # 权限更改按钮
        self.permission_change = PyQt5.QtWidgets.QPushButton(self)
        self.permission_change.setObjectName("permission_change")
        self.permission_change.setText("更改权限")
        self.permission_change.setGeometry(QRect(100, 550, 100, 35))


class change_permission(PyQt5.QtWidgets.QWidget):

    def __init__(self, c):
        super(change_permission, self).__init__()
        # 调用FTP_client
        self.c = c
        self.permission_value = '普通会员'

        # 创建主界面 设置宽高
        self.setObjectName("change_permission")
        self.resize(600, 400)
        # 文件夹下拉选框
        # 界面标题
        self.setWindowTitle("更改权限")

        # label标签1
        self.label_perm_name = PyQt5.QtWidgets.QLabel("用户名", self)
        self.label_perm_name.setGeometry(QRect(100, 15, 100, 35))
        self.label_perm_name.font()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("宋体")
        self.label_perm_name.setFont(font)

        # 输入框 输入要更改的用户名
        self.changeText = PyQt5.QtWidgets.QLineEdit(self)
        self.changeText.setObjectName("changeText")
        self.changeText.setGeometry(QRect(100, 50, 400, 50))
        self.changeText.font()
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setFamily("黑体")
        font.setWeight(60)
        self.changeText.setFont(font)

        # label标签2
        self.label_perm_rank = PyQt5.QtWidgets.QLabel("用户名", self)
        self.label_perm_rank.setGeometry(QRect(100, 125, 100, 35))
        self.label_perm_rank.font()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("宋体")
        self.label_perm_rank.setFont(font)

        # 权限等级下拉列表
        self.cbox_perm_rank = PyQt5.QtWidgets.QComboBox(self)
        self.cbox_perm_rank.setGeometry(QRect(100, 165, 400, 50))
        # 不可输入 只能选择
        self.cbox_perm_rank.setEditable(False)

        self.cbox_perm_rank.font()
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.cbox_perm_rank.setFont(font)
        # 获取下拉选框选取
        self.cbox_perm_rank.activated[str].connect(self.confirm_change2)

        # 确认 和 取消 按钮
        # 确定
        self.confirm = PyQt5.QtWidgets.QPushButton("确定", self)
        self.confirm.setGeometry(QRect(100, 275, 100, 35))
        self.confirm.setObjectName("confirm")

        # 取消按钮
        self.cancel = PyQt5.QtWidgets.QPushButton("取消", self)
        self.cancel.setGeometry(QRect(400, 275, 100, 35))
        self.cancel.setObjectName("cancel")

        # 设置点击槽函数
        self.confirm.clicked.connect(self.confirm_change)

        # 测试用label
        self.label_test = PyQt5.QtWidgets.QLabel("", self)
        self.label_test.setGeometry(QRect(100, 350, 200, 35))
        # 测试用label
        self.label_test2 = PyQt5.QtWidgets.QLabel("", self)
        self.label_test2.setGeometry(QRect(400, 350, 200, 35))

    # 先获取下拉选框的值
    def confirm_change2(self, text):
        self.permission_value = text

    # 槽函数2 获取下拉选框内容
    def confirm_change(self, text):
        # 发送选择的权限
        uname = self.changeText.text()

        self.c.changepower(uname, self.permission_value)
        self.cleartext()

    def clearcbox(self):
        self.cbox_perm_rank.clear()
        permItem = ["普通会员", "高级会员", "管理员"]
        for perm in permItem:
            self.cbox_perm_rank.addItem(perm)

    def cleartext(self):
        self.changeText.clear()
        self.cbox_perm_rank.clear()
        permItem = ["普通会员", "高级会员", "管理员"]
        for perm in permItem:
            self.cbox_perm_rank.addItem(perm)


class mkdir_window(PyQt5.QtWidgets.QWidget):
    # 创建文件夹名字输入窗口

    def __init__(self, c):
        super(mkdir_window, self).__init__()
        self.c = c
        # 创建主界面 设置宽高
        # 界面标题
        self.setWindowTitle("创建文件夹")
        self.setObjectName("创建文件夹")
        self.resize(400, 250)

        # 设置字体
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("楷体")

        # 输入框标题
        self.mkdirlabel = PyQt5.QtWidgets.QLabel('请输入文件夹名', self)
        self.mkdirlabel.setGeometry(QRect(50, 30, 150, 35))
        self.mkdirlabel.font()
        self.mkdirlabel.setFont(font)

        # 输入框
        self.mkdirname = PyQt5.QtWidgets.QLineEdit(self)
        self.mkdirname.setGeometry(QRect(50, 70, 300, 35))
        self.mkdirname.font()
        self.mkdirname.setFont(font)

        # 确认按钮
        self.mkdirconfirm = PyQt5.QtWidgets.QPushButton("确定", self)
        self.mkdirconfirm.setGeometry(QRect(50, 140, 100, 35))
        self.mkdirconfirm.font()
        self.mkdirconfirm.setFont(font)

        # 取消按钮
        self.mkdircancel = PyQt5.QtWidgets.QPushButton('取消', self)
        self.mkdircancel.setGeometry(QRect(250, 140, 100, 35))
        self.mkdircancel.font()
        self.mkdircancel.setFont(font)

        # 槽函数确认
        self.mkdirconfirm.clicked.connect(self.mkdir_confirm)

    def mkdir_confirm(self):
        dirname = self.mkdirname.text()
        # 本地判断输入的名字是否为空，为空弹出提示信息
        if dirname == "":
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '无法创建', '文件夹名不能为空')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
        elif ' ' in dirname or '/' in dirname:
            msgBox = PyQt5.QtWidgets.QMessageBox(
                PyQt5.QtWidgets.QMessageBox.NoIcon, '无法创建', '件夹名中包含空格或者"/"')
            msgBox.setIconPixmap(QPixmap())
            msgBox.exec_()
        else:
            dicts = self.c.client.create_menu(dirname)
            if dicts == 0:
                msgBox = PyQt5.QtWidgets.QMessageBox(
                    PyQt5.QtWidgets.QMessageBox.NoIcon, '无法创建', '您的权限值不够,无法创建文件夹')
                msgBox.setIconPixmap(QPixmap())
                msgBox.exec_()
                self.mkdirname.setText('')
            elif dicts == 1:
                msgBox = PyQt5.QtWidgets.QMessageBox(
                    PyQt5.QtWidgets.QMessageBox.NoIcon, '无法创建', '文件夹名以存在,请另用新名创建')
                msgBox.setIconPixmap(QPixmap())
                msgBox.exec_()
                self.mkdirname.setText('')
            else:
                msgBox = PyQt5.QtWidgets.QMessageBox(
                    PyQt5.QtWidgets.QMessageBox.NoIcon, '创建成功', '文件创建成功,请在文件夹中查看')
                msgBox.setIconPixmap(QPixmap())
                msgBox.exec_()
                self.c.show_menu(dicts)
                self.mkdirname.setText('')

    def comment_clear(self):
        self.mkdirname.setText('')


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    # IP界面对象
    ex = start()
    # 登录界面对象
    ac = cool()
    # 注册界面对象
    bt = tend()

    c = connect_f1Tof2()
    # 主界面对象
    mains = Mywindow(c)
    mk_dir = mkdir_window(c)
    permUi = permissionUI(c)
    change = change_permission(c)

    # 进行IP连接
    ex.show()

    # 进行登录

    ex.btn.clicked.connect(c.check_addr)
    ac.end.clicked.connect(c.check_log)
    # 进行注册
    ac.ando.clicked.connect(bt.reset)
    bt.sest.clicked.connect(c.check_register)

    # 创建文件夹
    mains.mkdir_.clicked.connect(mk_dir.comment_clear)
    mains.mkdir_.clicked.connect(mk_dir.show)

    # mk界面返回
    mk_dir.mkdircancel.clicked.connect(mk_dir.close)

    # 返回登录界面
    mains.back_login.clicked.connect(c.text_none)

    mains.back_login.clicked.connect(ac.show)

    mains.back_login.clicked.connect(mains.back_home)

    mains.back_login.clicked.connect(mains.close)

    # 点击按钮先调用函数发送套接字 获取权限名单
    mains.permission.clicked.connect(c.getinfo)

    # 点击改变权限按钮打开界面
    permUi.permission_change.clicked.connect(change.show)
    permUi.permission_change.clicked.connect(change.cleartext)

    # 关闭按钮 perm
    permUi.back_to_main.clicked.connect(permUi.close)

    # 关闭按钮 change
    change.cancel.clicked.connect(change.close)

    sys.exit(app.exec_())

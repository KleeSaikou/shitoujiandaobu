# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainw.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 433)
        MainWindow.setMinimumSize(QtCore.QSize(916, 433))
        MainWindow.setMaximumSize(QtCore.QSize(916, 433))
        MainWindow.setSizeIncrement(QtCore.QSize(916, 433))
        MainWindow.setBaseSize(QtCore.QSize(916, 433))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 341, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 261, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 341, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 521, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 581, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 270, 791, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 411, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_shitou = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shitou.setGeometry(QtCore.QRect(400, 40, 131, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.pushButton_shitou.setFont(font)
        self.pushButton_shitou.setObjectName("pushButton_shitou")
        self.pushButton_jiandao = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jiandao.setGeometry(QtCore.QRect(580, 40, 131, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.pushButton_jiandao.setFont(font)
        self.pushButton_jiandao.setObjectName("pushButton_jiandao")
        self.pushButton_bu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bu.setGeometry(QtCore.QRect(750, 40, 131, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.pushButton_bu.setFont(font)
        self.pushButton_bu.setObjectName("pushButton_bu")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 170, 281, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_shuru_queren = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shuru_queren.setGeometry(QtCore.QRect(830, 170, 81, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.pushButton_shuru_queren.setFont(font)
        self.pushButton_shuru_queren.setObjectName("pushButton_shuru_queren")
        self.label_getText = QtWidgets.QLabel(self.centralwidget)
        self.label_getText.setGeometry(QtCore.QRect(300, 340, 581, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_getText.setFont(font)
        self.label_getText.setText("")
        self.label_getText.setObjectName("label_getText")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(740, 410, 161, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "石头剪刀布"))
        self.label.setText(_translate("MainWindow", "这是一个石头剪刀布的游戏"))
        self.label_2.setText(_translate("MainWindow", "嘿，绅士们女士们大家好哇"))
        self.label_3.setText(_translate("MainWindow", "当然是我们两个人之间的游戏哦"))
        self.label_4.setText(_translate("MainWindow", "你可以选择右面三个选项中的一个，或者自己输入点什么"))
        self.label_5.setText(_translate("MainWindow", "当然，只可以输入“石头”、“剪刀”、“布”中的任意一个"))
        self.label_6.setText(_translate("MainWindow", "抱歉这个游戏只能这么玩，不过请选择一个吧 无论你怎么选择我都会随机出一个哦"))
        self.label_7.setText(_translate("MainWindow", "拜托了！这对我很重要！"))
        self.pushButton_shitou.setText(_translate("MainWindow", "石头"))
        self.pushButton_jiandao.setText(_translate("MainWindow", "剪刀"))
        self.pushButton_bu.setText(_translate("MainWindow", "布"))
        self.pushButton_shuru_queren.setText(_translate("MainWindow", "确认"))
        self.label_8.setText(_translate("MainWindow", "2020-2022 KleeTech版权所有"))

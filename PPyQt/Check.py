# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(945, 558)
        Dialog.setStyleSheet("QDialog{border-image: url(haha.jpg);}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet(" border:1px solid rgb(170,70,70);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("QPushButton{\n"
"font-family: \"等线 Light\";\n"
"font-size:30px;\n"
"color: #303030;\n"
"}\n"
"/* 正常状态或者鼠标松开按钮的状态，按钮颜色 */\n"
"QPushButton\n"
"{\n"
"    background-color:rgb(240,255,255);\n"
"    color: rgb(0, 0, 2);\n"
"    border-style: outset;\n"
"    border-color: beige;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* hover按钮悬浮，鼠标悬浮在按钮上的状态，按钮颜色 */\n"
" QPushButton:hover \n"
"{\n"
"    background-color:rgb(143, 197, 255);\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
" /* 鼠标按下按钮时的状态，按钮颜色 */\n"
"QPushButton:checked \n"
"{\n"
"    background-color:skyblue;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

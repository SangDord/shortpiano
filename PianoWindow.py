# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.key1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key1.sizePolicy().hasHeightForWidth())
        self.key1.setSizePolicy(sizePolicy)
        self.key1.setIconSize(QtCore.QSize(16, 16))
        self.key1.setObjectName("key1")
        self.pianokey = QtWidgets.QButtonGroup(MainWindow)
        self.pianokey.setObjectName("pianokey")
        self.pianokey.addButton(self.key1)
        self.horizontalLayout.addWidget(self.key1)
        self.key2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key2.sizePolicy().hasHeightForWidth())
        self.key2.setSizePolicy(sizePolicy)
        self.key2.setObjectName("key2")
        self.pianokey.addButton(self.key2)
        self.horizontalLayout.addWidget(self.key2)
        self.key3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key3.sizePolicy().hasHeightForWidth())
        self.key3.setSizePolicy(sizePolicy)
        self.key3.setObjectName("key3")
        self.pianokey.addButton(self.key3)
        self.horizontalLayout.addWidget(self.key3)
        self.key4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key4.sizePolicy().hasHeightForWidth())
        self.key4.setSizePolicy(sizePolicy)
        self.key4.setObjectName("key4")
        self.pianokey.addButton(self.key4)
        self.horizontalLayout.addWidget(self.key4)
        self.key5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key5.sizePolicy().hasHeightForWidth())
        self.key5.setSizePolicy(sizePolicy)
        self.key5.setObjectName("key5")
        self.pianokey.addButton(self.key5)
        self.horizontalLayout.addWidget(self.key5)
        self.key6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key6.sizePolicy().hasHeightForWidth())
        self.key6.setSizePolicy(sizePolicy)
        self.key6.setObjectName("key6")
        self.pianokey.addButton(self.key6)
        self.horizontalLayout.addWidget(self.key6)
        self.key7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key7.sizePolicy().hasHeightForWidth())
        self.key7.setSizePolicy(sizePolicy)
        self.key7.setObjectName("key7")
        self.pianokey.addButton(self.key7)
        self.horizontalLayout.addWidget(self.key7)
        self.key8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key8.sizePolicy().hasHeightForWidth())
        self.key8.setSizePolicy(sizePolicy)
        self.key8.setObjectName("key8")
        self.pianokey.addButton(self.key8)
        self.horizontalLayout.addWidget(self.key8)
        self.key9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key9.sizePolicy().hasHeightForWidth())
        self.key9.setSizePolicy(sizePolicy)
        self.key9.setObjectName("key9")
        self.pianokey.addButton(self.key9)
        self.horizontalLayout.addWidget(self.key9)
        self.key10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key10.sizePolicy().hasHeightForWidth())
        self.key10.setSizePolicy(sizePolicy)
        self.key10.setObjectName("key10")
        self.pianokey.addButton(self.key10)
        self.horizontalLayout.addWidget(self.key10)
        self.key11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key11.sizePolicy().hasHeightForWidth())
        self.key11.setSizePolicy(sizePolicy)
        self.key11.setObjectName("key11")
        self.pianokey.addButton(self.key11)
        self.horizontalLayout.addWidget(self.key11)
        self.key12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key12.sizePolicy().hasHeightForWidth())
        self.key12.setSizePolicy(sizePolicy)
        self.key12.setObjectName("key12")
        self.pianokey.addButton(self.key12)
        self.horizontalLayout.addWidget(self.key12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Piano"))
        self.key1.setText(_translate("MainWindow", "1"))
        self.key2.setText(_translate("MainWindow", "2"))
        self.key3.setText(_translate("MainWindow", "3"))
        self.key4.setText(_translate("MainWindow", "4"))
        self.key5.setText(_translate("MainWindow", "5"))
        self.key6.setText(_translate("MainWindow", "6"))
        self.key7.setText(_translate("MainWindow", "7"))
        self.key8.setText(_translate("MainWindow", "8"))
        self.key9.setText(_translate("MainWindow", "9"))
        self.key10.setText(_translate("MainWindow", "0"))
        self.key11.setText(_translate("MainWindow", "-"))
        self.key12.setText(_translate("MainWindow", "="))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 535)
        MainWindow.setMinimumSize(QtCore.QSize(665, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 13))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 13))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_5.setSizeIncrement(QtCore.QSize(0, 13))
        self.pushButton_5.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_4.setSizeIncrement(QtCore.QSize(0, 13))
        self.pushButton_4.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 13))
        self.pushButton.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Passgener"))
        self.label.setText(_translate("MainWindow", "Уведіть слово, яке Вам легко запам\'ятати:"))
        self.label_2.setText(_translate("MainWindow", "Уведіть платформу, для якої Ви генеруєте пароль:"))
        self.label_3.setText(_translate("MainWindow", "Згенерований пароль:"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", "Проста генерація"))
        self.pushButton_2.setText(_translate("MainWindow", "Складна генерація"))
        self.pushButton_5.setText(_translate("MainWindow", "Випадкова генерація"))
        self.pushButton_4.setText(_translate("MainWindow", "Зберегти пароль у базу"))
        self.pushButton.setText(_translate("MainWindow", "Скопіювати пароль"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Генерація пароля"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Платформа"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_6.setText(_translate("MainWindow", "Оновити таблицю"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Зчитування паролів"))

# own code:
class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        self.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Dialog from database")
        self.pushButton.setText("Ok")
        self.label.setText("Пароль записано у базу")

    def btnClosed(self):
        self.close()
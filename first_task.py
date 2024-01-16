# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_task.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 470)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(159, 221, 221, 255), stop:1 rgba(255, 255, 255, 255));")
        self.additem_pushButton = QtWidgets.QPushButton(Dialog,clicked=lambda:self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(20, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        self.additem_pushButton.setFont(font)
        self.additem_pushButton.setStyleSheet("background-color: rgb(119, 179, 179);")
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(Dialog, clicked=lambda:self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(190, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        self.deleteitem_pushButton_2.setFont(font)
        self.deleteitem_pushButton_2.setStyleSheet("background-color: rgb(119, 179, 179);")
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(Dialog,clicked=lambda:self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(360, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(11)
        self.clearall_pushButton_3.setFont(font)
        self.clearall_pushButton_3.setStyleSheet("background-color: rgb(119, 179, 179);")
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.additem_lineEdit.setGeometry(QtCore.QRect(20, 130, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.additem_lineEdit.setFont(font)
        self.additem_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(Dialog)
        self.mylist_listWidget.setGeometry(QtCore.QRect(20, 250, 471, 192))
        self.mylist_listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 431, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_it(self):
        item=self.additem_lineEdit.text()
        self.mylist_listWidget.addItem(item)
        self.additem_lineEdit.setText("")
        self.additem_lineEdit.setText("")
    def delete_it(self):
        clicked=self.mylist_listWidget.currentRow()
       # self.additem_lineEdit.setText(str(clicked))
        self.mylist_listWidget.takeItem(clicked)

    def clear_it(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " To Do List"))
        self.additem_pushButton.setText(_translate("Dialog", "Add Item To The List"))
        self.deleteitem_pushButton_2.setText(_translate("Dialog", "Delete Item From List"))
        self.clearall_pushButton_3.setText(_translate("Dialog", "Clear The List"))
        self.label.setText(_translate("Dialog", "To-Do List"))
        self.label_2.setText(_translate("Dialog", "-Lets plan your day, make a to-do list....."))
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice
from PyQt5.QtGui import QPixmap

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 304)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(212, 141, 105, 255), stop:1 rgba(255, 255, 255, 255));")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(30, 70, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet("background-color:rgb(231, 142, 106);")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 110, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("background-color:rgb(231, 142, 106);")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 150, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("background-color:rgb(231, 142, 106);")
        self.radioButton.clicked.connect(lambda: self.update_choice("rock"))
        self.radioButton_2.clicked.connect(lambda: self.update_choice("paper"))
        self.radioButton_3.clicked.connect(lambda: self.update_choice("scissors"))
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(96, 230, 171, 31))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog, clicked=lambda: self.play_game())
        self.pushButton.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 341, 41))
        self.label_2.setObjectName("label_2")


        self.result_label = QtWidgets.QLabel(Dialog)
        self.result_label.setGeometry(QtCore.QRect(30, 190, 341, 31))
        self.result_label.setObjectName("result_label")

        ##self.image_label = QtWidgets.QLabel(Dialog)
        ##self.image_label.setGeometry(QtCore.QRect(270, 70, 111, 111))
        ##self.image_label.setObjectName("image_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "ROCK"))
        self.radioButton_2.setText(_translate("Dialog", "PAPER"))
        self.radioButton_3.setText(_translate("Dialog", "SCISSOR"))  
        self.pushButton.setText(_translate("Dialog", "PLAY"))
        self.label_2.setText(_translate("Dialog", "ROCK-PAPER-SCISSOR GAME"))

    def update_choice(self, choice):
        # Add any additional logic for updating the choice if needed
        pass

    def play_game(self):
        choices = ["rock", "paper", "scissors"]
        player_choice = "rock"  # You need to get the player's choice from the radio buttons
        computer_choice = choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        result_text = f"You chose {player_choice}. Computer chose {computer_choice}. {result}"
        self.result_label.setText(result_text)

        image_path = f"images/{computer_choice}.png"
        #pixmap = QPixmap(image_path)
        #self.image_label.setPixmap(pixmap)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

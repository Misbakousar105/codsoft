from PyQt5 import QtCore, QtGui, QtWidgets
from calculator_ui import Ui_Dialog

class CalculatorApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to their respective functions
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.percent)
        self.pushButton_3.clicked.connect(self.clear_entry)
        self.pushButton_4.clicked.connect(lambda: self.append_operator("/"))
        self.pushButton_5.clicked.connect(lambda: self.append_number("7"))
        self.pushButton_6.clicked.connect(lambda: self.append_number("8"))
        self.pushButton_7.clicked.connect(lambda: self.append_number("9"))
        self.pushButton_8.clicked.connect(lambda: self.append_operator("*"))
        self.pushButton_9.clicked.connect(lambda: self.append_number("4"))
        self.pushButton_10.clicked.connect(lambda: self.append_number("5"))
        self.pushButton_11.clicked.connect(lambda: self.append_number("6"))
        self.pushButton_12.clicked.connect(lambda: self.append_operator("-"))
        self.pushButton_13.clicked.connect(lambda: self.append_number("1"))
        self.pushButton_14.clicked.connect(lambda: self.append_number("2"))
        self.pushButton_15.clicked.connect(lambda: self.append_number("3"))
        self.pushButton_16.clicked.connect(lambda: self.append_operator("+"))
        self.pushButton_17.clicked.connect(lambda: self.append_number("0"))
        self.pushButton_18.clicked.connect(self.append_decimal)
        self.pushButton_20.clicked.connect(self.calculate)

        # Variables to store the current input and result
        self.current_input = ""
        self.result = 0.0

    def clear(self):
        self.current_input = ""
        self.update_display()

    def percent(self):
        try:
            value = float(self.current_input)
            result = value / 100.0
            self.current_input = str(result)
            self.update_display()
        except ValueError:
            self.current_input = "Error"
            self.update_display()

    def clear_entry(self):
        self.current_input = self.current_input[:-1]
        self.update_display()

    def append_number(self, number):
        self.current_input += number
        self.update_display()

    def append_operator(self, operator):
        self.current_input += f" {operator} "
        self.update_display()

    def append_decimal(self):
        if "." not in self.current_input:
            self.current_input += "."
            self.update_display()

    def calculate(self):
        try:
            self.result = eval(self.current_input)
            self.current_input = str(self.result)
            self.update_display()
        except Exception:
            self.current_input = "Error"
            self.update_display()

    def update_display(self):
        self.lineEdit.setText(self.current_input)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec_())

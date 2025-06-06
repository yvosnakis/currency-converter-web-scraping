from PySide6.QtWidgets import QWidget
from ui_widget import Ui_widget
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Currency Converter")

        self.convert_button.clicked.connect(self.convert_currency)

    def get_currency(self, from_currency, to_currency):
        try:
            url = f'https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1'
            content = requests.get(url).text
            soup = BeautifulSoup(content, 'html.parser')
            rate = soup.find("span", class_="ccOutputRslt").get_text()
            rate = float(rate[:-4])
            return rate
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            return None

    def show_currency(self, rate):
        try:
            input_text = float(self.amount_lineEdit.text())
            from_currency = self.comboBox_1.currentText()
            to_currency = self.comboBox_2.currentText()
            output = round(input_text * rate, 2)
            message = f'{input_text} {from_currency} is {output} {to_currency}'
            self.results_display.setText(message)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")

    def convert_currency(self):
        amount = self.amount_lineEdit.text()
        if not amount:
            QMessageBox.warning(self, "Input Error", "Please enter an amount.")
            return

        from_currency = self.comboBox_1.currentText()
        to_currency = self.comboBox_2.currentText()

        rate = self.get_currency(from_currency, to_currency)
        if rate is not None:
            self.show_currency(rate)



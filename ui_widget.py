# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(280, 367)
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 221, 51))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 91, 16))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.amount_lineEdit = QLineEdit(widget)
        self.amount_lineEdit.setObjectName(u"amount_lineEdit")
        self.amount_lineEdit.setGeometry(QRect(10, 100, 261, 31))
        self.amount_lineEdit.setStyleSheet(u"*{\n"
"border-radius:10px;\n"
"border:0.5px solid gray;\n"
"padding: 5px;\n"
"}")
        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 91, 16))
        self.label_3.setFont(font1)
        self.comboBox_1 = QComboBox(widget)
        self.comboBox_1.addItem(QIcon("Flags/US-Flag.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/UK-Flag.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/EUR.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/CA-Flag.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/BRL.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/CNY.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/SEK.png"),"")
        self.comboBox_1.addItem(QIcon("Flags/THB.png"),"")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(0, 170, 111, 31))
        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 160, 61, 61))
        self.label_4.setPixmap(QPixmap(u":/Other Images/Arrows.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 150, 91, 16))
        self.label_5.setFont(font1)
        self.results_display = QLabel(widget)
        self.results_display.setObjectName(u"results_display")
        self.results_display.setGeometry(QRect(20, 240, 251, 21))
        self.results_display.setFont(font1)
        self.convert_button = QPushButton(widget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setGeometry(QRect(70, 290, 141, 51))
        self.convert_button.setFont(font1)
        self.convert_button.setStyleSheet(u"*{\n"
"background-color: #09A67B;\n"
"color: white;\n"
"border: none;\n"
"border-radius:8px;\n"
"}")
        self.comboBox_2 = QComboBox(widget)
        self.comboBox_2.addItem(QIcon("Flags/US-Flag.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/UK-Flag.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/EUR.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/CA-Flag.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/BRL.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/CNY.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/SEK.png"),"")
        self.comboBox_2.addItem(QIcon("Flags/THB.png"),"")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(170, 170, 111, 31))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("widget", u"Currency Converter", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"Enter Amount", None))
        self.amount_lineEdit.setPlaceholderText(QCoreApplication.translate("widget", u"Enter Amount Here", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"From", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("widget", u"USD", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("widget", u"GBP", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("widget", u"EUR", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("widget", u"CAD", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("widget", u"BRL", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("widget", u"CNY", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("widget", u"SEK", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("widget", u"THB", None))

        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("widget", u"To", None))
        self.results_display.setText("")
        self.convert_button.setText(QCoreApplication.translate("widget", u"Get Exchange Rate", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("widget", u"USD", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("widget", u"GBP", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("widget", u"EUR", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("widget", u"CAD", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("widget", u"BRL", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("widget", u"CNY", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("widget", u"SEK", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("widget", u"THB", None))

    # retranslateUi


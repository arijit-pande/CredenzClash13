# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created: Thu Aug 29 12:17:32 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(829, 629)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-50, 90, 451, 411))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("flag-dark.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 100, 381, 51))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(490, 210, 271, 101))
        self.lcdNumber.setStyleSheet(_fromUtf8("color: rgb(17, 23, 139);"))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 530, 711, 61))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);\n"
"font: 63 16pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">FINAL SCORE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Report your score to the nearest Clash 13 volunteer</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


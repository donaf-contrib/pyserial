"""
___author   : Dona F.

__desc      : Python Serial Monitor

"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 266)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.label_3.setObjectName("label_3")
        self.cmbPort = QtWidgets.QComboBox(self.groupBox)
        self.cmbPort.setGeometry(QtCore.QRect(90, 30, 69, 22))
        self.cmbPort.setObjectName("cmbPort")
        self.txtLadder = QtWidgets.QLineEdit(self.groupBox)
        self.txtLadder.setGeometry(QtCore.QRect(90, 70, 131, 20))
        self.txtLadder.setObjectName("txtLadder")
        self.txtOffset = QtWidgets.QLineEdit(self.groupBox)
        self.txtOffset.setGeometry(QtCore.QRect(90, 100, 131, 20))
        self.txtOffset.setObjectName("txtOffset")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 311, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtRaw = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.txtRaw.setGeometry(QtCore.QRect(10, 20, 291, 71))
        self.txtRaw.setObjectName("txtRaw")
        self.btnConnect = QtWidgets.QPushButton(Dialog)
        self.btnConnect.setGeometry(QtCore.QRect(420, 220, 91, 31))
        self.btnConnect.setObjectName("btnConnect")
        self.lbDepth = QtWidgets.QLabel(Dialog)
        self.lbDepth.setGeometry(QtCore.QRect(410, 60, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lbDepth.setFont(font)
        self.lbDepth.setObjectName("lbDepth")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Parameters"))
        self.label.setText(_translate("Dialog", "Port"))
        self.label_2.setText(_translate("Dialog", "Ladder"))
        self.label_3.setText(_translate("Dialog", "Offset"))
        self.groupBox_2.setTitle(_translate("Dialog", "Raw Data"))
        self.btnConnect.setText(_translate("Dialog", "Connect"))
        self.lbDepth.setText(_translate("Dialog", "DEPTH"))



"""
___author   : Dona F.

__desc      : Python Serial Monitor

"""

import binascii
import math

from PyQt5 import QtCore, QtWidgets, QtSerialPort

from guiform import Ui_Dialog


class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnConnect.clicked.connect(self.slot_clicked_connect_button)
        self.serial = QtSerialPort.QSerialPort(self)
        self.serial.readyRead.connect(self.onReadyRead)
        self._fill_serial_info()

    def onReadyRead(self):
        val_ldr = float(self.ui.txtLadder.text())
        val_off = float(self.ui.txtOffset.text())
        while self.serial.bytesAvailable() >= 14:
            buff = self.serial.read(14)
            rd = str(binascii.hexlify(buff), "ascii", "replace")
            if rd.startswith("68"):
                val_ag = float(rd[10:14]) / 100
                self.ui.txtRaw.insertPlainText(rd)
                self.ui.txtRaw.insertPlainText("\n")
                s = math.radians(val_ag)
                val_deg = float(math.sin(s))
                val_depth = float((val_deg * val_ldr) - val_off)
                self.ui.lbDepth.setText('%05.2F' % val_depth)

    def _fill_serial_info(self):
        self.ui.cmbPort.clear()
        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ui.cmbPort.addItem(info.portName())

    def _open(self, port_name, baudrate=QtSerialPort.QSerialPort.Baud9600):
        info = QtSerialPort.QSerialPortInfo(port_name)
        self.serial.setPort(info)
        self.serial.setBaudRate(baudrate)
        return self.serial.open(QtCore.QIODevice.ReadWrite)

    def connect_serial(self):
        serial_info = {"port_name": self.ui.cmbPort.currentText()}
        status = self._open(**serial_info)
        return status

    def disconnect_serial(self):
        return self.serial.close()

    @QtCore.pyqtSlot(name="clickedConnectButton")
    def slot_clicked_connect_button(self):
        if self.serial.isOpen():
            self.disconnect_serial()
        else:
            self.connect_serial()
        self.ui.btnConnect.setText(
            "Stop" if self.serial.isOpen() else "Connect"
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.resize(640, 300)
    w.show()
    sys.exit(app.exec_())
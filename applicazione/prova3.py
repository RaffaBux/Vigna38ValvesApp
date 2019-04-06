from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TempGUI(object):
    def setupUi(self, TempGUI):
        TempGUI.setObjectName("TempGUI")
        TempGUI.resize(464, 387)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TempGUI.setWindowIcon(icon)
        self.temp_grid = QtWidgets.QWidget(TempGUI)
        self.temp_grid.setObjectName("temp_grid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp_grid)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tempAttLabel2 = QtWidgets.QLabel(self.temp_grid)
        self.tempAttLabel2.setObjectName("tempAttLabel2")
        self.gridLayout_2.addWidget(self.tempAttLabel2, 1, 0, 1, 1)
        self.monitoraggioButton = QtWidgets.QPushButton(self.temp_grid)
        self.monitoraggioButton.setObjectName("monitoraggioButton")
        self.gridLayout_2.addWidget(self.monitoraggioButton, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.statoLabel = QtWidgets.QLabel(self.temp_grid)
        self.statoLabel.setObjectName("statoLabel")
        self.gridLayout_2.addWidget(self.statoLabel, 5, 2, 1, 1)
        self.tempModLabel = QtWidgets.QLabel(self.temp_grid)
        self.tempModLabel.setObjectName("tempModLabel")
        self.gridLayout_2.addWidget(self.tempModLabel, 2, 0, 1, 1)
        self.tempAttLabel1 = QtWidgets.QLabel(self.temp_grid)
        self.tempAttLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tempAttLabel1.setObjectName("tempAttLabel1")
        self.gridLayout_2.addWidget(self.tempAttLabel1, 1, 1, 1, 1)
        self.celsiusLabel1 = QtWidgets.QLabel(self.temp_grid)
        self.celsiusLabel1.setObjectName("celsiusLabel1")
        self.gridLayout_2.addWidget(self.celsiusLabel1, 1, 2, 1, 1)
        self.celsiusLabel2 = QtWidgets.QLabel(self.temp_grid)
        self.celsiusLabel2.setObjectName("celsiusLabel2")
        self.gridLayout_2.addWidget(self.celsiusLabel2, 2, 2, 1, 1)
        self.confermaButton = QtWidgets.QPushButton(self.temp_grid)
        self.confermaButton.setObjectName("confermaButton")
        self.gridLayout_2.addWidget(self.confermaButton, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.tempSpin = QtWidgets.QDoubleSpinBox(self.temp_grid)
        self.tempSpin.setWrapping(False)
        self.tempSpin.setFrame(True)
        self.tempSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tempSpin.setReadOnly(False)
        self.tempSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.tempSpin.setAccelerated(False)
        self.tempSpin.setKeyboardTracking(True)
        self.tempSpin.setPrefix("")
        self.tempSpin.setDecimals(1)
        self.tempSpin.setMinimum(5.0)
        self.tempSpin.setMaximum(25.0)
        self.tempSpin.setSingleStep(0.1)
        self.tempSpin.setProperty("value", 16.0)
        self.tempSpin.setObjectName("tempSpin")
        self.gridLayout_2.addWidget(self.tempSpin, 2, 1, 1, 1)
        TempGUI.setCentralWidget(self.temp_grid)

        self.retranslateUi(TempGUI)
        QtCore.QMetaObject.connectSlotsByName(TempGUI)

    def retranslateUi(self, TempGUI):
        _translate = QtCore.QCoreApplication.translate
        TempGUI.setWindowTitle(_translate("TempGUI", "******"))
        self.tempAttLabel2.setText(_translate("TempGUI", "Temperatura ******:"))
        self.monitoraggioButton.setText(_translate("TempGUI", "Monitoraggio"))
        self.statoLabel.setText(_translate("TempGUI", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))
        self.tempModLabel.setText(_translate("TempGUI", "Temperatura modificabile: "))
        self.tempAttLabel1.setText(_translate("TempGUI", "---"))
        self.celsiusLabel1.setText(_translate("TempGUI", "°C"))
        self.celsiusLabel2.setText(_translate("TempGUI", "°C"))
        self.confermaButton.setText(_translate("TempGUI", "Conferma"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TempGUI = QtWidgets.QMainWindow()
    ui = Ui_TempGUI()
    ui.setupUi(TempGUI)
    TempGUI.show()
    sys.exit(app.exec_())


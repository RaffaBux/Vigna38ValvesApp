from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGUI(QtWidgets.QMainWindow):                            #classe mainWindow

    def __init__(self):
        super(Ui_MainGUI, self).__init__()
        self.setupUi(self)
        self.show()                 #Maximized()

    def setupUi(self, MainGUI):                                     #grafica login
        MainGUI.setObjectName("MainGUI")
        MainGUI.resize(400,500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainGUI.setWindowIcon(icon)
        MainGUI.setStyleSheet("background-color: rgb(217, 240, 255);")
        self.main_grid = QtWidgets.QWidget(MainGUI)
        self.main_grid.setObjectName("main_grid")
        self.gridLayout = QtWidgets.QGridLayout(self.main_grid)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.main_grid)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 3, 1, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.main_grid)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.main_grid)
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 1, 1, 1)
        self.fallimentoLabel = QtWidgets.QLabel(self.main_grid)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.fallimentoLabel.setFont(font)
        self.fallimentoLabel.setText("")
        self.fallimentoLabel.setObjectName("fallimentoLabel")
        self.gridLayout.addWidget(self.fallimentoLabel, 4, 1, 1, 2)
        self.inviaButton = QtWidgets.QPushButton(self.main_grid)
        font = QtGui.QFont()
        font.setKerning(False)
        self.inviaButton.setFont(font)
        self.inviaButton.setObjectName("inviaButton")
        self.inviaButton.clicked.connect(lambda: self.invia(self.fallimentoLabel))
        self.gridLayout.addWidget(self.inviaButton, 6, 1, 1, 2)
        self.usernameLine = QtWidgets.QLineEdit(self.main_grid)
        self.usernameLine.setObjectName("usernameLine")
        self.gridLayout.addWidget(self.usernameLine, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 1, 1, 1)
        MainGUI.setCentralWidget(self.main_grid)
        self.retranslateUi(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)

    def retranslateUi(self, MainGUI):
        _translate = QtCore.QCoreApplication.translate
        MainGUI.setWindowTitle(_translate("MainGUI", "LOGIN"))
        self.passwordLabel.setText(_translate("MainGUI", "password:"))
        self.usernameLabel.setText(_translate("MainGUI", "username:"))
        self.inviaButton.setText(_translate("MainGUI", "INVIA"))

    def invia(self,fallimento):                                     #funzione invio credenziali login
        global userText, passwdText
        import socket
        client0=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client0.connect(("192.168.0.3",8282)) #indirizzo server
        userText=self.usernameLine.text()
        passwdText=self.passwordLine.text()
        cred=userText+","+passwdText+",0"
        client0.send(cred.encode())
        try:
            risp=client0.recv(1024).decode()
            if risp=="credenziali_errate":
                self.fallimentoLabel.setText("credenziali errate")
                client0.close()
            elif risp=="errore_connessione":
                self.fallimentoLabel.setText("errore connessione")
                client0.close()
            elif risp=="accesso_corretto":
                self.fallimentoLabel.setText("accesso corretto")
                client0.close()
                self.setupUiSec(self)
        except:
            self.fallimentoLabel.setText("errore connessione")
            client0.close()

    def closeEvent(self, event):                                    #evento di chiusura della main window
        app.closeAllWindows()

    def setupUiSec(self, MainGUI):                                  #grafica di refresh post-login (lista)
        from threading import Thread
        threadMainPace=True
        MainGUI.setObjectName("MainGUI")
        MainGUI.resize(400,500)
        MainGUI.setWindowModality(QtCore.Qt.WindowModal)
        MainGUI.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainGUI.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_grappoloicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainGUI.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mappacantLabel = QtWidgets.QLabel(self.centralwidget)
        self.mappacantLabel.setObjectName("mappacantLabel")
        self.gridLayout_2.addWidget(self.mappacantLabel, 1, 0, 1, 1)
        self.list_scrollarea = QtWidgets.QScrollArea(self.centralwidget)
        self.list_scrollarea.setStyleSheet("background-color: rgb(233, 236, 255);")
        self.list_scrollarea.setWidgetResizable(True)
        self.list_scrollarea.setObjectName("list_scrollarea")
        self.list_grid = QtWidgets.QWidget()
        self.list_grid.setGeometry(QtCore.QRect(0, 0, 102, 1101))
        self.list_grid.setObjectName("list_grid")
        self.gridLayout = QtWidgets.QGridLayout(self.list_grid)
        self.gridLayout.setObjectName("gridLayout")
        self.vv16 = QtWidgets.QPushButton(self.list_grid)
        self.vv16.setObjectName("vv16")
        self.vv16.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv16, 3, 0, 1, 1)
        self.locale2 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale2.setFont(font)
        self.locale2.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale2.setObjectName("locale2")
        self.locale2.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.locale2, 9, 0, 1, 1)
        self.vv14 = QtWidgets.QPushButton(self.list_grid)
        self.vv14.setObjectName("vv14")
        self.vv14.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv14, 1, 0, 1, 1)
        self.vv22 = QtWidgets.QPushButton(self.list_grid)
        self.vv22.setObjectName("vv22")
        self.vv22.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv22, 21, 0, 1, 1)
        self.vv33 = QtWidgets.QPushButton(self.list_grid)
        self.vv33.setObjectName("vv33")
        self.vv33.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv33, 32, 0, 1, 1)
        self.vv7 = QtWidgets.QPushButton(self.list_grid)
        self.vv7.setObjectName("vv7")
        self.vv7.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv7, 13, 0, 1, 1)
        self.vv32 = QtWidgets.QPushButton(self.list_grid)
        self.vv32.setObjectName("vv32")
        self.vv32.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv32, 31, 0, 1, 1)
        self.vv19 = QtWidgets.QPushButton(self.list_grid)
        self.vv19.setObjectName("vv19")
        self.vv19.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv19, 6, 0, 1, 1)
        self.vv15 = QtWidgets.QPushButton(self.list_grid)
        self.vv15.setObjectName("vv15")
        self.vv15.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv15, 2, 0, 1, 1)
        self.vv27 = QtWidgets.QPushButton(self.list_grid)
        self.vv27.setObjectName("vv27")
        self.vv27.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv27, 26, 0, 1, 1)
        self.vv25 = QtWidgets.QPushButton(self.list_grid)
        self.vv25.setObjectName("vv25")
        self.vv25.clicked.connect(lambda: self.functemp()())
        self.gridLayout.addWidget(self.vv25, 24, 0, 1, 1)
        self.vv23 = QtWidgets.QPushButton(self.list_grid)
        self.vv23.setObjectName("vv23")
        self.vv23.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv23, 22, 0, 1, 1)
        self.vv8 = QtWidgets.QPushButton(self.list_grid)
        self.vv8.setObjectName("vv8")
        self.vv8.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv8, 14, 0, 1, 1)
        self.vv29 = QtWidgets.QPushButton(self.list_grid)
        self.vv29.setObjectName("vv29")
        self.vv29.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv29, 28, 0, 1, 1)
        self.vv30 = QtWidgets.QPushButton(self.list_grid)
        self.vv30.setObjectName("vv30")
        self.vv30.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv30, 29, 0, 1, 1)
        self.vv17 = QtWidgets.QPushButton(self.list_grid)
        self.vv17.setObjectName("vv17")
        self.vv17.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv17, 4, 0, 1, 1)
        self.locale3 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale3.setFont(font)
        self.locale3.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale3.setObjectName("locale3")
        self.locale3.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.locale3, 20, 0, 1, 1)
        self.vv28 = QtWidgets.QPushButton(self.list_grid)
        self.vv28.setObjectName("vv28")
        self.vv28.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv28, 27, 0, 1, 1)
        self.vv24 = QtWidgets.QPushButton(self.list_grid)
        self.vv24.setObjectName("vv24")
        self.vv24.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv24, 23, 0, 1, 1)
        self.vv20 = QtWidgets.QPushButton(self.list_grid)
        self.vv20.setObjectName("vv20")
        self.vv20.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv20, 7, 0, 1, 1)
        self.vv18 = QtWidgets.QPushButton(self.list_grid)
        self.vv18.setObjectName("vv18")
        self.vv18.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv18, 5, 0, 1, 1)
        self.vv21 = QtWidgets.QPushButton(self.list_grid)
        self.vv21.setObjectName("vv21")
        self.vv21.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv21, 8, 0, 1, 1)
        self.vv10 = QtWidgets.QPushButton(self.list_grid)
        self.vv10.setObjectName("vv10")
        self.vv10.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv10, 16, 0, 1, 1)
        self.vv31 = QtWidgets.QPushButton(self.list_grid)
        self.vv31.setObjectName("vv31")
        self.vv31.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv31, 30, 0, 1, 1)
        self.vv26 = QtWidgets.QPushButton(self.list_grid)
        self.vv26.setObjectName("vv26")
        self.vv26.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv26, 25, 0, 1, 1)
        self.vv11 = QtWidgets.QPushButton(self.list_grid)
        self.vv11.setObjectName("vv11")
        self.vv11.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv11, 17, 0, 1, 1)
        self.vv12 = QtWidgets.QPushButton(self.list_grid)
        self.vv12.setObjectName("vv12")
        self.vv12.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv12, 18, 0, 1, 1)
        self.vv13 = QtWidgets.QPushButton(self.list_grid)
        self.vv13.setObjectName("vv13")
        self.vv13.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv13, 19, 0, 1, 1)
        self.vv6 = QtWidgets.QPushButton(self.list_grid)
        self.vv6.setObjectName("vv6")
        self.vv6.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv6, 12, 0, 1, 1)
        self.vv4 = QtWidgets.QPushButton(self.list_grid)
        self.vv4.setObjectName("vv4")
        self.vv4.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv4, 10, 0, 1, 1)
        self.vv5 = QtWidgets.QPushButton(self.list_grid)
        self.vv5.setObjectName("vv5")
        self.vv5.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv5, 11, 0, 1, 1)
        self.locale1 = QtWidgets.QPushButton(self.list_grid)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.locale1.setFont(font)
        self.locale1.setStyleSheet("background-color: rgb(221, 237, 255);")
        self.locale1.setObjectName("locale1")
        self.locale1.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.locale1, 0, 0, 1, 1)
        self.vv9 = QtWidgets.QPushButton(self.list_grid)
        self.vv9.setObjectName("vv9")
        self.vv9.clicked.connect(lambda: self.functemp())
        self.gridLayout.addWidget(self.vv9, 15, 0, 1, 1)
        self.list_scrollarea.setWidget(self.list_grid)
        self.gridLayout_2.addWidget(self.list_scrollarea, 0, 1, 2, 1)
        self.top_grid = QtWidgets.QGridLayout()
        self.top_grid.setObjectName("top_grid")
        self.dataoraTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dataoraTimeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataoraTimeEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.dataoraTimeEdit.setFrame(False)
        self.dataoraTimeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataoraTimeEdit.setReadOnly(True)
        self.dataoraTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dataoraTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dataoraTimeEdit.setMaximumDate(QtCore.QDate(10000, 12, 31))
        self.dataoraTimeEdit.setObjectName("dataoraTimeEdit")
        self.top_grid.addWidget(self.dataoraTimeEdit, 0, 1, 1, 1)
        dataora=Thread(target=self.ora, args=[lambda: threadMainPace], daemon=True)
        dataora.start()
        self.tempestLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempestLabel.setObjectName("tempestLabel")
        self.top_grid.addWidget(self.tempestLabel, 0, 0, 1, 1)
        tempest=Thread(target=self.tempesterna, args=[self.tempestLabel, lambda:threadMainPace], daemon=True)
        tempest.start()
        self.gridLayout_2.addLayout(self.top_grid, 0, 0, 1, 1)
        MainGUI.setCentralWidget(self.centralwidget)
        self.retranslateUiSec(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)

    def retranslateUiSec(self, MainGUI):
        _translate = QtCore.QCoreApplication.translate
        MainGUI.setWindowTitle(_translate("MainGUI", "MAPPA VASI VINARI"))
        self.mappacantLabel.setPixmap(QtGui.QPixmap("4_Planimetria_Botti.png"))
        self.vv16.setText(_translate("MainGUI", "v.v. 16"))
        self.locale2.setText(_translate("MainGUI", "LOCALE 2"))
        self.vv14.setText(_translate("MainGUI", "v.v. 14"))
        self.vv22.setText(_translate("MainGUI", "v.v. 22"))
        self.vv33.setText(_translate("MainGUI", "v.v. 33"))
        self.vv7.setText(_translate("MainGUI", "v.v. 7"))
        self.vv32.setText(_translate("MainGUI", "v.v. 32"))
        self.vv19.setText(_translate("MainGUI", "v.v. 19"))
        self.vv15.setText(_translate("MainGUI", "v.v. 15"))
        self.vv27.setText(_translate("MainGUI", "v.v. 27"))
        self.vv25.setText(_translate("MainGUI", "v.v. 25"))
        self.vv23.setText(_translate("MainGUI", "v.v. 23"))
        self.vv8.setText(_translate("MainGUI", "v.v. 8"))
        self.vv29.setText(_translate("MainGUI", "v.v. 29"))
        self.vv30.setText(_translate("MainGUI", "v.v. 30"))
        self.vv17.setText(_translate("MainGUI", "v.v. 17"))
        self.locale3.setText(_translate("MainGUI", "LOCALE 3"))
        self.vv28.setText(_translate("MainGUI", "v.v. 28"))
        self.vv24.setText(_translate("MainGUI", "v.v. 24"))
        self.vv20.setText(_translate("MainGUI", "v.v. 20"))
        self.vv18.setText(_translate("MainGUI", "v.v. 18"))
        self.vv21.setText(_translate("MainGUI", "v.v. 21"))
        self.vv10.setText(_translate("MainGUI", "v.v. 10"))
        self.vv31.setText(_translate("MainGUI", "v.v. 31"))
        self.vv26.setText(_translate("MainGUI", "v.v. 26"))
        self.vv11.setText(_translate("MainGUI", "v.v. 11"))
        self.vv12.setText(_translate("MainGUI", "v.v. 12"))
        self.vv13.setText(_translate("MainGUI", "v.v. 13"))
        self.vv6.setText(_translate("MainGUI", "v.v. 6"))
        self.vv4.setText(_translate("MainGUI", "v.v. 4"))
        self.vv5.setText(_translate("MainGUI", "v.v. 5"))
        self.locale1.setText(_translate("MainGUI", "LOCALE 1"))
        self.vv9.setText(_translate("MainGUI", "v.v. 9"))
        self.tempestLabel.setText(_translate("MainGUI", "Temperatura esterna: *****°C"))

    def ora(self, exit):                                            #funzione thread di ora e data
        import datetime
        import time as c
        while exit():
            try:
                tempo=datetime.datetime.now()
                self.dataoraTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(tempo.year, tempo.month, tempo.day), QtCore.QTime(tempo.hour, tempo.minute, tempo.second)))
                c.sleep(1)
            except:
                self.dataoraTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate('**', '**', '**'), QtCore.QTime('**', '**', '**')))
                c.sleep(1)

    def tempesterna(self, tempestLabel, exit):                      #funzione thread temperatura esterna
        import time as a
        import socket
        cred=userText+","+passwdText+",1"
        while exit():
            try:
                client1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client1.connect(("192.168.0.3",8282)) #indirizzo server 
                client1.send(cred.encode())
                risp=client1.recv(1024).decode()
                self.tempestLabel.setText("Temperatura esterna: "+str(risp)+"°C")
                client1.close()
                a.sleep(30)
            except RuntimeError:
                pass
            except:
                self.tempestLabel.setText("Temperatura esterna: *****°C")
                client1.close()
                a.sleep(60)

    def functemp(self):                                             #funzione apertura window b/l
        sendr=self.sender().objectName()
        if sendr[0]=="l":
            sendr="Locale "+sendr[6]
        else:
            try:
                sendr="Vaso vinario "+sendr[2]+sendr[3]
            except:
                sendr="Vaso vinario "+sendr[2]
        ui=Ui_TempGUI(sendr)

class Ui_TempGUI(QtWidgets.QMainWindow):

    def __init__(self, sendr):
        super(Ui_TempGUI, self).__init__()
        self.setupUi(self, sendr)

    def closeEvent(self, event):                                    #evento di chiusura window b/l
        quit_event.set()

    def setupUi(self, TempGUI, name):                               #grafica window b/l
        from threading import Thread, Event
        global quit_event
        quit_event = Event()
        TempGUI.resize(464, 387)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        TempGUI.setObjectName("TempGUI")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TempGUI.setWindowIcon(icon)
        self.temp_grid = QtWidgets.QWidget(TempGUI)
        self.temp_grid.setObjectName("temp_grid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp_grid)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tempModLabel = QtWidgets.QLabel(self.temp_grid)
        self.tempModLabel.setObjectName("tempModLabel")
        self.gridLayout_2.addWidget(self.tempModLabel, 3, 0, 1, 1)
        self.statoLabel = QtWidgets.QLabel(self.temp_grid)
        self.statoLabel.setObjectName("statoLabel")
        self.gridLayout_2.addWidget(self.statoLabel, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 7, 1, 1, 1)
        self.tempAttLabel2 = QtWidgets.QLabel(self.temp_grid)
        self.tempAttLabel2.setObjectName("tempAttLabel2")
        self.gridLayout_2.addWidget(self.tempAttLabel2, 2, 0, 1, 1)
        self.tempAttLabel1 = QtWidgets.QLabel(self.temp_grid)
        self.tempAttLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tempAttLabel1.setObjectName("tempAttLabel1")
        self.gridLayout_2.addWidget(self.tempAttLabel1, 2, 1, 1, 1)
        tempvin=Thread(target=self.tempRich, args=[self.tempAttLabel1, name, quit_event], daemon=True)
        tempvin.start()
        self.celsiusLabel1 = QtWidgets.QLabel(self.temp_grid)
        self.celsiusLabel1.setObjectName("celsiusLabel1")
        self.gridLayout_2.addWidget(self.celsiusLabel1, 2, 2, 1, 1)
        self.celsiusLabel2 = QtWidgets.QLabel(self.temp_grid)
        self.celsiusLabel2.setObjectName("celsiusLabel2")
        self.gridLayout_2.addWidget(self.celsiusLabel2, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.tempSpin = QtWidgets.QDoubleSpinBox(self.temp_grid)
        self.tempSpin.setWrapping(False)
        self.tempSpin.setFrame(True)
        self.tempSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tempSpin.setReadOnly(False)
        self.tempSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.tempSpin.setAccelerated(False)
        self.tempSpin.setKeyboardTracking(True)
        self.tempSpin.setPrefix("")
        self.tempSpin.setMinimum(5)
        self.tempSpin.setMaximum(30)
        self.tempSpin.setSingleStep(1)
        self.tempSpin.setProperty("value", 1)
        self.setDef(self.tempSpin, name)
        self.tempSpin.setObjectName("tempSpin")
        self.gridLayout_2.addWidget(self.tempSpin, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confermaButton = QtWidgets.QPushButton(self.temp_grid)
        self.confermaButton.setObjectName("confermaButton")
        self.confermaButton.clicked.connect(lambda: self.setTemp(self.tempSpin, name, self.confermaLabel))
        self.horizontalLayout.addWidget(self.confermaButton)
        self.resetButton = QtWidgets.QPushButton(self.temp_grid)
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(lambda: self.setDef(self.tempSpin, name))
        self.horizontalLayout.addWidget(self.resetButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.monitoraggioButton = QtWidgets.QPushButton(self.temp_grid)
        self.monitoraggioButton.setObjectName("monitoraggioButton")
        self.monitoraggioButton.clicked.connect(lambda: self.graficoTemp(name))
        self.horizontalLayout_2.addWidget(self.monitoraggioButton)        
        if name[0]=="V":
            self.quantitaButton = QtWidgets.QPushButton(self.temp_grid)
            self.quantitaButton.setObjectName("quantitaButton")
            self.quantitaButton.clicked.connect(lambda: self.graficoQuant(name))
            self.horizontalLayout_2.addWidget(self.quantitaButton)
            self.contenutoLabel1 = QtWidgets.QLabel(self.temp_grid)
            self.contenutoLabel1.setObjectName("contenutoLabel1")
            self.gridLayout_2.addWidget(self.contenutoLabel1, 1, 0, 1, 1)
            self.contenutoLabel2 = QtWidgets.QLabel(self.temp_grid)
            self.contenutoLabel2.setText("")
            self.contenutoLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.contenutoLabel2.setObjectName("contenutoLabel2")
            self.gridLayout_2.addWidget(self.contenutoLabel2, 1, 1, 1, 1)
            contenuto=Thread(target=self.contVaso, args=[self.contenutoLabel2, name, quit_event], daemon=True)
            contenuto.start()
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        self.confermaLabel = QtWidgets.QLabel(self.temp_grid)
        self.confermaLabel.setText("")
        self.confermaLabel.setObjectName("confermaLabel")
        self.gridLayout_2.addWidget(self.confermaLabel, 6, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statoscrLabel = QtWidgets.QLabel(self.temp_grid)
        self.statoscrLabel.setObjectName("statoscrLabel")
        self.horizontalLayout_3.addWidget(self.statoscrLabel)
        stvalv=Thread(target=self.statoValv, args=[self.statoLabel, self.statoscrLabel, name, quit_event], daemon=True)
        stvalv.start()
        self.statoLabel = QtWidgets.QLabel(self.temp_grid)
        self.statoLabel.setObjectName("statoLabel")
        self.horizontalLayout_3.addWidget(self.statoLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 9, 2, 1, 1)
        TempGUI.setCentralWidget(self.temp_grid)
        self.retranslateUi(TempGUI, name)
        QtCore.QMetaObject.connectSlotsByName(TempGUI)

    def retranslateUi(self, TempGUI, name):
        _translate = QtCore.QCoreApplication.translate
        TempGUI.setWindowTitle(_translate("TempGUI", "'"+name+"'"))
        self.monitoraggioButton.setText(_translate("TempGUI", "Monitoraggio"))
        self.tempModLabel.setText(_translate("TempGUI", "Temperatura modificabile: "))
        self.tempAttLabel2.setText(_translate("TempGUI", "Temperatura '"+name+"':"))
        self.tempAttLabel1.setText(_translate("TempGUI", "*****"))
        self.celsiusLabel1.setText(_translate("TempGUI", "°C"))
        self.celsiusLabel2.setText(_translate("TempGUI", "°C"))
        self.confermaButton.setText(_translate("TempGUI", "Conferma"))
        self.resetButton.setText(_translate("TempGUI", "Reset"))
        self.statoLabel.setText(_translate("TempGUI", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))
        self.statoscrLabel.setText(_translate("TempGUI", "off"))
        if name[0]=="V":
            self.quantitaButton.setText(_translate("TempGUI", "Quantità"))
            self.contenutoLabel1.setText(_translate("TempGUI", "Contenuto '"+name+"':"))
            self.contenutoLabel2.setText(_translate("TempGUI", "*****"))

    def statoValv(self, statoLabel, statoscrLabel, name, quit_event):    #funzione thread stato valvola
        import time as f
        import socket
        cod=userText+","+passwdText+",8,"+name
        while not quit_event.is_set():
            try:
                client8=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client8.connect(("192.168.0.3",8282)) #!!!!!!
                client8.send(cod.encode())
                risp=client8.recv(1024).decode()
                client8.close()
                if risp=="on":
                    self.statoLabel.setText("<html><head/><body><p><img src=\"green.png\"/></p></body></html>")
                elif risp=="off":
                    self.statoLabel.setText("<html><head/><body><p><img src=\"gray.png\"/></p></body></html>")
                elif risp=="avaria":
                    self.statoLabel.setText("<html><head/><body><p><img src=\"red.png\"/></p></body></html>")
                elif risp=="disinserita":
                    self.statoLabel.setText("<html><head/><body><p><img src=\"white.png\"/></p></body></html>")
                self.statoscrLabel.setText(risp)
            except RuntimeError:
                pass
            except Exception as e:
                print(e)
                self.statoscrLabel.setText("*****")
                client8.close()

    def tempRich(self, tempAttLabel1, name, quit_event):                 #funzione thread temperatura b/l
        import time as b
        import socket
        cod=userText+","+passwdText+",2,"+name
        while not quit_event.is_set():
            try:
                client2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client2.connect(("192.168.0.3",8282)) #!!!!!!
                client2.send(cod.encode())
                risp=client2.recv(1024).decode()
                self.tempAttLabel1.setText(str(risp))
                client2.close()
            except RuntimeError:
                pass
            except:
                self.tempAttLabel1.setText("*****")
                client2.close()
        
    def contVaso(self, contenutoLabel2, name, quit_event):               #funzione thread contenuto botte
        import time as d
        import socket
        cod=userText+","+passwdText+",3,"+name
        while not quit_event.is_set():
            try:
                client3=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client3.connect(("192.168.0.3",8282)) #!!!!!!
                client3.send(cod.encode())
                risp=client3.recv(1024).decode()
                self.contenutoLabel2.setText(str(risp))
                client3.close()
            except RuntimeError:
                pass
            except Exception as e:
                self.contenutoLabel2.setText("*****")
                print(e)
                client3.close()

    def setDef(self, tempSpin, name):                               #funzione set default value spinbox
        import socket
        cod=userText+","+passwdText+",4,"+name
        try:
            client4=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client4.connect(("192.168.0.3",8282)) #!!!!!!
            client4.send(cod.encode())
            risp=client4.recv(1024).decode()
            self.tempSpin.setValue(float(risp))
            client4.close()
        except RuntimeError:
            pass
        except:
            self.tempSpin.setValue(float(risp))
            client4.close()
    
    def setTemp(self, tempSpin, name, confermaLabel):               #funzione set value spinbox
        import socket
        valore=self.tempSpin.value()
        cod=userText+","+passwdText+",5,"+name+","+str(valore)
        try:
            client5=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client5.connect(("192.168.0.3",8282)) #!!!!!!
            client5.send(cod.encode())
            risp=client5.recv(1024).decode()
            self.confermaLabel.setText(str(risp))
            from threading import Thread
            mexconf=Thread(target=self.mexconf, args=[self.confermaLabel], daemon=True)
            mexconf.start()
            client5.close()
            self.setDef(tempSpin, name)
        except RuntimeError:
            pass
        except:
            self.confermaLabel.setText("errore aggiornamento")
            client5.close()
            self.setDef(tempSpin, name)

    def mexconf(self, confermaLabel):                               #funzione thread messaggio conferma
        import time as e
        e.sleep(10)
        self.confermaLabel.setText("")

    def graficoTemp(self, name):                                    #funzione grafico temperature
        cod=userText+","+passwdText+",6,"+name
        try:
            import socket
            import matplotlib.pyplot as plt
            import matplotlib.dates as dt
            import dateutil
            client6=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client6.connect(("192.168.0.3",8282)) #!!!!!!
            client6.send(cod.encode())
            risp=client6.recv(1024).decode()
            client6.close()
            dati=risp.split(";")
            misure=dati[0].split(",")
            quando=dati[1].split(",")
            misure=[float(valore) for valore in misure]
            y=misure[::-1]
            quando=quando[::-1]
            x=[dateutil.parser.parse(q) for q in quando]
            xfmt=dt.DateFormatter("%d/%m/%y %H:%M:%S")
            fig, ax = plt.subplots()
            ax.set_title("Storico temperature "+name)
            ax.set_xlabel("Data misurazione")
            ax.set_ylabel("Temperatura (°C)")
            ax.plot_date(x,y,"bo--", linewidth=2, markersize=6)
            ax.xaxis.set_major_formatter(xfmt)
            plt.gcf().autofmt_xdate()
            plt.grid(True)
            plt.yticks(y)
            plt.xticks(x)
            plt.gcf().canvas.set_window_title("Grafico "+name)
            plt.show()   
        except RuntimeError:
            pass
        except Exception as e:
            print(e)
            self.confermaLabel.setText("errore generazione grafico")
            client6.close()

    def graficoQuant(self, name):                                   #funzione grafico volumi
        cod=userText+","+passwdText+",7,"+name
        try:
            import socket
            import matplotlib.pyplot as plt
            import matplotlib.dates as dt
            import dateutil
            client7=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client7.connect(("192.168.0.3",8282)) #!!!!!!
            client7.send(cod.encode())
            risp=client7.recv(1024).decode()
            client7.close()
            dati=risp.split(";")
            misure=dati[0].split(",")
            quando=dati[1].split(",")
            misure=[float(valore) for valore in misure]
            y=misure[::-1]
            quando=quando[::-1]
            x=[dateutil.parser.parse(q) for q in quando]
            xfmt=dt.DateFormatter("%d/%m/%y %H:%M:%S")
            fig, ax = plt.subplots()
            ax.set_title("Storico volumi "+name)
            ax.set_xlabel("Data misurazione")
            ax.set_ylabel("Volume (L)")
            ax.plot_date(x,y,"bo--", linewidth=2, markersize=6)
            ax.xaxis.set_major_formatter(xfmt)
            plt.gcf().autofmt_xdate()
            plt.grid(True)
            plt.yticks(y)
            plt.xticks(x)
            plt.gcf().canvas.set_window_title("Grafico "+name)
            plt.show()
        except RuntimeError:
            pass
        except Exception as e:
            print(e)
            self.confermaLabel.setText("errore generazione grafico")
            client7.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainGUI()
    sys.exit(app.exec_())

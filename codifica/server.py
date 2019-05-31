from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_ServerGUI, self).__init__()
        self.setupUi(self)
        self.showMaximized()

    def closeEvent(self, event):
        try:
            threadMainPace=False
            app.closeAllWindows()
        except:
            pass

    def setupUi(self, Server):
        from threading import Thread
        threadMainPace=True
        listaLabel=[]
        Server.setObjectName("Server")
        Server.resize(564, 265)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2_icon38Server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Server.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statoServerLabel = QtWidgets.QLabel(self.centralwidget)
        self.statoServerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statoServerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statoServerLabel.setObjectName("statoServerLabel")
        self.horizontalLayout.addWidget(self.statoServerLabel)
        self.statoLabel = QtWidgets.QLabel(self.centralwidget)
        self.statoLabel.setObjectName("statoLabel")
        self.horizontalLayout.addWidget(self.statoLabel)
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.imgLabel.setObjectName("imgLabel")
        self.horizontalLayout.addWidget(self.imgLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setGeometry(QtCore.QRect(0, 0, 529, 472))
        self.scrollContent.setObjectName("scrollContent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollContent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label0 = QtWidgets.QLabel(self.scrollContent)
        self.label0.setObjectName("label0")
        self.gridLayout_2.addWidget(self.label0, 0, 0, 1, 1)
        listaLabel.append(self.label0)
        self.label1 = QtWidgets.QLabel(self.scrollContent)
        self.label1.setObjectName("label1")
        self.gridLayout_2.addWidget(self.label1, 1, 0, 1, 1)
        listaLabel.append(self.label1)
        self.label2 = QtWidgets.QLabel(self.scrollContent)
        self.label2.setObjectName("label2")
        self.gridLayout_2.addWidget(self.label2, 2, 0, 1, 1)
        listaLabel.append(self.label2)
        self.label3 = QtWidgets.QLabel(self.scrollContent)
        self.label3.setObjectName("label3")
        self.gridLayout_2.addWidget(self.label3, 3, 0, 1, 1)
        listaLabel.append(self.label3)
        self.label4 = QtWidgets.QLabel(self.scrollContent)
        self.label4.setObjectName("label4")
        self.gridLayout_2.addWidget(self.label4, 4, 0, 1, 1)
        listaLabel.append(self.label4)
        self.label5 = QtWidgets.QLabel(self.scrollContent)
        self.label5.setObjectName("label5")
        self.gridLayout_2.addWidget(self.label5, 5, 0, 1, 1)
        listaLabel.append(self.label5)
        self.label6 = QtWidgets.QLabel(self.scrollContent)
        self.label6.setObjectName("label6")
        self.gridLayout_2.addWidget(self.label6, 6, 0, 1, 1)
        listaLabel.append(self.label6)
        self.label7 = QtWidgets.QLabel(self.scrollContent)
        self.label7.setObjectName("label7")
        self.gridLayout_2.addWidget(self.label7, 7, 0, 1, 1)
        listaLabel.append(self.label7)
        self.label8 = QtWidgets.QLabel(self.scrollContent)
        self.label8.setObjectName("label8")
        self.gridLayout_2.addWidget(self.label8, 8, 0, 1, 1)
        listaLabel.append(self.label8)
        self.label9 = QtWidgets.QLabel(self.scrollContent)
        self.label9.setObjectName("label9")
        self.gridLayout_2.addWidget(self.label9, 9, 0, 1, 1)
        listaLabel.append(self.label9)
        self.label10 = QtWidgets.QLabel(self.scrollContent)
        self.label10.setObjectName("label10")
        self.gridLayout_2.addWidget(self.label10, 10, 0, 1, 1)
        listaLabel.append(self.label10)
        self.label11 = QtWidgets.QLabel(self.scrollContent)
        self.label11.setObjectName("label11")
        self.gridLayout_2.addWidget(self.label11, 11, 0, 1, 1)
        listaLabel.append(self.label11)
        self.label12 = QtWidgets.QLabel(self.scrollContent)
        self.label12.setObjectName("label12")
        self.gridLayout_2.addWidget(self.label12, 12, 0, 1, 1)
        listaLabel.append(self.label12)
        self.label13 = QtWidgets.QLabel(self.scrollContent)
        self.label13.setObjectName("label13")
        self.gridLayout_2.addWidget(self.label13, 13, 0, 1, 1)
        listaLabel.append(self.label13)
        self.label14 = QtWidgets.QLabel(self.scrollContent)
        self.label14.setObjectName("label14")
        self.gridLayout_2.addWidget(self.label14, 14, 0, 1, 1)
        listaLabel.append(self.label14)
        self.label15 = QtWidgets.QLabel(self.scrollContent)
        self.label15.setObjectName("label15")
        self.gridLayout_2.addWidget(self.label15, 15, 0, 1, 1)
        listaLabel.append(self.label15)
        self.label16 = QtWidgets.QLabel(self.scrollContent)
        self.label16.setObjectName("label16")
        self.gridLayout_2.addWidget(self.label16, 16, 0, 1, 1)
        listaLabel.append(self.label16)
        self.label17 = QtWidgets.QLabel(self.scrollContent)
        self.label17.setObjectName("label17")
        self.gridLayout_2.addWidget(self.label17, 17, 0, 1, 1)
        listaLabel.append(self.label17)
        self.label18 = QtWidgets.QLabel(self.scrollContent)
        self.label18.setObjectName("label18")
        self.gridLayout_2.addWidget(self.label18, 18, 0, 1, 1)
        listaLabel.append(self.label18)
        self.label19 = QtWidgets.QLabel(self.scrollContent)
        self.label19.setObjectName("label19")
        self.gridLayout_2.addWidget(self.label19, 20, 0, 1, 1)
        listaLabel.append(self.label19)
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        Server.setCentralWidget(self.centralwidget)
        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)
        be=Thread(target=self.backend, args=[lambda: threadMainPace, listaLabel], daemon=True)
        be.start()

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "Server"))
        self.statoServerLabel.setText(_translate("Server", "Stato server:"))
        self.statoLabel.setText(_translate("Server", "***"))
        self.imgLabel.setText(_translate("Server", "<html><head/><body><p><img src=\"gray.png\"/></p></body></html>"))

    def backend(self, exit, listaLabel):
        from threading import Thread
        import socket
        import mysql.connector as mys
        global ind
        ind=1
        global listaDati
        listaDati=[]
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("192.168.5.212", 8282)) #indirizzo macchina
        s.listen(10)
        while exit():
            try:
                connClient, ipClient = s.accept()
                cred=connClient.recv(1024).decode() #0 username, 1 password, 2 codIstruzione, 3&&+ info aggiuntive
                cod=cred.split(",")
                arrDati=cod
                if int(cod[2])==0:      #login
                    print(cod)
                    try:
                        mydb0=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Login")  #credenziali mysql
                        myc0=mydb0.cursor()
                        myc0.execute("select username,password from Utente where username='"+str(cod[0])+"' and password='"+str(cod[1])+"'")
                        record=myc0.fetchone()
                        if record[0]==str(cod[0]) and record[1]==str(cod[1]):
                            connClient.send("accesso_corretto".encode())
                        else:
                            connClient.send("credenziali_errate".encode())
                        mydb0.close()
                    except Exception as e:
                        print(e)
                        connClient.send("credenziali_errate".encode())
                        mydb0.close()
                elif int(cod[2])==1:    #temperatura esterna
                    print(cod)
                    try:
                        mydb1=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Esterno")   #credenziali mysql
                        myc1=mydb1.cursor()
                        myc1.execute("select tempEsterno from Esterno where idEsterno=1")
                        record=myc1.fetchone()
                        connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb1.close()
                    except:
                        connClient.send("*****".encode())
                        mydb1.close()
                elif int(cod[2])==2:    #temperature botti e locali e controllo sonda
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb2=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc2=mydb2.cursor()
                        if cod[0]=="Vaso":
                            myc2.execute("select statoS from Sonda where idBotte="+str(cod[2]))
                            attivo=myc2.fetchone()
                        else:
                            myc2.execute("select statoS from Sonda where idLocale="+str(cod[1]))
                            attivo=myc2.fetchone()
                        if attivo[0]==1:
                            if cod[0]=="Vaso":
                                myc2.execute("select tempBotte from Botte where idBotte="+str(cod[2]))
                                record=myc2.fetchone()
                                connClient.send(str(record[0]).encode())
                            else:
                                myc2.execute("select tempLocale from Locale where idLocale="+str(cod[1]))
                                record=myc2.fetchone()
                                connClient.send(str(record[0]).encode())
                        else:
                            connClient.send("**sonda disinserita**".encode())
                    except BrokenPipeError:
                        mydb2.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb2.close()
                elif int(cod[2])==3:    #contenuto
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb3=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc3=mydb3.cursor()
                        myc3.execute("select contenuto from Botte where idBotte="+str(cod[2]))
                        record=myc3.fetchone()
                        connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb3.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb3.close()
                elif int(cod[2])==4:    #reset spin
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb4=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc4=mydb4.cursor()
                            myc4.execute("select tempsetBotte from Botte where idBotte="+str(cod[2]))
                            record=myc4.fetchone()
                            connClient.send(str(record[0]).encode())
                        else:
                            mydb4=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc4=mydb4.cursor()
                            myc4.execute("select tempsetLocale from Locale where idLocale="+str(cod[1]))
                            record=myc4.fetchone()
                            connClient.send(str(record[0]).encode())
                    except BrokenPipeError:
                        mydb4.close()
                    except Exception as e:
                        print(e)
                        connClient.send("16.0".encode())
                        mydb4.close()
                elif int(cod[2])==5:    #conferma spin
                    print(cod)
                    valore=cod[4]
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idBotte,contenuto,tempBotte,tempsetBotte,volume from Botte where idBotte="+str(cod[2]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoBotte(dataAggB,contenutoAggB,tempAggB,tempsetAggB,volumeAggB,idBotte,flagContenuto,flagTemperatura,flagTemperaturaSet,flagVolume)values(now(),'"+str(record[1])+"',"+str(record[2])+","+str(record[3])+","+str(record[4])+","+str(record[0])+",0,0,1,0)")
                            myc5.execute("update Botte set tempsetBotte="+str(valore)+" where idBotte="+str(cod[2]))
                            mydb5.commit()
                        else:
                            mydb5=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc5=mydb5.cursor()
                            myc5.execute("select idLocale,tempLocale,tempsetLocale from Locale where idLocale="+str(cod[1]))
                            record=myc5.fetchone()
                            myc5.execute("insert into StoricoLocale(dataAggL,tempAggL,tempsetAggL,idLocale,flagTemperatura,flagTemperaturaSet)values(now(),"+str(record[1])+","+str(record[2])+","+str(record[0])+",0,1)")
                            myc5.execute("update Locale set tempsetLocale="+str(valore)+" where idLocale="+str(cod[1]))
                            mydb5.commit()
                        connClient.send("temperatura aggiornata".encode())
                    except BrokenPipeError:
                        mydb5.close()
                    except Exception as e:
                        print(e)
                        mydb5.rollback()
                        connClient.send("errore aggiornamento".encode())
                        mydb5.close()
                elif int(cod[2])==6:    #grafico monitoraggio temperature
                    print(cod)
                    misure=""
                    quando=""
                    dati=""
                    cod=str(cod[3]).split(" ")
                    try:
                        if cod[0]=="Vaso":
                            mydb6=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc6=mydb6.cursor()
                            myc6.execute("select tempAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordTemp=myc6.fetchall()
                            myc6.execute("select dataAggB from StoricoBotte where idBotte="+str(cod[2])+" order by dataAggB desc limit 10")
                            recordDate=myc6.fetchall()
                        else:
                            mydb6=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                            myc6=mydb6.cursor()
                            myc6.execute("select tempAggL from StoricoLocale where idLocale="+str(cod[1])+" order by dataAggL desc limit 10")
                            recordTemp=myc6.fetchall()
                            myc6.execute("select dataAggL from StoricoLocale where idLocale="+str(cod[1])+" order by dataAggL desc limit 10")
                            recordDate=myc6.fetchall()
                        c=0
                        for i in recordTemp:
                            try:
                                misure=misure+str(i[0])
                                c+=1
                                if c<len(recordTemp):
                                    misure=misure+","
                            except:
                                c+=1
                                pass
                        c=0
                        for i in recordDate:
                            try:
                                quando=quando+str(i[0])
                                c+=1
                                if c<len(recordDate):
                                    quando=quando+","
                            except:
                                c+=1
                                pass
                        dati=misure+";"+quando
                        connClient.send(dati.encode())
                    except BrokenPipeError:
                        mydb6.close()
                    except Exception as e:
                        print(e)
                        connClient.send("errore invio dati".encode())
                        mydb6.close()
                elif int(cod[2])==7:    #grafico monitoraggio quantità
                    print(cod)
                    misure=""
                    quando=""
                    dati=""
                    c=0
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb7=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc7=mydb7.cursor()
                        myc7.execute("select volumeAggB from StoricoBotte where idBotte="+str(cod[2])+" and flagVolume=1 order by dataAggB desc limit 10")
                        recordQuant=myc7.fetchall()
                        myc7.execute("select dataAggB from StoricoBotte where idBotte="+str(cod[2])+" and flagVolume=1 order by dataAggB desc limit 10")
                        recordDate=myc7.fetchall()
                        for i in recordQuant:
                            try:
                                misure=misure+str(i[0])
                                c+=1
                                if c<len(recordQuant):
                                    misure=misure+","
                            except:
                                c+=1
                                pass
                        c=0
                        for i in recordDate:
                            try:
                                quando=quando+str(i[0])
                                c+=1
                                if c<len(recordDate):
                                    quando=quando+","
                            except:
                                c+=1
                                pass
                        dati=misure+";"+quando
                        connClient.send(dati.encode())
                    except BrokenPipeError:
                        mydb7.close()
                    except Exception as e:
                        print(e)
                        connClient.send("errore invio dati".encode())
                        mydb7.close()
                elif int(cod[2])==8:    #controllo avarie valvole
                    print(cod)
                    cod=str(cod[3]).split(" ")
                    try:
                        mydb8=mys.connect(host="192.168.5.33", user="root", passwd="quinta", database="Cantina") #credenziali mysql
                        myc8=mydb8.cursor()
                        if cod[0]=="Vaso":
                            myc8.execute("select statoV, funzV from Sonda,Botte where Sonda.idSondaV=Botte.idSondaV and Sonda.idBotte="+str(cod[2]))
                        else:
                            myc8.execute("select statoV, funzV from Sonda,Locale where Sonda.idSondaV=Locale.idSondaV and Sonda.idLocale="+str(cod[1]))
                        record=myc8.fetchone()
                        if record[0]==0 and record[1]==0:
                            connClient.send("disinserita".encode())
                        elif record[0]==0 and record[1]==1:
                            connClient.send("avaria".encode())
                        elif record[0]==1 and record[1]==0:
                            connClient.send("off".encode())
                        elif record[0]==1 and record[1]==1:
                            connClient.send("on".encode())
                    except BrokenPipeError:
                        mydb8.close()
                    except Exception as e:
                        print(e)
                        connClient.send("*****".encode())
                        mydb8.close()
                aggLabel=Thread(target=self.aggScroll, args=[listaDati, listaLabel, arrDati])
                aggLabel.start()
            except KeyboardInterrupt:
                s.close()
                print("server chiuso")
                break
            except Exception as e:
                print(e) ### debug
                pass

    def aggScroll(self, listaDati, listaLabel, cod):
        try:
            global ind
            print(ind) ### debug
            import datetime
            ora=datetime.datetime.now()
            if ind>=19:
                listaDati.pop(0)
                print(listaDati) ### debug
                ind-=1
            istr=ora.strftime("%d-%m-%y")+" "+ora.strftime("%H-%M-%S")+" > "    #costruisco la stringa da appendere
            for el in cod:
                istr += " | "+str(el)
            listaDati.append(istr)                                                #appendo la stringa
            QtWidgets.QLabel(self.scrollContent)
            # for c in range(len(listaDati)):                                     #setto testo nelle label
            #     listaLabel[c].setText(listaDati[c])
            ind+=1
        except Exception as e:
            print(e)   ### debug
            pass

    ### Lazza thing
    def hello(self, content):
        QtWidgets.QLabel(self.scrollContent).setText(content)
        """ RESTART FROM HERE """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_ServerGUI()
    sys.exit(app.exec_())

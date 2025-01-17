from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication

from fornitore.view.VistaFornitore import VistaFornitore
from listafornitori.controller.ControllerListaFornitori import ControllerListaFornitori
from listafornitori.view.VistaInserisciFornitore import VistaInserisciFornitore

class VistaListaFornitori(QWidget):
    def __init__(self):
        super(VistaListaFornitori, self).__init__()

        self.controller = ControllerListaFornitori()
        # boolean: mi permettono di verificare se sto visualizzando in lista fornitori standard o premium
        self.standard= False
        self.premium= False
        self.lista_fornitori = self.controller.get_lista_fornitori()

        # Lista: E' una copia della lista reale. Mi permette di manipolare i suoi elementi senza modificare la lista originale (lista di riferimento)
        self.lista_dinamica = self.lista_fornitori[:]

        ############################

        ''' 
            Costruzione parte statica dell'interfaccia
        '''
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        #Come prendere le dimensioni dello schermo
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        self.setObjectName("Form")
        self.resize(1121, 576)
        self.setStyleSheet("background-color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_apri = QtWidgets.QPushButton(self)
        self.pushButton_apri.setObjectName("pushButton_apri")
        self.pushButton_apri.clicked.connect(self.show_fornitore)
        self.verticalLayout_2.addWidget(self.pushButton_apri)
        self.pushButton_apri.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.pushButton_nuovo = QtWidgets.QPushButton(self)
        self.pushButton_nuovo.setObjectName("pushButton_nuovo")
        self.pushButton_nuovo.clicked.connect(self.show_inserisci_fornitore)
        self.verticalLayout_2.addWidget(self.pushButton_nuovo)
        self.pushButton_nuovo.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.lineEdit_cerca = QtWidgets.QLineEdit(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_cerca.sizePolicy().hasHeightForWidth())
        self.lineEdit_cerca.setSizePolicy(sizePolicy)
        self.lineEdit_cerca.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_cerca.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_cerca.setFont(font)
        self.lineEdit_cerca.setClearButtonEnabled(False)
        self.lineEdit_cerca.setObjectName("lineEdit_cerca")
        self.lineEdit_cerca.setPlaceholderText("Cerca per codice")
        self.lineEdit_cerca.returnPressed.connect(self.filter_cerca)
        self.gridLayout.addWidget(self.lineEdit_cerca, 2, 6, 1, 1)
        self.lineEdit_cerca.setStyleSheet("QLineEdit {\n"
                                 "   border-width: 2px;\n"
                                 "   border-radius: 10px;\n"
                                 "   border: 2px solid gray;\n"
                                 "   font: 12px;\n"
                                 "   padding: 6px;\n"
                                 "}")
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setMinimumSize(QtCore.QSize(200, 0))
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        pixmap = QPixmap('listaprodotti/data/images/logo_mini2.png')
        self.label_logo.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_logo, 1, 4, 3, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 3, 1)
        self.pushButton_indietro = QtWidgets.QPushButton(self)
        self.pushButton_indietro.setObjectName("pushButton_indietro")
        self.pushButton_indietro.clicked.connect(self.close)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listaprodotti/data/images/logo_home.png'))
        self.pushButton_indietro.setIcon(icon)
        self.pushButton_indietro.setIconSize(QSize(50, 50))
        self.gridLayout.addWidget(self.pushButton_indietro, 1, 1, 1, 1)
        self.pushButton_indietro.setStyleSheet("QPushButton {\n"
                                    "   background-color:white;\n"
                                    "   border-width: 2px;\n"
                                    "   border-radius: 10px;\n"
                                    "   padding: 6px;\n"
                                    "}")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 7, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(0, self.width/8)
        self.tableWidget.setColumnWidth(1, self.width/7.05)
        self.tableWidget.setColumnWidth(2, self.width/7.05)
        self.tableWidget.setColumnWidth(3, self.width/7.05)
        self.tableWidget.setColumnWidth(4, self.width/7.05)
        self.tableWidget.setColumnWidth(5, self.width/7.05)
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 6)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 7)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.pushButton_stato1 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        self.pushButton_stato1.setFont(font)
        self.pushButton_stato1.setObjectName("pushButton_stato1")
        self.pushButton_stato1.clicked.connect(self.filter_standard)
        self.gridLayout_3.addWidget(self.pushButton_stato1, 0, 1, 1, 1)
        self.pushButton_stato1.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""min-width: 80px;\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 2, 1, 1)
        self.pushButton_stato2 = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_stato2.setFont(font)
        self.pushButton_stato2.setObjectName("pushButton_stato2")
        self.pushButton_stato2.clicked.connect(self.filter_premium)
        self.gridLayout_3.addWidget(self.pushButton_stato2, 0, 3, 1, 1)
        self.pushButton_stato2.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""min-width: 80px;\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 4, 1, 1)
        self.pushButton_all = QtWidgets.QPushButton(self)
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_all.clicked.connect(self.filter_all)
        self.gridLayout_3.addWidget(self.pushButton_all, 0, 5, 1, 1)
        self.pushButton_all.setStyleSheet("QPushButton {\n""   background-color: rgb(26, 108, 218);\n""min-width: 80px;\n""   border-width: 2px;\n""   border-radius: 10px;\n""   font: bold 12px;\n""   padding: 6px;\n""   color: white;\n""}")
        self.gridLayout.addLayout(self.gridLayout_3, 3, 1, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 7)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 5, 3, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        # chiamo la parte dinamica dell'interfaccia
        self.retranslateUi()
        self.setWindowTitle("Area fornitori")

    '''
        Costruzione parte dinamica dell'interfaccia  
    '''
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #imposto il testo degli oggetti dell'interfaccia
        self.pushButton_apri.setText(_translate("Form", "Apri"))
        self.pushButton_nuovo.setText(_translate("Form", "Nuovo"))
        self.pushButton_stato1.setText(_translate("Form", "Standard"))
        self.pushButton_stato2.setText(_translate("Form", "Premium"))
        self.pushButton_all.setText(_translate("Form", "All"))

        #imposto le colonne della tabella
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codice"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stato"))
        item = self.tableWidget.horizontalHeaderItem(3)
      #  item.setText(_translate("Form", "Rappresentante"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Telefono"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Indirizzo"))

        # inserisco gli elementi in tabella
        row = 0
        self.tableWidget.setColumnCount(6)
        # chiamo il filtro generale prima di visualizzare gli elementi in tabella
        if self.standard or self.premium:
            self.filter()
        self.tableWidget.setRowCount(len(self.lista_dinamica))
        for fornitore in self.lista_dinamica:
            item = QTableWidgetItem(str(fornitore.cod_fornitore))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(fornitore.nome))
            if fornitore.stato == "P":
                stato = "Premium"
            else:
                stato = "Standard"
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(stato))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(fornitore.rappresentante))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(fornitore.telefono)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(fornitore.indirizzo))

            row = row + 1

    def show_inserisci_fornitore(self):
        self.vista_inserisci_fornitore= VistaInserisciFornitore(self.controller, self.retranslateUi, self.lista_dinamica)
        self.vista_inserisci_fornitore.show()

    def show_fornitore(self):
        #len ritorna il numero di elementi, sarebbe il length di java
        if(len(self.tableWidget.selectedIndexes()) > 0):
            selected = self.tableWidget.selectedIndexes()[0].row()
            fornitore_selezionato = self.lista_dinamica[selected]
            self.vista_fornitore = VistaFornitore(fornitore_selezionato, self.retranslateUi, self.controller, self.lista_dinamica)
            self.vista_fornitore.show()

    # Metodo: indica al filtro generale filter() che vogliamo filtrare fornitori premium
    def filter_premium(self):
        self.premium = True
        self.standard = False
        self.lista_fornitori = self.controller.get_lista_fornitori()
        self.lista_dinamica = self.lista_fornitori[:]
        self.filter()
        self.retranslateUi()

    # Metodo: indica al filtro generale filter() che vogliamo filtrare fornitori standard
    def filter_standard(self):
        self.premium= False
        self.standard= True
        self.lista_fornitori = self.controller.get_lista_fornitori()
        self.lista_dinamica = self.lista_fornitori[:]
        self.filter()
        self.retranslateUi()

    # Metodo: indica al filtro generale filter() che vogliamo visualizzare tutti i fornitori
    def filter_all(self):
        self.standard= False
        self.premium= False
        self.lista_fornitori = self.controller.get_lista_fornitori()
        self.lista_dinamica = self.lista_fornitori[:]
        self.filter()
        self.retranslateUi()

    # Metodo: filtra i fornitori con cod_fornitore contenente il testo immesso
    def filter_cerca(self):
        self.lista_fornitori = self.controller.get_lista_fornitori()
        self.lista_dinamica = self.lista_fornitori[:]
        codice_cerca = self.lineEdit_cerca.text()
        codice_cerca= codice_cerca.upper()
        elementi_da_rimuovere = []
        for fornitore in self.lista_dinamica:
            cod_fornitore= str(fornitore.cod_fornitore)
            cod_fornitore= cod_fornitore.upper()
            if not (codice_cerca in cod_fornitore):
                elementi_da_rimuovere.append(fornitore)
        for fornitore in elementi_da_rimuovere:
            if fornitore in self.lista_dinamica:
                self.lista_dinamica.remove(fornitore)
        self.retranslateUi()

    # Metodo: filtro generale, svolge più filtraggi
    def filter(self):
        elementi_da_rimuovere = []

        if self.standard:
            for fornitore in self.lista_dinamica:
                if str(fornitore.stato) != "S":
                    elementi_da_rimuovere.append(fornitore)
            for fornitore in elementi_da_rimuovere:
                if fornitore in self.lista_dinamica:
                    self.lista_dinamica.remove(fornitore)
            return

        if self.premium:
            for fornitore in self.lista_dinamica:
                if str(fornitore.stato)!= "P":
                    elementi_da_rimuovere.append(fornitore)
            for fornitore in elementi_da_rimuovere:
                if fornitore in self.lista_dinamica:
                    self.lista_dinamica.remove(fornitore)
            return
        else:
            self.lista_fornitori= self.controller.get_lista_fornitori()
            self.lista_dinamica= self.lista_fornitori[:]
            return

    def closeEvent(self, event):
        self.controller.save_data()
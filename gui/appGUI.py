# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 500)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        MainWindow.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow.setMaximumSize(QtCore.QSize(300, 800))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.appLayout = QtWidgets.QVBoxLayout()
        self.appLayout.setObjectName("appLayout")
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.searchLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton.setObjectName("pushButton")
        self.searchLayout.addWidget(self.pushButton)
        self.appLayout.addLayout(self.searchLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.appLayout.addItem(spacerItem)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTr = QtWidgets.QWidget()
        self.tabTr.setObjectName("tabTr")
        self.trengLayout = QtWidgets.QVBoxLayout(self.tabTr)
        self.trengLayout.setContentsMargins(0, 0, 0, 0)
        self.trengLayout.setObjectName("trengLayout")
        self.trFrame = QtWidgets.QFrame(self.tabTr)
        self.trFrame.setStyleSheet("border:0px;")
        self.trFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trFrame.setLineWidth(0)
        self.trFrame.setObjectName("trFrame")
        self.trLayout = QtWidgets.QVBoxLayout(self.trFrame)
        self.trLayout.setContentsMargins(0, 0, 0, 0)
        self.trLayout.setObjectName("trLayout")

        self.trengLayout.addWidget(self.trFrame)
        self.tabWidget.addTab(self.tabTr, "")
        self.tabCamb = QtWidgets.QWidget()
        self.tabCamb.setObjectName("tabCamb")
        self.cambLayout = QtWidgets.QVBoxLayout(self.tabCamb)
        self.cambLayout.setContentsMargins(0, 0, 0, 0)
        self.cambLayout.setObjectName("cambLayout")
        self.cmFrame = QtWidgets.QFrame(self.tabCamb)
        self.cmFrame.setStyleSheet("border:1px;")
        self.cmFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cmFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cmFrame.setLineWidth(0)
        self.cmFrame.setObjectName("cmFrame")
        self.cmLayout = QtWidgets.QVBoxLayout(self.cmFrame)
        self.cmLayout.setContentsMargins(0, 0, 0, 0)
        self.cmLayout.setSpacing(6)
        self.cmLayout.setObjectName("cmLayout")

        self.cambLayout.addWidget(self.cmFrame)
        self.tabWidget.addTab(self.tabCamb, "")
        self.appLayout.addWidget(self.tabWidget)
        self.mainLayout.addLayout(self.appLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.menubar.setMinimumSize(QtCore.QSize(0, 30))
        self.menubar.setStyleSheet("border:0px; padding-top:4px")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAlways_On_Top = QtWidgets.QAction(MainWindow)
        self.actionAlways_On_Top.setCheckable(True)
        self.actionAlways_On_Top.setObjectName("actionAlways_On_Top")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setCheckable(True)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(True)
        self.actionDark.setObjectName("actionDark")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAlways_On_Top)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionLight)
        self.menuView.addAction(self.actionDark)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionAlways_On_Top.setDisabled(True)
        self.actionLight.setDisabled(True)
        self.actionDark.setDisabled(True)

        self.tabChanger = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Tab'),self)
        self.tabChanger.activated.connect(self.changeTab)
        
        self.tabWidget.setCurrentIndex(1)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(self.showDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTr), _translate("MainWindow", "TURENG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCamb), _translate("MainWindow", "Cambridge"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAlways_On_Top.setText(_translate("MainWindow", "Always On Top"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def changeTab(self):
        current = self.tabWidget.currentIndex()
        if current == 1:
            self.tabWidget.setCurrentIndex(0)
        else:
            self.tabWidget.setCurrentIndex(1)

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("""
        Turkish-English Multi Dictionary
        GitHub: ahmetveburak
        """)
        msgBox.setWindowTitle("About Me!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

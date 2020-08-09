import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.parse import urlencode

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Islamic Azad University Connect to the class")
        MainWindow.setFixedSize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #GroupBoXs
        self.G_specclass = QtWidgets.QGroupBox(self.centralwidget)
        self.G_specclass.setGeometry(QtCore.QRect(20, 10, 605, 210))
        self.G_specclass.setObjectName("G_specclass")
        self.G_linkclass = QtWidgets.QGroupBox(self.centralwidget)
        self.G_linkclass.setGeometry(QtCore.QRect(20, 370, 605, 91))
        self.G_linkclass.setObjectName("G_linkclass")
        self.G_connect = QtWidgets.QGroupBox(self.G_specclass)
        self.G_connect.setGeometry(QtCore.QRect(440, 20, 160, 180))
        self.G_connect.setObjectName("G_connect")
        self.G_tip = QtWidgets.QGroupBox(self.centralwidget)
        self.G_tip.setGeometry(QtCore.QRect(20, 225, 605, 140))
        self.G_tip.setObjectName("G_tip")
        
	#comboBoxs
        self.CB_ostad = QtWidgets.QComboBox(self.G_specclass)
        self.CB_ostad.setGeometry(QtCore.QRect(21, 30, 351, 21))
        self.CB_ostad.setObjectName("CB_ostad")
        op = ["Mr.Mojareb"] 
        for x in op:
        	self.CB_ostad.addItem(x)
        
        #labels
        self.L_ostad = QtWidgets.QLabel(self.G_specclass)
        self.L_ostad.setGeometry(QtCore.QRect(370, 24, 47, 31))
        self.L_ostad.setObjectName("L_ostad")
        self.L_fullname = QtWidgets.QLabel(self.G_specclass)
        self.L_fullname.setGeometry(QtCore.QRect(240, 60, 141, 16))
        self.L_fullname.setObjectName("L_fullname")
        self.L_studentnu = QtWidgets.QLabel(self.G_specclass)
        self.L_studentnu.setGeometry(QtCore.QRect(40, 60, 101, 20))
        self.L_studentnu.setObjectName("L_studentnu")
        self.L_errorname = QtWidgets.QLabel(self.G_specclass)
        self.L_errorname.setGeometry(QtCore.QRect(285, 110, 101, 20))
        self.L_errorname.setObjectName("L_errorname")
        self.L_errornu = QtWidgets.QLabel(self.G_specclass)
        self.L_errornu.setGeometry(QtCore.QRect(35, 110, 101, 20))
        self.L_errornu.setObjectName("L_errornu")
        self.L_tip = QtWidgets.QLabel(self.G_tip)
        self.L_tip.setGeometry(QtCore.QRect(280, 15, 300, 40))
        self.L_tip.setObjectName("L_tip")
        self.L_tip2 = QtWidgets.QLabel(self.G_tip)
        self.L_tip2.setGeometry(QtCore.QRect(280, 70, 300, 40))
        self.L_tip2.setObjectName("L_tip2")
        
	#Input
        self.input_fullname = QtWidgets.QLineEdit(self.G_specclass)
        self.input_fullname.setGeometry(QtCore.QRect(260, 90, 151, 20))
        self.input_fullname.setObjectName("input_fullname")
        self.input_fullname.setPlaceholderText("رضا رضایی")
        self.input_studentnu = QtWidgets.QLineEdit(self.G_specclass)
        self.input_studentnu.setGeometry(QtCore.QRect(20, 90, 151, 20))
        self.input_studentnu.setObjectName("input_studentnu")
        self.input_studentnu.setPlaceholderText("982154321")
        
	#RadioButton
        self.RB_adobe = QtWidgets.QRadioButton(self.G_connect)
        self.RB_adobe.setGeometry(QtCore.QRect(10, 20, 61, 17))
        self.RB_adobe.setObjectName("RB_adobe")
        self.RB_adobe.setChecked(True)
        self.RB_browser = QtWidgets.QRadioButton(self.G_connect)
        self.RB_browser.setGeometry(QtCore.QRect(90, 20, 51, 17))
        self.RB_browser.setObjectName("RB_browser")
        self.RB_browser.setChecked(False)

        #PushButton
        self.BT_link = QtWidgets.QPushButton(self.G_specclass)
        self.BT_link.setGeometry(QtCore.QRect(47, 145, 101, 23))
        self.BT_link.setObjectName("BT_link")
        self.BT_adcon = QtWidgets.QPushButton(self.G_tip)
        self.BT_adcon.setGeometry(QtCore.QRect(50, 30, 101, 23))
        self.BT_adcon.setObjectName("BT_adcon")
        self.BT_adcon.setText("Adobe Connect")
        self.BT_flash = QtWidgets.QPushButton(self.G_tip)
        self.BT_flash.setGeometry(QtCore.QRect(50, 85, 101, 23))
        self.BT_flash.setObjectName("BT_flash")
        self.BT_flash.setText("Adobe Flash")

        #TextBrowser
        self.T_link = QtWidgets.QTextBrowser(self.G_linkclass)
        self.T_link.setGeometry(QtCore.QRect(5, 19, 595, 61))
        self.T_link.setObjectName("T_link")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BT_link.clicked.connect(self.link)
        self.BT_flash.clicked.connect(self.flash)
        self.BT_adcon.clicked.connect(self.adcon)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Islamic Azad University Connect to the class"))
        self.G_specclass.setTitle(_translate("MainWindow", "Class specifications"))
        self.L_ostad.setText(_translate("MainWindow", "Professor :"))
        self.L_fullname.setText(_translate("MainWindow", "Full name :"))
        self.L_studentnu.setText(_translate("MainWindow", "Student Number :"))
        self.G_connect.setTitle(_translate("MainWindow", "Connection type"))
        self.RB_adobe.setText(_translate("MainWindow", "Software"))
        self.RB_browser.setText(_translate("MainWindow", "Browser"))
        self.BT_link.setText(_translate("MainWindow", "Get the link"))
        self.G_linkclass.setTitle(_translate("MainWindow", "Class link"))
        self.G_tip.setTitle(_translate("MainWindow", "Tip"))
        self.L_tip.setText(_translate("MainWindow", "In software mode, you must install the Adobe Connect application.\n\nIf you do not have the application, click the Adobe Connect button."))
        self.L_tip2.setText(_translate("MainWindow", "In browser mode you must install Adobe Flash Player.\n\nIf you do not have the program, click the Adobe Flash button."))
        
    def flash(self):
    	webbrowser.open("https://soft98.ir/software/flash-tools/29-adobe-flash-player.html")

    def adcon(self):
    	webbrowser.open("https://dl2.soft98.ir/adobe/Adobe.Connect.Client.2020.1.5.3.zip?1596809939")


    def link(self):
    	ostad = str(self.CB_ostad.currentText())
    	fullname = str(self.input_fullname.text())
    	studentnu = str(self.input_studentnu.text())
    	con = self.RB_browser.isChecked()
    	if fullname == "":
    		self.L_errorname.setText("Enter your name !!")
    	if studentnu == "":
    		self.L_errornu.setText("Enter correctly !!")
    	
    	i = urlencode({
    			'guestName':f"{studentnu}-{fullname}",
    			'launcher': 'true',
    			'html-view': 'false',
    			'proto': 'true'
    		})
    	if con == True :
    		i = urlencode({
    			'guestName':f"{studentnu}-{fullname}",
    			'launcher': 'false',
    			'html-view': 'true',
    			'proto': 'flase'
    		})

    	masters_link = {
    	'Mr.Mojareb': f"http://class.iauq.ac.ir/C40020?{i}",
    	}
    	if ostad in masters_link:
    		send = masters_link[ostad]
    		self.T_link.setHtml(f"{send}")
    		webbrowser.open(f"{send}")

def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
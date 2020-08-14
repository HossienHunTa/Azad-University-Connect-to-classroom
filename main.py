import os
import sys
import webbrowser
import base64
import re
from collections import ChainMap
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlencode
from PyQt5 import QtCore, QtGui, QtWidgets

def get_captcha(driver, img, captcha_number):
    img_captcha_base64 = driver.execute_async_script(
        """
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
        ele.removeEventListener('load', fn, false);
        var cnv = document.createElement('canvas');
        cnv.width = this.width; cnv.height = this.height;
        cnv.getContext('2d').drawImage(this, 0, 0);
        callback(cnv.toDataURL('image/png').substring(22));
        }, false); ele.dispatchEvent(new Event('load'));
        """, img
    )
    with open(r"captcha.png", 'wb') as f:
        f.write(base64.b64decode(img_captcha_base64))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(660, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FxHome.Ir_daneshgah-azad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.G_Login = QtWidgets.QGroupBox(self.centralwidget)
        self.G_Login.setGeometry(QtCore.QRect(10, 10, 171, 191))
        self.G_Login.setObjectName("G_Login")
        self.inputstudentnu = QtWidgets.QLineEdit(self.G_Login)
        self.inputstudentnu.setGeometry(QtCore.QRect(10, 30, 150, 20))
        self.inputstudentnu.setAlignment(QtCore.Qt.AlignCenter)
        self.inputstudentnu.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputstudentnu.setObjectName("inputstudentnu")
        self.inputpassword = QtWidgets.QLineEdit(self.G_Login)
        self.inputpassword.setGeometry(QtCore.QRect(10, 70, 150, 20))
        self.inputpassword.setText("")
        self.inputpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.inputpassword.setObjectName("inputpassword")
        self.btlogin = QtWidgets.QPushButton(self.G_Login)
        self.btlogin.setGeometry(QtCore.QRect(10, 150, 150, 23))
        self.btlogin.setObjectName("btlogin")
        self.G_Tip = QtWidgets.QGroupBox(self.centralwidget)
        self.G_Tip.setGeometry(QtCore.QRect(200, 10, 421, 191))
        self.G_Tip.setObjectName("G_Tip")
        self.label = QtWidgets.QLabel(self.G_Tip)
        self.label.setGeometry(QtCore.QRect(10, 20, 341, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.G_Tip)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 341, 41))
        self.label_2.setObjectName("label_2")
        self.btadcon = QtWidgets.QPushButton(self.G_Tip)
        self.btadcon.setGeometry(QtCore.QRect(10, 140, 101, 31))
        self.btadcon.setObjectName("btadcon")
        self.btflash = QtWidgets.QPushButton(self.G_Tip)
        self.btflash.setGeometry(QtCore.QRect(130, 140, 101, 31))
        self.btflash.setObjectName("btflash")
        self.G_con = QtWidgets.QGroupBox(self.G_Tip)
        self.G_con.setGeometry(QtCore.QRect(240, 130, 171, 51))
        self.G_con.setObjectName("G_con")
        self.software = QtWidgets.QRadioButton(self.G_con)
        self.software.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.software.setObjectName("software")
        self.software.setChecked(True)
        self.browser = QtWidgets.QRadioButton(self.G_con)
        self.browser.setGeometry(QtCore.QRect(90, 20, 82, 17))
        self.browser.setObjectName("browser")
        self.browser.setChecked(False)
        self.G_specclass = QtWidgets.QGroupBox(self.centralwidget)
        self.G_specclass.setEnabled(True)
        self.G_specclass.setGeometry(QtCore.QRect(10, 210, 611, 221))
        self.G_specclass.setObjectName("G_specclass")
        self.btsubmit = QtWidgets.QPushButton(self.G_specclass)
        self.btsubmit.setGeometry(QtCore.QRect(10, 180, 150, 23))
        self.btsubmit.setObjectName("btsubmit")
        self.master = QtWidgets.QComboBox(self.G_specclass)
        self.master.setGeometry(QtCore.QRect(350, 20, 251, 22))
        self.master.setObjectName("master")
        self.label_3 = QtWidgets.QLabel(self.G_specclass)
        self.label_3.setGeometry(QtCore.QRect(290, 22, 61, 16))
        self.label_3.setObjectName("label_3")
        self.inputname = QtWidgets.QLineEdit(self.G_specclass)
        self.inputname.setGeometry(QtCore.QRect(110, 20, 150, 22))
        self.inputname.setAlignment(QtCore.Qt.AlignCenter)
        self.inputname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputname.setObjectName("inputname")
        self.inputnu = QtWidgets.QLineEdit(self.G_specclass)
        self.inputnu.setGeometry(QtCore.QRect(110, 50, 150, 22))
        self.inputnu.setAlignment(QtCore.Qt.AlignCenter)
        self.inputnu.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputnu.setObjectName("inputnu")
        self.label_4 = QtWidgets.QLabel(self.G_specclass)
        self.label_4.setGeometry(QtCore.QRect(40, 22, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.G_specclass)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_5.setObjectName("label_5")
        self.G_specclass.raise_()
        self.G_Login.raise_()
        self.G_Tip.raise_()
        self.pic = QtWidgets.QLabel(self.G_Login)
        self.pic.setGeometry(QtCore.QRect(30, 100, 150, 20))
        self.pic.setPixmap(QtGui.QPixmap(r"captcha.png"))
        self.inputkey = QtWidgets.QLineEdit(self.G_Login)
        self.inputkey.setGeometry(QtCore.QRect(10, 125, 150, 20))
        self.inputkey.setAlignment(QtCore.Qt.AlignCenter)
        self.inputkey.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputkey.setObjectName("inputkey")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btlogin.clicked.connect(self.login)
        self.btadcon.clicked.connect(self.adcon)
        self.btflash.clicked.connect(self.flash)
        self.btsubmit.clicked.connect(self.link)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Islamic Azad University Connect to the class"))
        self.G_Login.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.G_Login.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.G_Login.setTitle(_translate("MainWindow", "Login"))
        self.inputstudentnu.setPlaceholderText(_translate("MainWindow", "Student Number"))
        self.inputpassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.inputkey.setPlaceholderText(_translate("MainWindow", "Answer the question"))
        self.btlogin.setText(_translate("MainWindow", "Login"))
        self.G_Tip.setTitle(_translate("MainWindow", "Tip"))
        self.label.setText(_translate("MainWindow", "In software mode, you must install the Adobe Connect application.\n"
"\n"
"If you do not have the application, click the Adobe Connect button."))
        self.label_2.setText(_translate("MainWindow", "In browser mode you must install Adobe Flash Player.\n"
"\n"
"If you do not have the program, click the Adobe Flash button."))
        self.btadcon.setText(_translate("MainWindow", "Adobe Connect"))
        self.btflash.setText(_translate("MainWindow", "Adobe Flash"))
        self.G_con.setTitle(_translate("MainWindow", "Connection Type"))
        self.software.setText(_translate("MainWindow", "Software"))
        self.browser.setText(_translate("MainWindow", "Browser"))
        self.G_specclass.setTitle(_translate("MainWindow", "Class Specifications"))
        self.btsubmit.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Professor :"))
        self.inputname.setPlaceholderText(_translate("MainWindow", "Reza Bahrami"))
        self.inputnu.setPlaceholderText(_translate("MainWindow", "982132145"))
        self.label_4.setText(_translate("MainWindow", "Full name :"))
        self.label_5.setText(_translate("MainWindow", "Student Number :"))

    def login(self):
        selen2(self=self,app=app2)

    def flash(self):
        webbrowser.open("https://soft98.ir/software/flash-tools/29-adobe-flash-player.html")

    def adcon(self):
        webbrowser.open("https://dl2.soft98.ir/adobe/Adobe.Connect.Client.2020.1.5.3.zip?1596809939")

    def link(self):
        fullname = str(self.inputname.text())
        studentnu = str(self.inputnu.text())
        if fullname == "":
            self.inputname.setPlaceholderText("Enter your name !!")
        if studentnu == "":
            self.inputnu.setPlaceholderText("Enter correctly !!")

        ostad = str(self.master.currentText())
        con = self.browser.isChecked()
        i = urlencode({'guestName':f"{studentnu}-{fullname}",'launcher': 'true','html-view': 'false','proto': 'true'})
        if con == True :
            i = urlencode({'guestName':f"{studentnu}-{fullname}",'launcher': 'false','html-view': 'true','proto': 'flase'})
        
        if ostad in masters_links:
            send = f"{masters_links[ostad]}?{i}"
            print(send)
            webbrowser.open(f"{send}")

def selen():
    WINDOW_SIZE = "640,480"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    global app, username, password, captcha, submit
    captcha_number = 0
    app = webdriver.Chrome(chrome_options=chrome_options)
    app.get('https://cms.iauq.ac.ir/')
    img = app.find_element_by_xpath('//img[@id="ContentPlaceHolder1_Login1_imgCaptcha"]')
    get_captcha(app, img, captcha_number)
    username = app.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtUserName']")
    password = app.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtPassword']")
    captcha = app.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtSecurityImage']")
    submit = app.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_btnLogin']")
    return app

def selen2(self,app):
    user = str(self.inputstudentnu.text())
    pas = str(self.inputpassword.text())
    username.send_keys(f"{user}")
    password.send_keys(f"{pas}")
    key = str(self.inputkey.text())
    captcha.send_keys(f'{key}')
    submit.click()
    app.get(r'https://cms.iauq.ac.ir/31/%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C/%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8-%D9%88%D8%A7%D8%AD%D8%AF')
    name = app.find_element_by_xpath("//span[@id='ContentPlaceHolder1__MemberBox1_lblTitle']").text
    self.inputname.setText(f"{name}")
    self.inputnu.setText(f"{user}")
    table = app.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody")
    nutr = len(table.find_elements_by_tag_name("tr"))
    global masters_links
    masters_links = {}
    for x in range(1,nutr+1):
        namemaster = app.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody/tr[{x}]/td[4]")
        linkmaster = app.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody/tr[{x}]/td[2]/a").get_attribute("href")
        classid = re.findall(r'C\d*', linkmaster)
        self.master.addItem(namemaster.text)
        masters_new = {f'{namemaster.text}': f"http://class.iauq.ac.ir/{classid[0]}",}
        masters_links = ChainMap(masters_links, masters_new)
    
    #app.quit()

if __name__ == '__main__':
    app2 = selen()
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
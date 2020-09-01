import sys
import os
import webbrowser
import base64
import re
from urllib.parse import urlencode
from collections import ChainMap
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


os.environ['QT_API'] = 'pyqt5'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        loadUi('loginpage.ui', self)
        self.seleniumuni()
        self.InitUI()
        self.handelbuttons()

    def InitUI(self):
        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(50, 100, 150, 20))
        self.pic.setPixmap(QtGui.QPixmap(r"captcha.png").scaled(110, 120, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.show()

    def seleniumuni(self):
        WINDOW_SIZE = "640,480"
        self.chrome_options = Options()
        #self.chrome_options.add_argument("headless")
        self.chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.get('https://cms.iauq.ac.ir/')
        img = self.driver.find_element_by_xpath('//img[@id="ContentPlaceHolder1_Login1_imgCaptcha"]')
        get_captcha(self.driver, img, 0)
        self.fildusername = self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtUserName']")
        self.fildpassword = self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtPassword']")
        self.fildcaptcha = self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_txtSecurityImage']")
        self.btsubmit = self.driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_Login1_btnLogin']")
    
    def handelbuttons(self):
        self.submit.clicked.connect(self.login)
        self.menu_about.triggered.connect(self.about)

    def about(self):
        self.a = loadUi('about.ui')
        self.a.show()

    def login(self):
        username = self.inputuser.text()
        password = self.inputpass.text()
        captcha = self.inputcap.text()
        if username != '' and password != '':
            self.fildusername.send_keys(username)
            self.fildpassword.send_keys(password)
            self.fildcaptcha.send_keys(captcha)
            self.btsubmit.click()
            try:
                self.m = loadUi('main.ui', self)
                self.handelbuttons()
                self.master = QtWidgets.QComboBox(self.groupBox)
                self.master.setGeometry(QtCore.QRect(20, 80, 450, 30))
                self.master.setObjectName("master")
                self.driver.get(r'https://cms.iauq.ac.ir/31/%D8%A2%D9%85%D9%88%D8%B2%D8%B4%DB%8C/%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8-%D9%88%D8%A7%D8%AD%D8%AF')
                name = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//span[@id='ContentPlaceHolder1__MemberBox1_lblTitle']")))
                self.name = name.text
                self.inputfullname.setText(self.name)
                self.inputstudentnumber.setText(username)
                try:
                    self.class_submit.clicked.connect(self.classroom)
                    self.table = self.driver.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody")
                    nutr = len(self.table.find_elements_by_tag_name("tr"))
                    self.masters_links = {}
                    for x in range(1,nutr+1):
                        namemaster = self.driver.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody/tr[{x}]/td[4]")
                        linkmaster = self.driver.find_element_by_xpath(f"//table[@id='ContentPlaceHolder1_ContentPlaceHolder1_ctl00_GridView2']/tbody/tr[{x}]/td[2]/a").get_attribute("href")
                        classid = re.findall(r'C\d*', linkmaster)
                        self.master.addItem(namemaster.text)
                        self.masters_new = {f'{namemaster.text}': f"http://class.iauq.ac.ir/{classid[0]}",}
                        self.masters_links = ChainMap(self.masters_links, self.masters_new)
                        
                except Exception as e:
                    self.master.addItem('هیچ استادی یافت نشد.')
                    print("Error >>  ",e)

                self.driver.quit()
                                
            except Exception as e:
                self.driver.quit()
                self.seleniumuni()
                self.pic.setPixmap(QtGui.QPixmap(r"captcha.png").scaled(110, 120, Qt.KeepAspectRatio, Qt.FastTransformation))
                self.inputuser.setText('! اشتباه !')
                self.inputpass.setText('! اشتباه !')
                QtWidgets.QApplication.processEvents()

        elif username == '' or password == '':
            if username == '' and password == '':
                self.inputuser.setText('خالی نباشد')
                self.inputpass.setText('خالی نباشد')
            elif password == '':
                self.inputpass.setText('خالی نباشد')
            else:
                self.inputuser.setText('خالی نباشد')
    
    def classroom(self):
        fullname = self.inputfullname.text()
        studentnumber = self.inputstudentnumber.text()
        if fullname != '' and studentnumber != '':
            ostad = str(self.master.currentText())
            #con = self.browser.isChecked()
            i = urlencode({'guestName':f"{studentnumber}-{fullname}",'launcher': 'true','html-view': 'false','proto': 'true'})
            #if con == True :
            #i = urlencode({'guestName':f"{studentnumber}-{fullname}",'launcher': 'false','html-view': 'true','proto': 'flase'})
            if ostad in self.masters_links:
                send = f"{self.masters_links[ostad]}?{i}"
                print(send)
                webbrowser.open(f"{send}")
        elif fullname == '' or studentnumber == '':
            if fullname == '' and studentnumber == '':
                self.inputfullname.setText('خالی نباشد')
                self.inputstudentnumber.setText('خالی نباشد')
            elif fullname == '':
                self.inputfullname.setText('خالی نباشد')
            else:
                self.inputstudentnumber.setText('خالی نباشد')


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


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

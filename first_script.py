from selenium import webdriver
from time import sleep
from Admin_creds import username,password    
from usercreds import userid,uname,passd
from selenium.webdriver.common.by import By


class ameyo():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        url = input("Enter Ameyo url: ")
        self.driver.get(url)
        sleep(2)

        email = self.driver.find_element_by_xpath('//*[@id="gwt-uid-1"]')
        email.send_keys(username)

        passd = self.driver.find_element_by_xpath('//*[@id="gwt-uid-2"]')
        passd.send_keys(password)

        clickbtn = self.driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[3]/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/form/div[6]/div/button')
        clickbtn.click()

        sleep(10)

        #user = self.driver.find_element_by_xpath('//*[@id="automationIdAdminUserManagementTab"]/span') 
        #user.click()

        #add = self.driver.find_element_by_xpath('//*[@id="automationIdAdminAddUserButton"]/span')
        #add.click()

        #self.driver.find_e

        #uid = self.driver.find_elements_by_class_name('gwt-TextBox')
        #uid.send_keys(userid)

        #usrname = self.driver.find_element_by_xpath('//*[@id="gwt-uid-450"]')
        #usrname.send_keys(uname)

        #passwd = self.driver.find_element_by_class_name('gwt-PasswordTextBox')
        #passwd.send_keys(passd)

        #cpasswd = self.driver.find_element_by_class_name('gwt-PasswordTextBox')
        #cpasswd.send_keys(passd)

        #usertype = self.driver.find_element_by_xpath('//*[@id="gwt-uid-443"]/span[1]/span[1]/span/span[2]')
        #usertype.click()

        #pa = self.driver.find_element_by_xpath('//*[@id="select2-vzeg-result-wei7-Professional-Agent"]')
        #pa.click()

        #save = self.driver.find_element_by_xpath('//*[@id="automationIdAdminAddUserApplyButton"]')
        #save.click()
        
    #def logout(self):
        dd = self.driver.find_element_by_xpath('//*[@id="ameyo-body"]/div[4]/header/nav/div/ul[2]/li/a/i')
        dd.click()
        
        self.driver.find_element_by_xpath('//*[@id="userdp2"]/li[3]/a/span').click()
        




bot = ameyo()
bot.login()
#bot.logout()




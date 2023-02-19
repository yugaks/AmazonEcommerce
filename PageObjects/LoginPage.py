from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    button_sigin_xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div/div[2]/span/span/a"
    textbox_mobilenumber_id="ap_email"
    button_continue_id="continue"
    textbox_password_name="password"
    button_signin_id="signInSubmit"
    linktext_Allmenu_id="nav-hamburger-menu"
    linktext_signout_xpath="//a[@class='hmenu-item'][normalize-space()='Sign Out']"

    def __init__(self,driver):
        self.driver=driver

    def ClickSigin(self):
        self.driver.find_element(By.XPATH,"button_sigin_xpath").click()

    def setmobileNumber(self,mobileNumber):
        self.driver.find_element(By.ID,"textbox_mobilenumber_id").send_keys(mobileNumber)

    def ClickContinue(self):
        self.driver.find_element(By.ID,"button_continue_id").click()

    def setPassword(self,Password):
        self.driver.find_element(By.NAME,"textbox_password_name").send_keys(Password)

    def ClickSignin(self):
        self.driver.find_element(By.ID, "button_signin_id").click()

    def ClickAllmenu(self):
        self.driver.find_element(By.ID, "linktext_Allmenu_id").click()

    def ClickSignout(self):
        self.driver.find_element(By.XPATH, "linktext_signout_xpath").click()












import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL="https://www.amazon.in/"
    mobileNumber="8147877848"
    password="ullasAmazon"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.ClickSigin()
        self.lp.setmobileNumber(self.mobileNumber)
        self.lp.ClickContinue()
        self.lp.setPassword(self.password)
        self.lp.ClickSignin()
        act_title=self.driver.title
        if act_title=="Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
            assert True
        else:
            assert False



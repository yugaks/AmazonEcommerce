import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:\webdrivers.chromedriver.exe")
    return driver


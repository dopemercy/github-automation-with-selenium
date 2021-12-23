import pytest
from selenium.webdriver.common.by import By
from config import username, repository_name
import time
from withselenium import MyClass


test = MyClass()

def test_login():
    test.login()
    assert "GitHub" == test.driver.title


def test_createrepo():
    time.sleep(3)
    test.create_repo()
    assert username+"/"+repository_name == test.driver.title


def test_deleterepo():
    time.sleep(1)
    test.del_repo()
    assert "Your repository "+'"'+username+"/"+repository_name+'"' + \
        " was successfully deleted." == test.driver.find_element(by = By.XPATH,value=
            '//*[@id="js-flash-container"]/div/div').text


        
        

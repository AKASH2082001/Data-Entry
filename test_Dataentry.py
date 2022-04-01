from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def setUp():
    global Name,Address,Pincode,Mobile,Email_Id,Password,Confirm_Password,driver
    Name = input("Enter the name: ")
    Address = input("Enter the Address: ")
    Pincode = input("Enter the pincode: ")
    Mobile = input("Enter the Mobile no: ")
    Email_Id = input("Enter the Email ID: ")
    Password = input("Enter the Password: ")
    Confirm_Password = input("Enter the password again: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield
    time.sleep(5)
    driver.close()

def test_DataEntry(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/userdata.php")
    time.sleep(2)
    driver.find_element_by_name("name").send_keys(Name)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[2]").click()
    time.sleep(2)
    driver.find_element_by_name("Address").send_keys(Address)
    time.sleep(2)
    driver.find_element_by_name("Pincode").send_keys(Pincode)
    time.sleep(2)
    driver.find_element_by_name("Mobile").send_keys(Mobile)
    time.sleep(2)
    driver.find_element_by_name("Email").send_keys(Email_Id)
    time.sleep(2)
    driver.find_element_by_name("pass").send_keys(Password)
    time.sleep(2)
    driver.find_element_by_name("cnfpass").send_keys(Confirm_Password)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[10]/td[2]/div/input").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)

from selenium.webdriver.common.by import By
from time import sleep
from utils import *
from locators.element_locators import ElementLocators

def go_to_reddit(driver):
    driver.get("https://www.reddit.com")

def main():
    driver = driver_setup()
    go_to_reddit(driver)
    login_button = try_getting(ElementLocators.LOGIN_BUTTON, driver)
    print("Found button")

main()
sleep(10)

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://us-east-1.signin.aws.amazon.com/oauth?response_type=code&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fnc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgs%2523%26isauthcode%3Dtrue&forceMobileLayout=0&forceMobileApp=0"
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


def login(account_id, username, password):
    browser = webdriver.Chrome(executable_path=DRIVER_BIN)
    browser.get(URL)
    action = webdriver.ActionChains(browser)
    account_field = browser.find_element_by_id("account")
    account_field.send_keys(account_id)
    username_field = browser.find_element_by_id("username")
    username_field.send_keys(username)
    password_field = browser.find_element_by_id("password")
    password_field.send_keys(password)
    browser.find_element_by_id("signin_button").click()


def main():
    login("a", "b", "c")


if __name__ == "__main__":
    main()

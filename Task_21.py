# Task_21.py
# Import necessary libraries for web automation using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Class for URL and basic data
class Data:
   url = "https://www.saucedemo.com/"
   username ="standard_user"
   password = "secret_sauce"

# Class for web-elements locator
class Locators:
    username_id = "user-name"
    password_id = "password"
    login_btn_id = "login-button"
    menu_btn_id = "react-burger-menu-btn"
    logout_btn_id = "logout_sidebar_link"

# Class for webpage automation with constructor
class CookieAutomation (Data,Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def login(self):
        # Locate the username, password fields, and login button to perform login
        self.wait.until(EC.element_to_be_clickable((By.ID, self.username_id))).send_keys(self.username)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.password_id))).send_keys(self.password)
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.login_btn_id)))
        login_button.click()

    def get_cookies(self):
        # Return the current cookies in the browser
        return self.driver.get_cookies()

    def logout(self):
        # Find and click the menu button, then the logout button
        self.wait.until(EC.element_to_be_clickable((By.ID, self.menu_btn_id))).click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.logout_btn_id)))
        logout_button.click()

    def close_browser(self):
        # Close the browser after operations
        self.driver.quit()
"""test_CookieAutomation .py"""
import pytest
from Task_21 import CookieAutomation

def test_cookies_before_login():
    # Create an instance of the WebAutomation class
    obj = CookieAutomation()
    # Test to check if there are no cookies before login.
    print("Cookies before login")
    cookies_before_login = obj.get_cookies()
    if cookies_before_login:
        for cookie in cookies_before_login:
            print(cookie)
    else:
        print("No cookies found before login.")
    assert len(cookies_before_login) == 0, "Cookies should be empty before login."

def test_cookies_after_login():
    obj = CookieAutomation()
    # Test to check if cookies are set after login.
    print("Cookies after login")
    # Perform login operation
    obj.login()
    cookies_after_login = obj.get_cookies()
    if cookies_after_login:
        for cookie in cookies_after_login:
            print(cookie)
    else:
        print("No cookies found after login.")
    assert len(cookies_after_login) > 0, "Cookies should be set after login."
    # Perform logout operation
    obj.logout()
    # Close the browser after the operations
    obj.close_browser()

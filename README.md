# PAT-Task-21

## Overview:

This project automates the process of logging into the SauceDemo website using Selenium. It checks the state of cookies before and after logging in and performs logout operations. The purpose of this project is to demonstrate how to handle web elements, cookies, and basic login/logout functionality using Selenium WebDriver.

## Table of Contents:
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Code Explanation](#Code-Explanation)
- [Working of Test Cases](#Working-of-Test-Cases)
- [Running the test](#Running-the-test)

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `webdriver-manager`
 
## Installation:
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from  [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure
```
PAT Task 21/
│
├── Task_21.py                      # Main automation script for handling login, logout, and cookie management
├── test_CookieAutomation.py        # Test cases for verifying cookie state before and after login
├── cookie.html                     # Pytest html report
└── README.md                       # This README file
```

## Code Explanation
### Task_21.py
This script contains the main logic for the Selenium WebDriver automation:

- __Data class:__ This class Stores the URL, username, and password.

- __Locators class:__ This class contains the identifiers for various elements like username, password, login button, and logout button.

- __WebAutomation class:__ Handles the browser automation, including login, logout, and cookie management functionalities.

### Methods in `WebAutomation` class:
- `login()`: Logs in to the website using the stored username and password.

- `get_cookies()`: Retrieves and returns the cookies from the current session.
  
- `logout()`: Logs out of the website by interacting with the menu and logout button.
  
- `close_browser()`: Closes the browser after the operations.

### test_CookieAutomation.py
This script uses `pytest` to perform tests on the automation script:

- __test_cookies_before_login():__ Verifies that no cookies are set before logging in.
  
- __test_cookies_after_login():__ Verifies that cookies are set after logging in.

## Working of Test Cases

-__test_cookies_before_login:__ This test checks if there are no cookies before logging in by calling the `get_cookies()` method. It asserts that the cookie count is 0 before the login process.

-__test_cookies_after_login:__ This test performs the login operation using the `login()` method and then checks if cookies are set. After that, it asserts that there is at least one cookie after logging in.

-__Logout and Close:__ After the tests, the `logout()` method is called to log out from the website, and the `close_browser()` method is used to close the browser.

## Running the test:
- This script uses `pytest` to perform tests on the automation script:

  - Make sure the project and dependencies are properly set up.

  - Run the following command to execute the test cases:
 
  ```
  pytest -v -s --capture=sys --html=Reports\cookie.html test_CookieAutomation.py 
  ```



  



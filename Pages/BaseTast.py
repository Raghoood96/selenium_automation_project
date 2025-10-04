from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    """The Base Test How other Pages inheritance"""

    def __init__(self, driver):
        self.driver = driver
        # self.wait = wait


    def find_element(self, locator):
        """Find the Element with Waiting"""
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        """ click on the element"""
        return self.driver.find_element(*locator)

    def get_title(self):
        """Get the title of the Page"""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL"""
        return self.driver.current_url
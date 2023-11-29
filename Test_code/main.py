import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_yogi.Locators import Test_Locators
from Test_yogi.excel_functions import Excel_Functions
from selenium.common.exceptions import *


class Test_code_1:
    url = "https://www.zenclass.in/login"

    @pytest.fixture()
    def Home_page(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_code(self, Home_page):
        self.driver.maximize_window()
        self.driver.get(self.url)
        excel_file = "C:\\Users\\Admin\\Desktop\\Mr_yogi\\Book1.xlsx"
        sheet_number = "Sheet1"

        a = Excel_Functions(excel_file, sheet_number)
        row = a.row_count()
        self.driver.implicitly_wait(15)
        for row in range(3, row + 1):
            username = a.read_data(row, 3)
            password = a.read_data(row, 4)
            print(username)
            print(password)
            wait = WebDriverWait(self.driver, 10, 1, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementNotInteractableException,
                                                                         TimeoutException])
            username_box = wait.until(EC.presence_of_element_located((By.XPATH, Test_Locators().username_input)))
            username_box.send_keys(username)
            password_box = wait.until((EC.presence_of_element_located((By.XPATH,Test_Locators().password_input))))
            password_box.send_keys(password)
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH,Test_Locators().logout_button)))
            login_button.click()

        # basil@guvi.in

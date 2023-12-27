import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from BasePageObject import BasePageObject

class TestEndToEndSaucedemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_successful_login(self):
        login_page = BasePageObject(self.driver)
        login_page.enter_credentials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        time.sleep(3)
        # Assertions untuk memastikan bahwa login berhasil
        Product = self.driver.find_element(By.CLASS_NAME, 'title').text
        assert Product == "Products"
        time.sleep(2)

    def test_successfully_adding_to_basket(self):
        product = BasePageObject(self.driver)
        self.test_successful_login()
        product.select_product()
        time.sleep(2)
        Keranjang = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').text
        assert Keranjang == '1'
        time.sleep(2)

    def test_user_verifying_price_are_corrected(self):
        cart = BasePageObject(self.driver)
        self.test_successfully_adding_to_basket()
        # self.test_successful_login()
        # cart.select_product()
        cart.click_cart()
        time.sleep(2)
        Check_Price = self.driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
        assert Check_Price == '$29.99'

    def test_user_successfully_postcheckout(self):
        postcheckout = BasePageObject(self.driver)
        self.test_user_verifying_price_are_corrected()
        postcheckout.checkout()
        time.sleep(2)
        postcheckout.input_form_checkout("Je", "Test", "120983")
        time.sleep(2)
        postcheckout.postcheckout()
        time.sleep(2)
        postcheckout.finishorder()
        time.sleep(2)
        Finish = self.driver.find_element(By.CSS_SELECTOR, '.complete-header').text
        assert Finish == 'Thank you for your order!'

if __name__ == '__main__':
    unittest.main()

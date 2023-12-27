from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageObject:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")
        self.product_locator = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.input_firstName = (By.ID, "first-name")
        self.input_lastName = (By.ID, "last-name")
        self.input_postCode = (By.ID, "postal-code")
        self.postcheckout_button = (By.ID, "continue")
        self.finis_order_button = (By.ID, "finish")

    def enter_credentials(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_locator)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_locator)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        ).click()

    def select_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_locator)
        ).click()

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_locator)
        ).click()

    def checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def input_form_checkout(self, firstName, lastName, postalCode):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_firstName)
        ).send_keys(firstName)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_lastName)
        ).send_keys(lastName)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.input_postCode)
        ).send_keys(postalCode)

    def postcheckout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.postcheckout_button)
        ).click()

    def finishorder(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finis_order_button)
        ).click()
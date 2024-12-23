from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver


class TestNavigateToPersonalAccount:
    # Проверка перехода из конструктора бургеров в личный кабинет
    def test_navigate_from_constructor_to_personal_account(self, driver):
        email = 'gzvoznikova@ya.ru'
        password = 'qwerty123'
        driver.find_element(*TestLocators.button_personal_account).click()
        driver.find_element(*TestLocators.input_email_auth).send_keys(email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_make_the_order))
        driver.find_element(*TestLocators.button_personal_account).click()
        assert driver.find_element(*TestLocators.order_history).is_displayed()

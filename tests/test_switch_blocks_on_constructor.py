from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from conftest import driver


class TestSwitchBlocksOnConstructor:

    # Проверка перехода из раздела "Соусы" в раздел "Начинки"
    def test_navigate_to_fillings_block_from_sauces_on_constructor_success(self, driver):
        driver.find_element(*TestLocators.sauces_block).click()
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    # Проверка перехода из раздела "Начинки" в раздел "Соусы"
    def test_navigate_to_sauces_block_from_fillings_on_constructor_success(self, driver):
        driver.find_element(*TestLocators.sauces_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    # Проверка перехода из раздела "Начинки" в раздел "Булки"
    def test_navigate_to_buns_block_from_fillings_on_constructor_success(self, driver):
        driver.find_element(*TestLocators.sauces_block).click()
        driver.find_element(*TestLocators.buns_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"

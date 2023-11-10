import pytest
import random
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture
def get_phone_number():
    return random.randint(79000000000, 79999999999)


@pytest.fixture
def get_date_today():
    return datetime.date.today().strftime('%d.%m.%Y')


@pytest.fixture
def get_date_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser ..")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching FireFox Browser ..")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):   # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the Browser value to setup method
    return request.config.getoption("--browser")
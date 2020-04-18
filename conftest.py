import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                         help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                         help="Choose language: ec or fr")



@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif (browser_name=="firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart chrome browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> is still not implemented")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()

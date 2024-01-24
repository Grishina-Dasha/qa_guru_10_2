import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.open()
    browser.config.window_height = 1440
    browser.config.window_width = 700
    yield
    browser.quit()

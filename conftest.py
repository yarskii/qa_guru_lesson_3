from selene import browser
import pytest

duckduckgo = 'https://duckduckgo.com'
yandex = 'https://ya.ru'
google = 'https://www.google.com/ncr'


@pytest.fixture(scope='session')
def open_browser():
    browser.config.window_width = 960
    browser.config.window_height = 640
    browser.open(duckduckgo)

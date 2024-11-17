from selene import browser, be, have
import pytest
from selene.core.exceptions import TimeoutException
from selenium.common import NoSuchElementException

enter_word = 'yashaka/selene'
looking_text = 'User-oriented Web UI browser tests in Python'


def test_duckduckgo(open_browser):
    browser.element('[name=q]').should(be.blank).type(enter_word).press_enter()
    browser.element('[id=react-layout]').should(have.text(looking_text))


def test_duckduckgo_false(open_browser):
    browser.element('[name=q]').clear().type(
        'iejghalkkgларопылдворпыдлвпордлkdfjghskdlfjhsflkdjhдлапорфавдлпрфлдо').press_enter()
    browser.element('[id=react-layout]').should(have.text('результаты не найдены.'))

def test_ya(open_browser):
    browser.element('[name=q]').clear().type('https://ya.ru').press_enter()
    browser.element('[id=react-layout]').should(have.text('Яндекс — быстрый поиск в интернете')).click()
    try:
        browser.element('[id=checkbox-label]').should(have.text('Я не робот'))
        print('CAPTCHA')
    except TimeoutException:
        browser.element('[id=text]').should(be.blank).type(enter_word).press_enter()
        browser.element('[id=search-result]').should(have.text(looking_text))

import allure
import pytest
from playwright.sync_api import Page

from pages.pages import Pages
from utils.consts import LOGIN_PAGE
from utils.data import LOGIN_DATA
from utils.texts import *
from utils.users import USER_FOR_TEST

class TestLoginPage:
    @allure.title('Check login with empty Password')
    def test_login_with_empty_password_page(self, page: Page, pages: Pages):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.user_name.fill(USER_FOR_TEST.login)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_USERNAME)

    @allure.title('Check login with empty username and password')
    def test_login_with_empty_username_and_password_page(self, page: Page, pages: Pages):
        page.goto(LOGIN_PAGE)
        pages.login.title.check_text(TITLE_LOGIN_PAGE)
        pages.login.button_login.click()
        pages.login.alert.check_contain_text(ALERT_USERNAME_INVALID)

    


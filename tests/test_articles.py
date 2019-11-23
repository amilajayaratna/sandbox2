import pytest
import allure

from selenium.webdriver import Chrome
from pages.search import SlashDotHomePage


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.description("this is amila test")
@allure.title("Count articles on homepage")
def test_articles_on_homepage(browser):
    slackdot_page = SlashDotHomePage(browser)
    slackdot_page.load()

    article_count = slackdot_page.get_articles()
    assert len(article_count) > 10
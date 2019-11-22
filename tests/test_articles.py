import pytest

from selenium.webdriver import Chrome
from pages.search import SlashDotHomePage


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_articles_on_homepage():
    slackdot_page = SlashDotHomePage(browser)
    slackdot_page.load()

    article_count = slackdot_page.get_articles()
    assert len(article_count) > 10
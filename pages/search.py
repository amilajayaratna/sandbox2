from selenium.webdriver.common.by import By


class SlashDotHomePage:
    URL = 'https://slashdot.org/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_articles(self):
        search_input = self.browser.find_elements(By.CSS_SELECTOR, "#firehoselist [data-fhtype='story']")

        return search_input
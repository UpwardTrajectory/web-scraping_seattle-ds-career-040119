import requests
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.keys import Keys


def scrape_company_data(companies):
    """Scrape data from Glassdoor on companies in list."""
    browser = Chrome()
    url = "https://www.glassdoor.com/Reviews/index.htm"
    browser.get(url)

    for company in companies:
        sel = "input#KeywordSearch.keyword"
        search_bar = browser.find_element_by_css_selector(sel)

        search_bar.send_keys(company)
        search_bar.send_keys(Keys.ENTER)

        if len(browser.window_handles) > 1:
            tab_1, tab_2 = browser.window_handles
            browser.switch_to.window(tab_1)
            browser.close()
            browser.switch_to.window(tab_2)

        sel = "a.tightAll.h2"
        company_link = browser.find_element_by_css_selector(sel)
        company_link.click()

        sel = "a.eiCell.cell.reviews"
        reviews_link = browser.find_element_by_css_selector(sel)
        reviews_link.click()

        dummy_function()
        browser.get(url)
        
        
def dummy_function():
    """Stand-in for Hussein and Lee's work."""
    pass


def get_fortune_500():
    """Stand-in for Kaspar's work."""
    return ["Google", "Amazon", "AMD"]
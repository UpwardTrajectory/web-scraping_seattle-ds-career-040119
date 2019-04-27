import requests
from time import sleep
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.keys import Keys
import pandas as pd

def get_ratingNum(browser):
    """Return the ratingNum metric"""
    try:
        sel = "div.ratingNum"
        title = browser.find_element_by_css_selector(sel)
    except:
        try:
            sel = "div.common__EIReviewsRatingsStyles__ratingNum.mb-sm.mb-md-0"
            title = browser.find_element_by_css_selector(sel)
        except Exception as e:
            print(e)
            print("error for ", company)
    return title.text

def get_EmpStats_Recommend(browser):
    """Return the EmpStats_Recommend metric"""
    sel = "div#EmpStats_Recommend svg text"
    title = browser.find_element_by_css_selector(sel)
    return title.text

def get_EmpStats_Approve(browser):
    """Return the EmpStats_Approve metric"""
    sel = "div#EmpStats_Approve svg text"
    title = browser.find_element_by_css_selector(sel)
    return title.text

def get_stats(browser):
    """perform all 3 data requests, and return as list"""
    stats_list = []
    stats_list.append(get_ratingNum(browser))
    stats_list.append(get_EmpStats_Recommend(browser))
    stats_list.append(get_EmpStats_Approve(browser))
    return stats_list

def scrape_company_data(companies):
    """Scrape data from Glassdoor on companies in list."""
    browser = Chrome()
    url = "https://www.glassdoor.com/Reviews/index.htm"
    browser.get(url)
    final_data = []
    sleep(23)
    
    for company in companies:
        try:
            sel = "input#KeywordSearch.keyword"
            search_bar = browser.find_element_by_css_selector(sel)

            search_bar.send_keys(company)
            search_bar.send_keys(Keys.ENTER)
            sleep(4)

            if len(browser.window_handles) > 1:
                tab_1, tab_2 = browser.window_handles
                browser.switch_to.window(tab_1)
                browser.close()
                browser.switch_to.window(tab_2)

            sel = "a.tightAll.h2"
            company_link = browser.find_element_by_css_selector(sel)
            company_link.click()
            sleep(4)

            sel = "a.eiCell.cell.reviews"
            reviews_link = browser.find_element_by_css_selector(sel)
            reviews_link.click()
            sleep(4)

            temp_stats = [company]
            stats = get_stats(browser)
            for stat in stats:
                temp_stats.append(stat)
            print(temp_stats)
            final_data.append(temp_stats)

            browser.get(url)
        except Exception as e:
            print(e)
            print('error with ', company)
            url = "https://www.glassdoor.com/Reviews/index.htm"
            browser.get(url)
        
    return pd.DataFrame(final_data, columns=['Company', 'Rating', 'Employee Recommended', 'CEO Approval'])
        


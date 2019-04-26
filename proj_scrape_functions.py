import requests

def get_ratingNum(browser):
    """Return the ratingNum metric"""
    sel = "div.ratingNum"
    title = browser.find_element_by_css_selector(sel)
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
    stats_list = []
    stats_list.append(get_ratingNum(browser))
    stats_list.append(get_EmpStats_Recommend(browser))
    stats_list.append(get_EmpStats_Approve(browser))
    return stats_list
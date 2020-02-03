from selenium import webdriver
from time import sleep

class Scraper:
    def __init__(self, location):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://openweathermap.org/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Your city name']").send_keys(location)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="searchform"]/button').click()
        sleep(2)
        # find_elements_by_tag_name

Scraper('Cape Town')
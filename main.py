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
        temp = self.driver.find_element_by_class_name("badge-info")

        print("TEMP", temp.text)

        f = open("file.txt", "a")
        f.write(temp.text[0:4])
        f.close()


Scraper('Cape Town')
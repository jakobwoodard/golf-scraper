from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.golfnow.com/tee-times/search#qc=GeoLocation&q=Cape+Carteret&sortby=Facilities.Distance.0&view=Course&date=Mar+04+2025&holes=3&radius=35&timemax=42&timemin=10&players=0&pricemax=10000&pricemin=0&promotedcampaignsonly=false&hotdealsonly=false&longitude=-77.063&latitude=34.69155")
#assert "Python" in driver.title
courses = driver.find_elements(By.CLASS_NAME, "course-details")
prices = driver.find_elements(By.CLASS_NAME, "price")

for (course, price) in zip(courses, prices):
    print(course.text)
    print(price.text)
else: 
    driver.close()
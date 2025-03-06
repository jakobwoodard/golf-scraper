from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

# list of how golfnow represents months in their search queries
golfnow_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

desired_location = input("Search for courses near: ")
golfnow_location = desired_location.replace(' ', '+')
print(golfnow_location)

desired_date = input("Show courses with available times on (mm/dd): ")
date_tokens = desired_date.split('/')
print(golfnow_months[int(date_tokens[0])])

driver = webdriver.Firefox()
driver.get(f"https://www.golfnow.com/tee-times/search#qc=GeoLocation&q={golfnow_location}&sortby=Facilities.Distance.0&view=Course&date={golfnow_months[int(date_tokens[0])]}+{desired_date[1]}+2025&holes=3&radius=35&timemax=42&timemin=10&players=0&pricemax=10000&pricemin=0&promotedcampaignsonly=false&hotdealsonly=false&longitude=-77.063&latitude=34.69155")
#assert "Python" in driver.title
courses = driver.find_elements(By.CLASS_NAME, "course-details")
prices = driver.find_elements(By.CLASS_NAME, "price")

for (course, price) in zip(courses, prices):
    print(course.text)
    print(price.text)
else: 
    driver.close()
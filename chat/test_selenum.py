import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('/home/kaa/.local/bin/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/')
time.sleep(5)   # Let the user actually see something!
driver.quit()

# Create a new instance of the Firefox driver
driver = webdriver.Remote(service.service_url)

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese!")

# submit the form
# (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing
    #  that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print(driver.title)

finally:
    driver.quit()
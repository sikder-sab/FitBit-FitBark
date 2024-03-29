import fitbit
import oauth2
import requests
import threading
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import threading
import re
import openpyxl
from openpyxl import Workbook
import os
from datetime import datetime

def checkURLAndGetCode(webDriver):
    currentURL = webDriver.current_url
    print(currentURL)
    if "google.com" in currentURL:
        try:
            allowButton = driver.find_element_by_id("searchfake")
            return "allow"
        except:
            return "fake"
    else:
        timer = threading.Timer(3.0, checkURLAndGetCode(webDriver))
        timer.start
#--------------------------------------------------------------------------------

authenticationUrl = "https://www.google.com/search?q=hello"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options) 
driver.get(authenticationUrl)

authencode = checkURLAndGetCode(driver)
print(authencode)
driver.close()
    
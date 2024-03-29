import fitbark
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import threading
import re
from datetime import datetime, timedelta
import requests
import http.client
import json
import os
import openpyxl
from openpyxl import Workbook



testURL = "www.google.com"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options) 
driver.get(testURL)
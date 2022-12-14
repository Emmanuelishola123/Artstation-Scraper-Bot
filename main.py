# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from keep_alive import alive
from utils.scraper import scrape_artstation_user
from utils.users import get_all_users
import chromedriver_autoinstaller


# CONFIG FOR PRODUCTION ENV
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# alive()
users = get_all_users()
i = 0

# alive()

while True:
    #driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)         
    
    user_url = users[i]
    print(user_url)
    print(len(users))


    print(f'Scraping {user_url} profile in progress...........................')
    scrape_artstation_user(user_url, driver, WebDriverWait, By, EC)
    print('Done Scraping.......................')

    i = i + 1
    if i >= len(users):
        i = 0

    # Sleep for 30secs, then continua
    time.sleep(30)

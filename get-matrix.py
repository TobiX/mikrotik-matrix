#!/usr/bin/env python3

import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

target = Path(__file__).parent / 'pages'
target.mkdir(exist_ok=True)
tfile = target / 'product_matrix.csv'
tfile.unlink(missing_ok=True)

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_experimental_option('prefs', {
    "download.default_directory": str(target),
})
driver = webdriver.Chrome(options=options)
driver.get('https://mikrotik.com/products/matrix')
csv_link = driver.find_element(by=By.CSS_SELECTOR, value="a.csv")
csv_link.click()
while not tfile.exists():
    time.sleep(0.1)
driver.quit()

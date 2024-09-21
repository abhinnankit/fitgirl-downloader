from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime

import time
import sys
import os

WEBSITE_URL = 'https://paste.fitgirl-repacks.site/?2d25d933656bc78a#6vZZAEdL8nYvhxN5Vji88SNLAkBEHhtXEUfQquPQ6Rw2'
DOWNLOAD_DIR = '/Users/abhinnankit/Downloads' # Update downloads directory path where the files are going to be downloaded


def launch_chrome(url):
    # Set up the WebDriver (Ensure that the path to your webdriver is correct)
    ch_options = webdriver.ChromeOptions()
    lt_options = {"build": "Build: FuckingFast link downloader",
                  "project": "Project: FuckingFast link downloader",
                  "name": "Test: FuckingFast link downloader", "browserName": "Chrome",
                  "browserVersion": "latest", "platformName": "Windows 11", "console": "error", "w3c": (True,),
                  "headless": False, "network": (True,), "video": (True,), "visual": True}

    ch_options.set_capability('LT:Options', lt_options)

    # Open the desired website
    driver = webdriver.Chrome(options=ch_options)
    driver.get(url)
    driver.maximize_window()

    return driver


def wait_for_page_to_load(locator: Tuple[str, str], driver):
    # Get current time stamp
    web_driver_clock = datetime.now()
    current_time_webdriver = web_driver_clock.strftime("%H:%M:%S")

    print("\nTime before waiting for #plaintext button with webdriver=", current_time_webdriver)
    WebDriverWait(driver, 10, poll_frequency=5).until(ec.visibility_of_element_located(locator),
                                                      'Timed out waiting for element to appear')

    # Get current time stamp after wait
    element_found = datetime.now()
    current_time_element_found = element_found.strftime("%H:%M:%S")
    print("Time when Element Found=", current_time_element_found)


def latest_download_file(download_dir=DOWNLOAD_DIR):
    os.chdir(download_dir)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    latest_f = files[-1]
    return latest_f


def wait_for_download_to_finish():
    has_cr_download = True
    while has_cr_download:
        time.sleep(1)
        newest_file = latest_download_file()
        if not "crdownload" in newest_file:
            has_cr_download = False


def open_page(driver):
    # Wait for element to appear
    wait_for_page_to_load((By.ID, 'plaintext'), driver)

    # Find all <li> tags and extract the links
    links = []
    li_tags = driver.find_elements(By.CSS_SELECTOR, '#plaintext li')

    for li in li_tags:
        # Find anchor tags within the <li> and get their href attributes
        a_tag = li.find_element(By.TAG_NAME, 'a')
        link = a_tag.get_attribute('href')
        if link:
            links.append(link)

    # Loop through the list of links and open each one in a new tab
    for link in links:
        # Open a new tab
        driver.execute_script(f"window.open('{link}');")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        button_xpath = "//button[contains(text(), 'DOWNLOAD')]"
        wait_for_page_to_load((By.XPATH, button_xpath), driver)

        # Click download button twice since it opens ads the first time
        download_button = driver.find_elements(By.XPATH, button_xpath)
        download_button[0].click()

        # Close the ads tab
        driver.switch_to.window(driver.window_handles[2])
        driver.close()

        # Start the download
        driver.switch_to.window(driver.window_handles[1])
        download_button[0].click()

        # Wait for 5 seconds
        wait_for_download_to_finish()

        # Close the current tab
        driver.close()

        # Switch back to the main window (the first tab)
        driver.switch_to.window(driver.window_handles[0])


def main(url=None):
    driver = launch_chrome(url) if url else launch_chrome(WEBSITE_URL)

    open_page(driver)

    print("\nAll files have been downloaded...\nClosing browser...")
    # Close the main browser window after processing all links
    driver.quit()


if __name__ == "__main__":
    main(*sys.argv[1:])

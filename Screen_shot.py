from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loguru import logger
from PIL import Image
import json
import time
import os

the_timestamp = int(time.time())

class Screen_shot:
    def __init__(self):
        pass
        self.width = 1920
        self.height = 15000
        self.elements = {}
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument(
            f"--window-size={self.width},{self.height}")
        self.chrome_options.add_argument("--hide-scrollbars")
        self.chrome_options.add_argument('disable-infobars')
        self.chrome_options.add_argument("--disable-logging")
        # self.chrome_options.add_extension('ublock_origin.crx')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def Full_screenshot(self, url, save_path='', image_name=f'{the_timestamp}.png'):
        logger.info('Starting chrome full page screenshot Capturing ...')
        self.driver.get(url)
        time.sleep(2)
        # save screenshot
        abs_save_path = os.path.abspath(save_path + '/' + image_name)
        self.driver.save_screenshot(abs_save_path)
        return abs_save_path

    def End_selenium(self):
        self.driver.close()

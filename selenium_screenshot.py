import os
import time
import datetime
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
import chromedriver_binary
#import pyautogui as pg
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

class AutoWrite():
	def __init__(self,url:str,slug:str,mode=0):
		chromedriver_autoinstaller.install() 
		self.options = webdriver.ChromeOptions()
		self.options.use_chromium = True
		self.options.add_argument('--headless')
		self.driver = webdriver.Chrome(options=self.options)
		self.screenShot(url,slug,mode)
	def initialize_driver(self,user_agent: str):
		self.options.add_argument(f"user-agent={user_agent}")
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)


	def quit(self):
		self.driver.quit()

	def screenShot(self,url:str,slug:str,mode=0):
		#modeについて。0: PC,　1: タブレット,　2: スマホ
		user_agent = {
			0: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
			1: "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
			2: "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
		}[mode]
		window_sizes = {
				0: (1512, 824),
				1: (768, 1024),
				2: (375, 667)
		}
		window_width, window_height = window_sizes[mode]

		dt_now = datetime.datetime.now()
		dt_now_str = dt_now.strftime('%Y%m%d_%H%M%S')[2:]
		#screenshot/top/top_230803_221104.pngって感じで出力
		#引数slugはここのtopみたいなやつを入れる
		image_dir = "screenshot/" + slug + "/"
		image_file_png = "screenshot/" + slug + "/" + slug + "_" + dt_now_str + ".png"
		image_file_jpeg = "screenshot/" + slug + "/" + slug + "_" + dt_now_str + ".jpeg"
		self.initialize_driver(user_agent)
		self.driver.set_window_size(window_width, window_height)
		self.driver.get(url)
		time.sleep(1)
		self.driver.execute_script(f"document.body.style.width = '{window_width}px';")
		time.sleep(3)
		self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
		time.sleep(3)
		self.driver.execute_script('window.scrollTo(0, 0);')
		page_width = self.driver.execute_script('return document.body.scrollWidth')
		page_height = self.driver.execute_script('return document.body.scrollHeight')
		print(page_width, page_height)
		# フッターが読み込まれなかったので+150してる
		self.driver.set_window_size(page_width, page_height + 150)
		os.makedirs(image_dir, exist_ok=True)
		self.driver.save_screenshot(image_file_png)

		# Convert PNG to JPEG
		with Image.open(image_file_png) as img:
				rgb_img = img.convert('RGB')
				rgb_img.save(image_file_jpeg, 'JPEG')

		# Optionally, you can remove the PNG file after conversion
		os.remove(image_file_png)

		self.driver.quit


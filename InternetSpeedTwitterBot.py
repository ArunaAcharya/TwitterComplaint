import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


class InternetSpeedTwitterBot:

   def __init__(self):
      self.driver= webdriver.Chrome(service= Service(ChromeDriverManager().install()))
      self.down= 0
      self.up= 0

   def get_internet_speed(self):
      self.driver.get("https://www.speedtest.net/")
      self.driver.maximize_window()
      time.sleep(5)
      self.driver.find_element(By.CLASS_NAME,"start-text").click()
      time.sleep(60)
      self.speeds= self.driver.find_elements(By.CLASS_NAME,"result-data-large")
      for _ in self.speeds:
        self.down_speed = self.speeds[0].text
        self.up_speed= self.speeds[1].text

      self.driver.quit()



   def tweet_at_provider(self, username, password):
      self.driver.get("https://twitter.com/?lang=en")
      self.driver.maximize_window()
      time.sleep(3)
      self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
      time.sleep(10)
      self.sign_up= self.driver.find_element(By.LINK_TEXT,'Sign in')
      self.sign_up.click()
      time.sleep(4)
      self.username= self.driver.find_element(By.NAME,'text')
      self.username.send_keys(username)
      self.username.send_keys(Keys.RETURN)
      time.sleep(4)
      self.re_username = self.driver.find_element(By.NAME,'text')
      self.re_username.send_keys("ArunaAcharya7")
      self.re_username.send_keys(Keys.RETURN)
      time.sleep(3)
      self.password= self.driver.find_element(By.NAME,"password")
      self.password.send_keys(password)
      self.password.send_keys(Keys.RETURN)
      time.sleep(5)
      self.status= self.driver.find_element(By.CSS_SELECTOR,'.public-DraftStyleDefault-block')
      self.status.send_keys(f"Hey my internet provider why is my internet speed is {self.down_speed} and {self.up_speed} when i pay for 150down/10up? ")
      time.sleep(5)
      self.tweet= self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
      self.tweet.click()
      time.sleep(10)


      self.driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.set_window_position(0, 0)
driver.set_window_size(1024, 768)

driver.get("https://www.google.it")
driver.find_element_by_id('L2AGLb').click()
driver.find_element_by_name('q').send_keys('smart_edu unict')
driver.find_element_by_name('q').send_keys(Keys.ENTER)
driver.get("https://studenti.smartedu.unict.it/")

johnson_url = "68747470733a2f2f7777772e796f75747562652e636f6d2f77617463683f763d6451773477395767586351"

driver.get(bytes.fromhex(johnson_url).decode('utf-8'))
time.sleep(1)
driver.find_element_by_xpath("/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a").click()
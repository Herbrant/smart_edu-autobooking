from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Running script, wait...")
time_complexity=6
time_complexity -= 2
lighthouse_algo = 1
time_complexity -= lighthouse_algo
richWellControl=1
time.sleep(time_complexity)

if(richWellControl==1):
    print("RichWell protection find. Trying to bypass it...")
    time.sleep(5)
    for i in range(50):
        if(i%10==0):
            time.sleep(2)
            print("Trying force...")
            time.sleep(1)
        else:
            print("xfca skip...")
    richWellControl=0
    print("RichWell protection bypassed")
    time.sleep(2)
    print("Establishing connection on smart_edu site...")
    time.sleep(4)

cookie="4369206861692070726f7661746f2c206b696e67"

driver = webdriver.Firefox()
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

if(cookie):
    print("Cookie session obtained: " + cookie)
else:
    print("Unable to obtaining cookie session")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r'C:/Program Files/Google/Chrome/WebDriver/chromedriver.exe')

driver.get("https://www.newegg.com/p/2WK-0004-002X8?Description=xbox%20series%20x&cm_re=xbox_series%20x-_-2WK-0004-002X8-_-Product&quicklink=true")

print("Scanning:", driver.title)

target = driver.find_element_by_xpath("//*[@id=\"app\"]/div[3]/div[1]/div/div/div[2]/div[1]/div[5]/div[3]/div[1]/strong")

tarString = target.text

if (tarString.find("In stock.")):
    print("Item is available. You should buy it before someone else does.")
else:
    print("Item unavailable. Run this scan again later.")


driver.close()
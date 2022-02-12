from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

path = os.getenv("EXE_PATH")

driver = webdriver.Chrome(executable_path=r"{}".format(path))

driver.get("https://www.newegg.com/p/2WK-0004-002X8?Description=xbox%20series%20x&cm_re=xbox_series%20x-_-2WK-0004-002X8-_-Product&quicklink=true")

print("Scanning:", driver.title)

target = driver.find_element_by_id("app")

tarString = target.text

if (tarString.find("In stock.")):
    print("Item is available. You should buy it before someone else does.")
else:
    print("Item unavailable. Run this scan again later.")


driver.close()
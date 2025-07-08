from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import smtplib, ssl
import os
load_dotenv()

port = 465
destination = "https://www.newegg.com/p/2WK-0004-002X8?Description=xbox%20series%20x&cm_re=xbox_series%20x-_-2WK-0004-002X8-_-Product&quicklink=true"
sender_email = os.getenv("LOGIN_EMAIL")
auth = os.getenv("LOGIN_PASS")
receiver_email = os.getenv("TARGET_EMAIL")
message = """
Subject: ---SCAN RESULTS---

Scan complete. Item in stock at {}. Immediate acquisition recommended.

""".format(destination)

path = os.getenv("EXE_PATH")

context = ssl.create_default_context()

driver = webdriver.Chrome()

driver.get(destination)

print("Scanning:", driver.title)

target = driver.find_element(By.ID, "app")

tarString = target.text

if (tarString.find("In stock.")):
    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login(sender_email, auth)
    #     server.sendmail(sender_email, receiver_email, message)
    print("It's there! This worked, y'all!")
    
else:
    print("Item unavailable. Run this scan again later.")


driver.close()
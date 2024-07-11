from playwright.sync_api import sync_playwright
import time
import json
import sys
import os
login = os.environ["LOGIN"]

password = os.environ["PASSWORD"]

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
try:
    with open("cookies.json", "r") as f:
            cookies = json.loads(f.read())
            context.add_cookies(cookies)
except:
    pass

page = context.new_page()
page.goto("https://centrum24.pl")
page.wait_for_load_state("networkidle")

page.locator("#input_nik").fill(login)
page.locator("#okBtn2").click()
page.locator("#ordinarypin").fill(password)
page.locator("#okBtn2").click()

main_money = page.locator("#left-column > div:nth-child(1) > md-accounts-details-component > md-accounts-section > div > div.md-accounts-details-parent > div.md-carousel > div > div > md-single-account > div > div > div.md-account-amount-default-box > div > span")
secondary_money = page.locator("#left-column > div.md-widget-container-no-padding.top-border > md-goals > div > div.goals-container > div:nth-child(2) > div > div:nth-child(1) > div.goal-data > div.amount-container > div")
print("Main account: ", main_money.inner_text())
print("Secondary account: ", secondary_money.inner_text())
input(" ")
#get href of an a element #id17
logout = page.locator("#id17").get_attribute("href")
# url should look like this https://www.centrum24.pl/centrum24-web/multi/dashboard?x=-9Ius3HlEypDMSwpfozyLwGm3Mq4CUa5LLb6rRjkv0F6EEyD7bn1Eg
logout = logout.split("?")[1]
logout = "https://www.centrum24.pl/centrum24-web/multi/dashboard?" + logout
print(logout)
page.goto(logout)
time.sleep(5)
page.goto("https://centrum24.pl/")
input(" ")
with open("cookies.json", "w") as f:
    f.write(json.dumps(context.cookies()))
browser.close()
playwright.stop()

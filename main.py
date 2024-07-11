from playwright.sync_api import sync_playwright
import time
import json
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
time.sleep(10)


with open("cookies.json", "w") as f:
    f.write(json.dumps(context.cookies()))
browser.close()
playwright.stop()

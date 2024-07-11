from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=True)
page = browser.new_page()
page.goto("centrum24.pl")

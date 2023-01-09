import time
import pandas as pd  # Read Excel file 

# Automate web
from playwright.sync_api import sync_playwright

file = "teste.xlsx"
url = "https://docs.google.com/forms/d/e/1FAIpQLSfwDHPzx_gSxM7FP4yPWYybDJdqhJHhdpr6jKwdgoIW0BRh9w/viewform?vc=0&c=0&w=1&flr=0"

df = pd.read_excel(file)

# Read Excel rows
for index, row in df.iterrows():
    # "iterrows" creates a tuple with the row name and the content
    print("Index: " + str(index))
    print("Name: " + row["NOME"])
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # True = silent process, False = shows the window
        page = browser.new_page()
        page.goto(url)
        
        page.fill("#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input", row["NOME"])
        page.fill("#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input", str(row["TELEFONE"]))
        # page.fill("Copy selector", what do you want to write)

        page.click("#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
        browser.close()
        

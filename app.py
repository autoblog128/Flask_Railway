from flask import Flask
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def run_script():
    youtube_url = "https://ouo.io/frkMrF"
    
    # Configure Chrome options for headless mode
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    # Initialize WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(youtube_url)

    time.sleep(10)

    try:
        button1 = driver.find_element(By.XPATH, "//html/body/section/div/div/div/div/div/form/div/button")
        button1.click()
        time.sleep(10)

        button2 = driver.find_element(By.XPATH, "//html/body/section/div/div/div/div/div/form/button")
        button2.click()
        result = "Both buttons clicked successfully!"
    except Exception as e:
        result = f"Error clicking button: {e}"
    finally:
        driver.quit()

    return result

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
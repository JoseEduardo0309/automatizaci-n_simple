import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Inicializar driver de Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # 1) Ir a Google
        driver.get("https://www.google.com")
        time.sleep(2)

        # 2) Ir a Hybridge Education
        driver.get("https://hybridge.education")
        time.sleep(2)

        # 3) Ir a OpenAI
        driver.get("https://openai.com")
        time.sleep(2)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

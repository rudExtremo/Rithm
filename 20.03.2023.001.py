from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/")

elements = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".card:nth-child(1)")))
elements.click()

checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".show #item-1 > .text")))
checkbox.click()

home = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-icon-expand-close")))
home.click()

downloads = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-node:nth-child(3) .rct-collapse > .rct-icon")))
downloads.click()

word_file = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-node-leaf:nth-child(1) .rct-checkbox > .rct-icon")))
word_file.click()

message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#result")))
assert "wordFile" in message.text

print("Test case passed")

driver.quit()

# 用 Selenium 自動化瀏覽器（最像真人）
# 最推薦、最穩定、最少踩雷！
# 它會「真的開啟 Chrome」，像真人一樣做到：

# 自動輸入帳號密碼
# 自動點按鈕
# 自動選下拉選單
# 自動填表單
# 自動下載資料
# 自動爬動態網頁
#pip install selenium webdriver-manager

#1.自動登入網站（以示範用假網站）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://example.com/login")  # 你的網站登入頁

# 找到輸入欄位（用 name / id / xpath 都行）
email_box = driver.find_element(By.NAME, "email")
password_box = driver.find_element(By.NAME, "password")

email_box.send_keys("your_email@example.com")
password_box.send_keys("your_password")

# 點擊登入
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()

time.sleep(5)
print("登入完成！")

#2.範例：自動登入網站（以示範用假網站）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://example.com/login")  # 你的網站登入頁

# 找到輸入欄位（用 name / id / xpath 都行）
email_box = driver.find_element(By.NAME, "email")
password_box = driver.find_element(By.NAME, "password")

email_box.send_keys("your_email@example.com")
password_box.send_keys("your_password")

# 點擊登入
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()

time.sleep(5)
print("登入完成！")

#3.範例：自動填表單（輸入文字、勾選、選下拉）
driver.get("https://example.com/form")

driver.find_element(By.NAME, "username").send_keys("王小明")
driver.find_element(By.NAME, "age").send_keys("20")

# 勾選 checkbox
driver.find_element(By.ID, "agree").click()

# 選下拉
from selenium.webdriver.support.ui import Select
Select(driver.find_element(By.NAME, "city")).select_by_value("taipei")

# 送出
driver.find_element(By.XPATH, "//button[text()='送出']").click()

print("表單已送出！")
``
# -*- coding: utf-8 -*-
# author: itimor

# 导入 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC
import platform
from config import siteinfo


# 如果没有在环境变量指定PhantomJS位置
if platform.system() == 'Windows':
    driver = webdriver.Chrome(executable_path="windows/chromedriver")
    # 如果windows下需要phantomjs模式，现在在phantomjs到对应目录
    # driver = webdriver.PhantomJS(executable_path="windows/phantomjs")
else:
    driver = webdriver.PhantomJS(executable_path="linux/phantomjs")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get(siteinfo["url"])

# 等待加载
driver.implicitly_wait(5)  # seconds

# 关闭弹窗
try:
    driver.find_element_by_id("shut_down_alert").click()
except:
    pass

# 点击登录
driver.find_element_by_id("JD_sign").click()

# 等待加载
driver.implicitly_wait(5)  # seconds

# 获取登录表单
data = driver.find_element_by_class_name("login-form")

# 输入用户名密码
data.find_element_by_name("username").send_keys(siteinfo["username"])
data.find_element_by_name("password").send_keys(siteinfo["password"])

# 生成当前页面快照并保存
driver.save_screenshot("login.png")

# 点击登录
driver.find_element_by_id("login-btn2").click()

try:
    # 每隔10秒查找页面元素 id="myDynamicElement"，直到出现则返回
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "JD_sign"))
    )
    # 生成当前页面快照并保存
    driver.save_screenshot("before_sign.png")
    # 点击签到
    element.click()
except:
    print("already sign")
finally:
    # 等待加载
    driver.implicitly_wait(5)  # seconds
    # 生成签到页面快照并保存
    driver.save_screenshot("sign.png")
    driver.quit()

import time
from random import random
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 使用Service对象指定驱动程序的路径
from selenium.webdriver.edge.service import Service
service = Service("E:\edg\msedgedriver.exe")


driver = webdriver.Edge(service=service)

# 打开搜索引擎页面
driver.get("https://www.bing.com")

# 循环搜索33次
for i in range(50):
    # 定位搜索框并输入搜索关键词
    search_box = driver.find_element("name", "q")
    search_box.clear()  # 清空搜索框
    search_box.send_keys("自动化测试 当前时间：" + time.strftime("%Y-%m-%d %H:%M:%S"))  # 输入搜索关键词
    search_box.send_keys(Keys.RETURN)
    time_set = random.randint(9, 15)
    # 等待搜索结果加载完成
    time.sleep(time_set)  # 等待10秒

    # 打印搜索结果标题
    results = driver.find_elements("xpath", "//ol[@id='b_results']/li//h2/a")
    print("第", i+1, "次搜索结果：")
    for result in results:
        print(result.text)

    # 返回到搜索首页
    driver.get("https://www.bing.com")

# 关闭浏览器
driver.quit()


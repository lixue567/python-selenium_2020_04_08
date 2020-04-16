
from selenium import webdriver
import time
import os


user = "admin"
password = "CD123456"
bug_title = "返回服务器错误"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/biz/user-login.html")

driver.find_element_by_id("account").send_keys(user)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_id("submit").click()
time.sleep(1)

#进入到提交BUG界面
driver.find_element_by_xpath('//li[@data-id="qa"]').click()
driver.find_element_by_xpath('//li[@data-id="bug"]').click()
driver.find_element_by_xpath('//a[@class="btn btn-primary"]').click()

#开始提交BUG,选择所属产品
driver.find_element_by_xpath('//div[@id="product_chosen"]').click()
driver.find_element_by_xpath('//ul[@class="chosen-results"]/li[@title="物业管理系统"]').click()
#选择所属模块
driver.find_element_by_xpath('//div[@id="module_chosen"]').click()
driver.find_element_by_xpath('//ul[@class="chosen-results"]/li[@title="/登录"]').click()
#选择所属项目
driver.find_element_by_xpath('//div[@id="project_chosen"]').click()
driver.find_element_by_xpath('//ul[@class="chosen-results"]/li[@title="门禁管理系统"]').click()
time.sleep(1)
#选择影响版本
driver.find_element_by_xpath('//div[@id="openedBuild_chosen"]').click()
driver.find_element_by_xpath('//div[@id="openedBuild_chosen"]/div/ul/li[@title="V1.2.3"]').click()
#选择当前指派
driver.find_element_by_xpath('//span[@class="input-group-btn"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//div[@id="assignedTo_chosen"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@id="assignedTo_chosen"]/div/ul/li[@title="W:王伟"]').click()
#选择截止日期
driver.find_element_by_xpath('//input[@id="deadline"]').send_keys("2020-5-11")
#选择BUG类型
driver.find_element_by_xpath('//div[@id="type_chosen"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@id="type_chosen"]/div/ul/li[@title="设计缺陷"]').click()
#选择操作系统
driver.find_element_by_xpath('//div[@id="os_chosen"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@id="os_chosen"]/div/ul/li[@title="Windows 10"]').click()
#选择浏览器
driver.find_element_by_xpath('//div[@id="browser_chosen"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@id="browser_chosen"]/div/ul/li[@title="chrome"]').click()
#BUG标题
driver.find_element_by_xpath('//input[@id="title"]').send_keys(bug_title)
#选择严重程度

driver.find_element_by_xpath('//div[@data-type="severity"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@data-type="severity"]/div/div/span[@data-value="2"]').click()
#选择优先级
driver.find_element_by_xpath('//div[@data-type="pri"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@data-type="pri"]/div/div/span[@data-value="2"]').click()
#重现步骤
edit = driver.find_element_by_xpath('//iframe[@class="ke-edit-iframe"]')
driver.switch_to.frame(edit)
driver.find_element_by_xpath('//body[@class="article-content"]').clear()
driver.find_element_by_xpath('//body[@class="article-content"]').send_keys("<p>[步骤]</p>'登录系统'<br><p>[结果]</p>'登录失败'<br><p>[期望]</p>'登录成功'")
driver.switch_to.default_content()
#关键词
driver.find_element_by_xpath('//input[@id="keywords"]').send_keys("登录")
driver.find_element_by_xpath('//button[@class="btn btn-wide btn-primary"]').click()
time.sleep(5)
#登出
driver.find_element_by_xpath('//a[@class="dropdown-toggle"]').click()
time.sleep(1)
driver.find_element_by_xpath('//ul[@id="userNav"]/li/ul/li[13]/a').click()

driver.quit()
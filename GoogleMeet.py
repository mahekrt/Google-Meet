from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=opt,executable_path="C:\Program Files (x86)\chromedriver.exe")
driver.get("https://accounts.google.com/AccountChooser/identifier?continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=AddSession")


username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.click()
username.send_keys("2018.mahek.tardeja@ves.ac.in")

next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()
time.sleep(5)


password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('Mahek@123')


next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()
time.sleep(5)

classroom = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]')
classroom.click()
time.sleep(5)

link = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/span/a/div')
link.click()
time.sleep(10)

current_tab = driver.window_handles[1]
driver.switch_to_window(current_tab)
time.sleep(15)

camera = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div')
camera.click()

mic = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div')
mic.click()

join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join.click()


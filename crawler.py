from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# this is a path to the Chrome web driver on your system
webdriver_path = "C:\\Users\\hssak\\Downloads\\chromedriver_win32\\chromedriver.exe"

# add headless browser option
options = Options()
options.headless = True
driver = webdriver.Chrome(webdriver_path)
driver.set_window_size(100, 100)
test_url = "https://en.wikipedia.org/wiki/Nepal"

driver.get(test_url)
links = driver.find_elements_by_tag_name('a')
print(driver.page_source)



# opening
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    #x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_id("robotsRule")
    radiobox.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


#####Screncapture evidencia captura de pantalla
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def test_windows_interaction():
  driver = webdriver.Chrome()

  driver.get("https://testautomationpractice.blogspot.com/")

  driver.save_screenshot('./imagen3.png')

#####Screncapture evidencia captura de pantalla
#from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#def test_windows_interaction():
#   driver = webdriver.Chrome()

#   driver.get("https://testautomationpractice.blogspot.com/")

#   driver.save_screenshot('./imagen3.png')

#WINDOWS

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#import time

#def test_windows_interaction():
    #   driver = webdriver.Chrome()

    #  driver.get("https://testautomationpractice.blogspot.com/")

    # print(driver.current_window_handle)
    # print(len(driver.window_handles))

    # driver.find_element(By.XPATH, "//*[@class = 'feed-link' and text() = 'Posts (Atom)']").click()
    # print(len(driver.window_handles))

    #driver.switch_to.new_window("tab")
    #   print(len(driver.window_handles))
    driver.close()

    #   driver.switch_to.window(driver.window_handles[1])

    # time.sleep(3)
    # driver.set_window_size(1024, 768)
    #   time.sleep(3)
    #driver.maximize_window()
    #driver.minimize_window()

    #crea nueva ventana

    #  driver.switch_to.new_window('window')
    #    time.sleep(4)

#Buscando elementos en iframe

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#import time

#def test_element_iframe():
    #   driver = webdriver.Chrome()

    #driver.get("https://testautomationpractice.blogspot.com/")

    #my_iframe = driver.find_element(By.ID, "frame-one1434677811")
    #driver.switch_to.frame(my_iframe)
    #web_element = driver.find_element(By.ID, "RESULT_TextField-1")
    #web_element.send_keys("Noel")

    #time.sleep(4)

    # ALERTAS

    #from selenium import webdriver
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.common.alert import Alert
    #import time

    #def test_cookies_browser():
        #driver = webdriver.Chrome()

        # driver.get("https://testautomationpractice.blogspot.com/")

        #print("COOKIES: ", driver.get_cookies())

        #driver.add_cookie({"name": "udemy", "value": "cookies browser"})

        #print("COOKIES: ", driver.get_cookies())

        # driver.delete_cookie("udemy")

       # print("COOKIES: ", driver.delete_cookie("udemy"))

#Cooekies

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.alert import Alert
#import time

#def test_alertas_browser():
    #driver = webdriver.Chrome()

    #driver.get("https://testautomationpractice.blogspot.com/")

    #driver.find_element(By.XPATH, "//*[text()='Click Me']").click()

    #alert = Alert(driver)
    #texto = alert.text
    #print("Texto de la Alerta: ", texto)

    #alert.accept()
    #assert driver.find_element(By.ID, "demo").text=="You pressed OK!"

    #time.sleep(4)


#Navegacion
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time


#def test_navegacion_browser():
    #   driver = webdriver.Chrome()
    #driver.get("https://nytimes.com/")
    #print("Url Actua    l: ", driver.current_url)

    #driver.find_element(By.LINK_TEXT, "Science").click()
    #print("Url Actual: ", driver.current_url)

    #driver.back()
    #print("Url Actual: ", driver.current_url)

    #driver.forward()
    #print("Url Actual: ", driver.current_url)

    #driver.refresh()
    #print("Url Actual: ", driver.current_url)

    #time.sleep(4)


# Dgar and DROP
#from selenium import webdriver
#from selenium.webdriver.common.by import By
# import time


# def test_drag_and_drop():
    # driver = webdriver.Chrome()
    # driver.get("https://testautomationpractice.blogspot.com/")

    # source = driver.find_element(By.XPATH, "//*[@class='ui-widget-header' and text() = 'Mr John']")
    # target = driver.find_element(By.ID, 'trash')

    # action = ActionChains(driver)

    # action.drag_and_drop(source, target).perform()

    #  time.sleep(4)

# COMBOBOX
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# def test_combobox():
#   driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")

# time.sleep(4)
# select_file = Select(driver.find_element(By.NAME, 'files'))
# select_file.select_by_value('3')

# time.sleep(4)

# select_file.select_by_visible_text('Other file')

# time.sleep(4)

# COMBOBOX
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# def test_combobox():
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")

# time.sleep(4)
# select_file = Select(driver.find_element(By.NAME, 'files'))
# select_file.select_by_value('3')

# time.sleep(4)


# CALENDARIO
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_calendario():
#   driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")

# calendario = driver.find_element(By.ID, 'datepicker')
# calendario.click()

# time.sleep(4)

# driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text()='23']").click()
# time.sleep(3)
# driver.find_element(By.ID, 'datepicker').click()
# time.sleep(3)
# calendario.click()
# driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text()='14']").click()
# time.sleep(3)

# calendario.clear()
# calendario.send_keys('01/01/2001')

# time.sleep(5)

# CALENDARIO
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_calendario():
#   driver = webdriver.Chrome()
#
# driver.get("https://testautomationpractice.blogspot.com/")

# driver.find_element(By.ID, 'datepicker').click()

# time.sleep(4)

# driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text()='23']").click()
# time.sleep(3)
# driver.find_element(By.ID, 'datepicker').click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text()='14']").click()
# time.sleep(3)


# Checkbox
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_textbox_interaction():
#   driver = webdriver.Chrome()

# driver.get("https://testautomationpractice.blogspot.com/")

# frame_element = driver.find_element(By.ID, "frame-one1434677811")
# driver.switch_to.frame(frame_element)

# checkbox = driver.find_element(By.NAME, 'RESULT_CheckBox-8')
# driver.execute_script("arguments[0].scrollIntoView();", checkbox)

# time.sleep(3)
# driver.execute_script("arguments[0].click();", checkbox)
# time.sleep(3)

# print("Tipo de elemento: ", checkbox.get_attribute('type'))
# print("Seleccionado despues del click: ", checkbox.is_selected())


# TEXBOX
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_textbox_interaction():
# driver = webdriver.Chrome()

# driver.get("https://testautomationpractice.blogspot.com/")

# frame_element = driver.find_element(By.ID, "frame-one1434677811")
# driver.switch_to.frame(frame_element)

# textbox = driver.find_element(By.NAME, 'RESULT_TextField-1')
# time.sleep(3)
# textbox.send_keys("Noel")
# time.sleep(3)
# textbox.clear()
# time.sleep(3)
# textbox.send_keys("Hola de nuevo")
# time.sleep(3)
# actual_value = textbox.get_attribute('value')

# print(actual_value)


# Utilizando XPATH
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_element_by_id():
#   driver = webdriver.Chrome()
#   driver.get('https://testautomationpractice.blogspot.com/')
#
#   my_iframe = driver.find_element(By.ID, "frame-one1434677811")
#   driver.switch_to.frame(my_iframe)
#
#   web_element = driver.find_element(By.XPATH, "/html/body/form/div[2]/div[4]/input")
#   web_element.send_keys("Noel")
#
#   time.sleep(4)

# ID
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_element_by_id():
#   driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')

# web_element = driver.find_element(By.ID, "field2").send_keys('Noel')

# time.sleep(10)

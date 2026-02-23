from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):
  driver.get(f"https://www.google.com/search?q=temperatura+actual+en+{consulta}")
  try:
    temperatura = driver.find_element(By.CSS_SELECTOR, "span#wob_tm").text
    descripcion = driver.find_element(By.CSS_SELECTOR, "span#wob_dc").text
    return f"El clima en {consulta}: {temperatura}C, {descripcion}."
  except Exception as e:
    return "No se pudo obtener el clima en este momento."

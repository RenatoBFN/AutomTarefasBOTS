# bibliotecas
import pyautogui
import time

pyautogui.PAUSE = 2 # executar a próxima tarefa em 02 segundos
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 01 - Entrar no sistema;
# Abrir o navegador - windows/chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# 02 - Realizar o login;
pyautogui.write(link)
pyautogui.press("enter")

# uma pausa para carregar o site
time.sleep(2)

pyautogui.click(x=-1544, y=514)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.click(x=-1202, y=720)

# uma pausa para carregar o site
time.sleep(2)

# 03 - Abrir a base de dados;







# 04 - Cadastrar o produto;
# 05 - Repetir o passo anterior até o fim da lista.
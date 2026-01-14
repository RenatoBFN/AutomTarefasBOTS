# bibliotecas
import time
import pyautogui
import pandas

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
produtos_xml = pandas.read_csv("produtos.csv")

# 04 - Cadastrar produtos
for linha in produtos_xml.index:
    pyautogui.click(x=-1555, y=374)
    codigo =  str(produtos_xml.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(produtos_xml.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(produtos_xml.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(produtos_xml.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(produtos_xml.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(produtos_xml.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(produtos_xml.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.click(x=-1355, y=1184)

'''
    pyautogui.scroll(5000)
'''
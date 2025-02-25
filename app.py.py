import pyautogui
import time
import os

# Abrir o Chrome
os.system('start chrome') 

# Aguarda o Chrome abrir
time.sleep(2)

# Maximiza a janela do Chrome
pyautogui.hotkey('win', 'up') 

# Aguarda a janela ser maximizada
time.sleep(1)

# Seleciona a barra de pesquisa do Chrome (Ctrl + L seleciona a barra de endereço)
pyautogui.hotkey('ctrl', 'l')

# Digita o endereço do Linkedin
pyautogui.write('https://www.linkedin.com/feed/', interval=0.1)

# Pressiona enter
pyautogui.press('enter')

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona a aba de rede  
pyautogui.click(800, 100)   

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona conexão com a primeira recomendação
pyautogui.click(700, 700)  

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona conexão com a segunda recomendação
pyautogui.click(900, 700) 

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona conexão com a terceira recomendação
pyautogui.click(1100, 700)  

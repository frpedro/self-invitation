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

# Foca na barra de pesquisa do Chrome (Ctrl + L seleciona a barra de endereços)
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

# Pressiona primeira recomendação de conexão
pyautogui.click(700, 700)  

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona segunda recomendação de conexão
pyautogui.click(900, 700) 

# Aguarda a janela ser maximizada
time.sleep(3)

# Pressiona terceira recomendação de conexão
pyautogui.click(1100, 700)  

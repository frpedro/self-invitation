## LinkedIn Connection Inviter
Este projeto é um script de automação em Python desenvolvido para testar a biblioteca pyautogui. Ele envia automaticamente convites de conexão para as pessoas recomendadas pelo LinkedIn.

⚠️ Observação: Este projeto é apenas para fins educacionais e de teste. O uso de automações no LinkedIn pode violar os termos de uso da plataforma.

# Funcionalidades
Abre o Google Chrome automaticamente.
Acessa a página inicial do LinkedIn.
Navega até a seção de recomendações de conexão.
Envia convites de conexão automaticamente para três recomendações.
# Pré-requisitos
Python 3.x instalado
Biblioteca pyautogui
Você pode instalar com o comando:
bash
Copiar
Editar
pip install pyautogui
# Como usar
Clone o repositório ou copie o código.
Certifique-se de que o navegador Google Chrome esteja instalado.
Execute o script com:
bash
Copiar
Editar
python linkedin_inviter.py
Não mova o mouse ou pressione teclas enquanto o script estiver rodando.
# Observações
As coordenadas dos cliques (pyautogui.click(x, y)) podem variar dependendo da resolução da tela e do layout do LinkedIn. Você pode ajustar as posições usando:

-python
-Copiar
-Editar
-pyautogui.displayMousePosition()
-para encontrar as coordenadas corretas.

O script é básico e pode ser melhorado com detecção automática de botões, usando bibliotecas como opencv ou reconhecimento de imagens.
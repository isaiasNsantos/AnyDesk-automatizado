import pyautogui
import time
from getpass import getpass



pyautogui.PAUSE = 1

print('''
░█████╗░███╗░░██╗██╗░░░██╗░░░░░░██████╗░███████╗░██████╗██╗░░██╗
██╔══██╗████╗░██║╚██╗░██╔╝░░░░░░██╔══██╗██╔════╝██╔════╝██║░██╔╝
███████║██╔██╗██║░╚████╔╝░█████╗██║░░██║█████╗░░╚█████╗░█████═╝░
██╔══██║██║╚████║░░╚██╔╝░░╚════╝██║░░██║██╔══╝░░░╚═══██╗██╔═██╗░
██║░░██║██║░╚███║░░░██║░░░░░░░░░██████╔╝███████╗██████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░░░░░░╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝      
      ''')
print('Carregando.....')
time.sleep(1)
i_d = input('Digite o ID: ')
time.sleep(1)
print('Processando....')
senha = getpass('Digite a senha: ')# deixando a senha invisivel

# Abrir o app AnyDesk
pyautogui.press('win') # função press - aperta algo no teclado de acordo com o que vc escolher ('windows')
pyautogui.write('AnyDesk') # função write - digite o que vc quer entre aspas ('Anydesk)
# time.sleep(2)
pyautogui.press('enter')
pyautogui.click(x=62, y=68)
pyautogui.write(i_d)  
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(senha)
pyautogui.press('enter')

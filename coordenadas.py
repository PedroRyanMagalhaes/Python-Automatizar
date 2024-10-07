import pyautogui
import time

print("Posicione o mouse sobre o local desejado e aguarde 5 segundos...")
time.sleep(5)  # Tempo para você posicionar o mouse
x, y = pyautogui.position()  # Obtém a posição atual do mouse
print(f"Coordenadas: ({x}, {y})")
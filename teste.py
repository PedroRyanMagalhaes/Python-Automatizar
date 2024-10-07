import pyautogui
import time

# Espera um tempo para você posicionar o Paint na tela
print("Posicione o Paint e aguarde 5 segundos...")
time.sleep(5)

# Altera para a janela do Paint
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

# Clica na posição onde você deseja começar a desenhar
pyautogui.click(631, 102)  # Ajuste as coordenadas conforme necessário

# Aguarda um pouco para garantir que o clique foi registrado
time.sleep(0.5)

# Pressiona o botão do mouse para começar a desenhar
pyautogui.mouseDown()

# Move o mouse para desenhar a bolinha
# Para um círculo pequeno, você pode usar um pequeno deslocamento
pyautogui.move(50, 0)  # Move 50 pixels para a direita
pyautogui.drag(0, 50, duration=0.5)  # Desce 50 pixels (cerca de meio círculo)
pyautogui.drag(-50, 0, duration=0.5)  # Move para a esquerda (finalizando o círculo)
pyautogui.drag(0, -50, duration=0.5)  # Sobe 50 pixels (fechando o círculo)

# Solta o botão do mouse para parar de desenhar
pyautogui.mouseUp()

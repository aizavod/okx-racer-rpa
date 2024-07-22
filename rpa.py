import pyautogui
import time
import random
import pyscreeze
# Путь к изображению кнопки
DOOM_PATH = 'static/doom.png'
MOON_PATH = 'static/moon.png'
N_SLEEP = 8  # Задержка между кликами

while True:
    # Поиск изображения кнопки на экране
    button_image_path = random.choice([DOOM_PATH, MOON_PATH])
    button_locations = []
    try:
        button_locations = list(pyautogui.locateAllOnScreen(button_image_path))
    except (pyautogui.ImageNotFoundException, pyscreeze.ImageNotFoundException):
        print(f"Изображение {button_image_path} не найдено")
        time.sleep(N_SLEEP)
        continue
    except KeyboardInterrupt:
        print("Выход из программы")
        break

    for button_location in button_locations:
        # Кликаем по центру каждой найденной кнопки
        button_center = pyautogui.center(button_location)
        pyautogui.click(button_center)
        time.sleep(0.01)  # Задержка в 0.01 секунды между кликами
    
    time.sleep(N_SLEEP)  # Подождать 10 секунд перед следующей попыткой

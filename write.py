import time
import pyautogui

def type_text_from_file(file_path, typing_delay=0.1):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        pyautogui.typewrite(line.strip())
        time.sleep(typing_delay)
        pyautogui.press('enter')
        time.sleep(typing_delay)

if __name__ == "__main__":
    file_path = "your_text_file.txt" 
    typing_delay = 1 
    type_text_from_file(file_path, typing_delay)

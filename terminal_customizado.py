import time
import os
from tqdm  import tqdm
from pyfiglet import Figlet

def loading():
    for _ in tqdm(range(100), desc="Carregando...",ascii=False,ncols=75):
        time.sleep(0.1)
    print("Loading Done!")

def font(text):

    cool_text=Figlet(font="doom")
    return str(cool_text.renderText(text))

def window_size(colums=750, height=30):
    os.system("cls")
    os.system(f'mode con: cols={colums} lines={height}')

if __name__ == "__main__":
    window_size(80,20)
    print(font("Sistema de Estoque!"))
    loading()
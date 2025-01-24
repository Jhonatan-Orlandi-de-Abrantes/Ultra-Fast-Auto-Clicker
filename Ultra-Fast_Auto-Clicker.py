import customtkinter as ctk, threading as thr
from time import sleep
from mouse import click
from keyboard import wait
from sys import exit

janela = ctk.CTk()
janela.title('Ultra-Fast Auto-Clicker')
janela.geometry('200x100')
janela.resizable(width=False, height=False)
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

key = 'F8'
confirm = False

def sair_programa():
    exit()

janela.protocol("WM_DELETE_WINDOW", sair_programa)

def toggle():
    global confirm, botao
    
    if confirm == False:
        for i in range(1, 0, -1):
            botao.configure(text=str(i))
            sleep(1)
        botao.configure(text=f'Start/Stop ({key})')
        
        confirm = True
        
        
        while confirm == True:
            click('left')
            sleep(0.01)
    
    else:
        confirm = False
        botao.configure(text=f'Start/Stop ({key})')

def toggle_thread():
    thread = thr.Thread(target=toggle)
    thread.start()

def tecla_para_clicks():
    while True:
        wait(key)
        toggle_thread()

def tecla_para_clicks_thread():
    thread = thr.Thread(target=tecla_para_clicks)
    thread.daemon = True
    thread.start()

tecla_para_clicks_thread()

space = ctk.CTkLabel(janela, text=None).pack()
frame = ctk.CTkFrame(janela, width=180, height=80).place(x=10, y=10)
botao = ctk.CTkButton(janela, text=f'Start/Stop ({key})', font=('',18), command=toggle_thread)
botao.pack(ipady=8)

janela.mainloop()
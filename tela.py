from typing import Sized, Text
from PySimpleGUI import PySimpleGUI as sg
from PIL import Image
import json

def inicial():
    sg.theme('Topanga')
    layout = [
    [sg.Button('Login', size=(20,1))],[sg.Button('Nova Conta', size=(20,1))]
    ]
    janela = sg.Window('Tela', layout, finalize=True)
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Login':
            login()
            inicial().hide()      
        if eventos == 'Nova Conta':
            singup()
            inicial.hide()
        break 
            

def singup():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Criar Usuário'),sg.Input(key='newuser', size=(20,1))],
    [sg.Text('Criar Senha  '),sg.Input(key='newpass', size=(20,1))],
    [sg.Text('\n')],
    [sg.Button('Criar Conta')]
    ]
    janela = sg.Window('Tela', layout, finalize=True)
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        ler = json.load(open('bancodedados.json','r'))
        ler['banco_de_dados'].append({
            'user' : valores['newuser'],
            'senha' : valores['newpass']
        })
        json.dump(ler,open('bancodedados.json','w'),indent=2)
        
        

        
def login():
    # layout
    sg.theme('Topanga')
    layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha  '),sg.Input(key='senha',password_char='*', size=(20,1))],
    [sg.Text('\n')],
    [sg.Button('Entrar')]
    ]
    # janela
    janela = sg.Window('Tela', layout, finalize=True)
    # Ler os eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            with open('bancodedados.json','r+') as f:
                ler = json.load(f)
                bancodedados = ler['banco_de_dados']
                for i in bancodedados:
                    if valores['usuario'] == i['user'] and valores['senha'] == i['senha']:
                        Image.open('bem-vindo.jpg').show()


inicial()

        




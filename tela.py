from tkinter import Button
from tkinter.constants import N
from typing import Sized, Text
from PySimpleGUI import PySimpleGUI as sg
from PIL import Image
import json

def win_inicial():
    sg.theme('Topanga')
    layout = [
    [sg.Button('Login', size=(20,1))],[sg.Button('Nova Conta', size=(20,1))]
    ]
    return sg.Window('Tela', layout, finalize=True)
            
def win_singup():
    sg.theme('Topanga')
    layout = [
    [sg.Text('Criar Usuário  ')],
    [sg.Input(key='newuser', size=(20,1))],
    [sg.Text('Criar Senha   ')],
    [sg.Input(key='newpass',password_char='*',size=(20,1))],
    [sg.Text('Repita Senha ')],
    [sg.Input(key='confpass',password_char='*',size=(20,1))],
    #[sg.Text('\n')],
    [sg.Button('Voltar'),sg.Button('Criar Conta')]
    ]
    return sg.Window('Tela', layout, finalize=True)

def win_login():
    # layout
    sg.theme('Topanga')
    layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha')],
    [sg.Input(key='senha',password_char='*', size=(20,1))],
    #[sg.Text('\n')],
    [sg.Button('Voltar'),sg.Button('Entrar')]
    ]
    return sg.Window('Tela', layout, finalize=True)

def win_on(user):
    sg.theme('Topanga')
    layout = [
    [sg.Text('Bem-vindo(a) '+user+'!')]
    ]
    return sg.Window('Tela',layout, finalize=True)

    def win_cpass():
        sg.theme('Topanga')
        layout = [
        [sg.Text('Senha antiga ')], 
        [sg.Input(key='oldpass', size=(20,1))],
        [sg.Text('Senha nova   ')],
        [sg.Input(key='newpass', size=(20,1))],
        [sg.Text('Repita a senha nova')],
        [sg.Input(key='confnewpass', size=(20,1))],
        [sg.Button('Voltar'),sg.Button('Confirmar')]
        ]

inicial, login, singup, on = win_inicial(), None, None, None

while True:
    
    window, event, value = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        break
    if window == inicial and event == 'Login':
        login = win_login()
        inicial.hide()
    if window == login and event == 'Entrar':        
        
        def verificar():
            with open('bancodedados.json','r+') as f:
                ler = json.load(f)
                bancodedados = ler['banco_de_dados']
                for i in bancodedados:
                    if value['usuario'] == i['user'] and value['senha'] == i['senha']:
                        return True
        if verificar():
            on = win_on(value['usuario'])
        else:
            sg.popup('O Usuário não existe ou a senha está incorreta.')
    
    if window == login and event == 'Voltar':
        login.hide()
        inicial.un_hide()
    if window == inicial and event == 'Nova Conta':
        singup = win_singup()
        inicial.hide()
    if window == singup and event == 'Criar Conta':
        
        def verificar():    
            with open('bancodedados.json','r+') as f:
                ler = json.load(f)
                bancodedados = ler['banco_de_dados']
                for i in bancodedados:
                    if value['newuser'] and value['newpass'] == '':
                        return 0
                    if value['newuser'] == i['user']:
                        return 1
                    if value['newuser'] == '':
                        return 2
                    if value['newpass'] == '':
                        return 3
        if len(value['newuser']) > 11:
            sg.popup('Usuário deve conter no máximo 10 carácteres')
            break
        #if verificar() == 0:
        #    sg.popup('Usuário e senha não inseridos')
        #    break
        #elif verificar() == 1:
        #    break
        elif verificar() == 2:
            sg.popup('Usuário não inserido')
            break
        #elif verificar() == 3:
        #    sg.popup('Senha não inserida')
        #    break
        else:       
            if value['newpass'] == value['confpass']:   
                ler = json.load(open('bancodedados.json','r'))
                ler['banco_de_dados'].append({
                    'user' : value['newuser'],
                    'senha' : value['newpass']
                })
                json.dump(ler,open('bancodedados.json','w'),indent=2)
                break
            else:
                sg.popup('Senha de confirmação incorreta.')
                inicial
    if window == singup and event == 'Voltar':
        singup.hide()
        inicial.un_hide()

        





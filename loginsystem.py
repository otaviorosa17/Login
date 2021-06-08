from datetime import datetime

import json

def displaymenu():
    status = input ('\n\nVocê já está cadastrado?\n\n')
    if status in ['sim','SIM','Sim',]:
        usuarioexistente()
    elif status in ['não','nao','Não','NÃO','NAO']:
        cadastro()

def cadastro():
    senha = input('\n\nDigite a senha para criar uma conta em nosso sistema.\n\n')
    if senha == 'senha':
        novousuario()

def verificarusuario(usuario,senha = None):
    with open('usuarios.json','r+') as f:
        usuarios = json.load(f)
        lista_usuarios = usuarios['lista_usuarios']
        for user in lista_usuarios:
            if senha:
                if usuario == user['usuario'] and senha == user['senha']:
                    return True
            else: 
                if usuario == user['usuario']:
                    return True

def bancodedados():
    senhamaster = input('\n\nAtive o modo administrador para ver os dados do sistema.\n\n\n')
    if senhamaster == '123':
        print('\n\nModo administrador ativado!')
        with open('usuarios.json','r') as f:
            print('\n')
            dados = json.load(f)
            [print(f'\n\n\n\nusuário: {item["usuario"]}\nsenha: {item["senha"]}\ncriado em: ({item["hora_criacao"]})') for item in dados["lista_usuarios"]]
            # print(json.dumps(dados['lista_usuarios'],indent=2))
            
def novousuario():
    criarnome = input ('Crie o seu nome de Usuário: ')
    
    if verificarusuario(criarnome):
        print ('\n\nEste nome já foi registrado\n\n')
    else:
        criarsenha = input ('Criar a sua senha: ')
        criarhorario = horario()
        print('\nUsuário criado!\n')
        usuarios = json.load(open('usuarios.json','r'))
        usuarios['lista_usuarios'].append({
            'usuario' : criarnome,
            'senha' : criarsenha,
            'hora_criacao' : criarhorario
        })
        json.dump(usuarios,open('usuarios.json','w'),indent=2)

        # with open('usuarios.txt','a') as f:
        #     f.write(f'{criarnome} {DIVISOR} {criarsenha} {DIVISOR} \n')


   
def trocar_senha(senha):
        senha_nova = input('Senha nova: ')
        lista = json.load(open('usuarios.json','r+'))['lista_usuarios']
        def index():
            for i,val in enumerate(lista):
                if val['senha'] == senha:
                    # return i
                    val['senha'] = senha_nova
        index()
        # lista[[index()]] = senha_nova 
        json.dump(lista,open('usuarios.json','w'),indent=2)
                
            



def usuarioexistente():
    usuarioinserido = None
    senhainserida = None
    while not senhainserida or not usuarioinserido:
        usuarioinserido = input('\n\nDigite seu Usuário: ')
        senhainserida = input('Digite sua senha: ')
    usuariovalido = verificarusuario(usuarioinserido,senhainserida)
    
    if usuariovalido:
        print('\n\nAcesso Concedido!\n\n')
        print('Bem-vindo(a) '+usuarioinserido+'!')
        condicao = input('\n\nDigite \'trocar\' para trocar de senha\n\n')
        if condicao == 'trocar':
            trocar_senha(senhainserida)
            print('\n\nSenha trocada com sucesso!\n\n') 
        else:  
            bancodedados()
    else:
        print('\n\nO Usuário não exite ou a senha está errada.\n\n')


def horario():
    agora = datetime.now().strftime("%d-%m-%Y às %H:%M:%S")
    return agora

displaymenu()
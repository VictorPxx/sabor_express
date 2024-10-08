import os

restaurantes = [{'nome': 'Cantina Ditalia', 'categoria': 'Pizzaria', 'ativo': False},
                {'nome': 'Avenida', 'categoria': 'Lanchonete', 'ativo': True},
                {'nome': 'Tekai', 'categoria': 'Japonesa', 'ativo': True}]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('''
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀

    ''')
    
def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')
    
def escolher_opcoes():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_opcao()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternando_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_opcao():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastramento de restaurantes')
    nome_do_restaurante = input('Insira o nome do restaurante a ser cadastrado: ')
    categoria_do_restaurante = input('Insira o nome da categoria do restaurante: ')
    dados_do_cadastro = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_cadastro)
    print(f'\nO restaurante {nome_do_restaurante.upper()} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(24)} {'Categoria'.ljust(22)} Status')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Desativo'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_ao_menu_principal()
    
def alternando_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    restaurante_escolhido = input('Insira o nome do restaurante que deseja ativar/desativar')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante_escolhido == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante_escolhido} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante_escolhido} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado ')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print()
    input('Escolha qualquer tecla para voltar ao menu principal ')
    main()
    
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    ''' 
    linha = '*' * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizando app')
      
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida\n')
    voltar_ao_menu_principal()    
    
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
import json
import os.path

def cabecalho(msg):
    print('-'*30)
    print(f'{msg}'.center(30))


def menu_principal(lista):
        print('-'*30)
        for posicao,item in enumerate(lista):
            print(f'{posicao + 1} - {item}')
        return '-'*30


def validacao_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if opcao <= 0 or opcao >= 5:
                print('ERRO! Digite uma opção válida!')
            else:
                return opcao
        except ValueError:
            print('ERRO: por favor, digite um número inteiro válido.')




def criar_cadastro(opcao_usuario, lista_definitiva):
    import json
    if opcao_usuario == 1:
        cabecalho('Pessoas cadastradas:')
        if not os.path.exists('arquivo_lista.txt') or os.path.getsize('arquivo_lista.txt') ==0:
            print('Nenhum dado disponível.')
            return

        with open('arquivo_lista.txt', 'r') as arquivo:
            conteudo = json.load(arquivo)
            if not conteudo:
                print('-'*30)
                print('Não há ninguem cadastrado!')
            else:
                print(f'{'nome':<15}{'idade':>10}')
                print('='*30)
                for nome, idade in conteudo:
                    print(f'{nome:<15}{idade:>10}')

    if opcao_usuario == 2:
        lista_temp = list()
        print('-'*30)
        lista_temp.append(input('Nome: '))
        while True:
            try:
                lista_temp.append(int(input('Idade: ')))
                break
            except ValueError:
                print('ERRO! Digite um número inteiro válido!')

        lista_definitiva.append(lista_temp)
        with open('arquivo_lista.txt', 'w') as arquivo2:
            json.dump(lista_definitiva, arquivo2)

    if opcao_usuario == 3:
        if not os.path.exists('arquivo_lista.txt') or os.path.getsize('arquivo_lista.txt') == 0:
            print('Nenhum dado disponível.')
            return

        else:
            with open('arquivo_lista.txt', 'r') as arquivo:
                try:
                    dados_salvos = json.load(arquivo)
                except json.JSONDecodeError:
                    print('Erro ao ler o arquivo.')
                    return

        lista_definitiva.clear()
        lista_definitiva.extend(dados_salvos)

        print(f'{"indice":<15}', f'{"nome":<15}')
        print('-'*20)
        for indice, pessoa in enumerate(lista_definitiva):
            print(f'{indice:<15}',f'{pessoa[0]:<15}')
        try:
            remover = int(input('Digite o índice para remover a pessoa correspondente:'))
            if 0 <= remover < len(lista_definitiva):
                pessoa_removida= lista_definitiva.pop(remover)
                print(f'Pessoa removida: {pessoa_removida[0]}')

                with open('arquivo_lista.txt', 'w') as arquivo:
                    json.dump(lista_definitiva, arquivo)
            else:
                print('Índice inválido.')
        except ValueError:
             print('Digite um número inteiro válido.')

    if opcao_usuario == 4:
        return lista_definitiva



def cadastro():
    lista_definitiva = list()

    if os.path.exists('arquivo_lista.txt'):
        if os.path.getsize('arquivo_lista.txt') > 0:
            try:
                with open('arquivo_lista.txt', 'r') as arquivo:
                    lista_definitiva = json.load(arquivo)
            except json.JSONDecodeError:
                print('Arquivo vazio ou corrompido.')

    while True:
        menu_principal(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
                           'Remover pessoa','Sair do sistema'])
        opcao_usuario = validacao_opcao('Sua opção: ')
        criar_cadastro(opcao_usuario, lista_definitiva)

        if opcao_usuario == 4:
            return lista_definitiva
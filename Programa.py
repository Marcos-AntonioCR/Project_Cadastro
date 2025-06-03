import funções

funções.cabecalho('Menu Principal')

cad = funções.cadastro()
print('-'*30)
print(f'{"Nome":<15}{"Idade":>10}')
print('-'*30)
for nome, idade in cad:
    print(f'{nome:<15}{idade:>10}')
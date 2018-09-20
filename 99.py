"""
    And I thought I was yours forever
    Maybe I was mistaken
    But I just cannot manage to make it through the day
    Without thinking of you lately

    Fireside - Arctic Monkeys ♪♫
"""

import os

PATH = './estagiarios/'

# Cria um registro de estagiários.
def registrar(data):
    dir = os.listdir(PATH)
    # Verificando se existe algum arquivo com a matrícula informada.
    if(dir.count(data[0] + '.txt') != 0):
        print('\n\nJá existe um estagiário com essa matrícula !\n\n')
    else:
        tag = ['Matricula: ', 'Nome: ', 'RG: ', 'CPF: ', 'Endereço: ', 'Celular: ', 'Curso: ', 'Observação: ',
               'Horário de entrada: ', 'Horário de saída: ']
        # Criando um arquivo para o novo estagiário.
        arquivo = open(PATH+data[0]+'.txt', 'w+', encoding="utf8")
        # Escrevendo os dados do estagiário no arquivo.
        for pos, i in enumerate(data):
            arquivo.write('{}{}'.format(tag[pos], i + '\n'))
        # Informando que o estagiário foi cadastrado.
        print("\nO estagiário de matrícula {} foi cadastrado com sucesso !\n".format(data[0]))
# Mostra todos os estagiários cadastrados.
def mostrar():
    dir = os.listdir(PATH)
    if len(dir) == 0:
        print('\n\nNão existe nenhum registro de estagiário !\n\n')
    else:
        print("\nListando {} estagiário(s) cadastrado(s) !\n".format(len(dir)))
        # Percorrendo a lista de arquivos.
        for i in dir:
            # Abrindo o arquivo de registro do estagiário.
            estagiario = open(PATH+i, 'r+', encoding="utf8")
            # Mostrando o conteúdo do arquivo.
            print(estagiario.readline() + estagiario.readline())

# Mostra um estagiário.
def perfil(matricula):
    dir = os.listdir(PATH)
    # Verificando se a matrícula é igual ao nome do arquivo.
    if dir.count(matricula + '.txt') != 0:
        # Abrindo o arquivo do estagiário.
        arquivo = open(PATH+matricula+'.txt', 'r+', encoding="utf8")
        print("\nEstagiário encontrado !\n")
        # Mostrando o conteúdo do arquivo.
        print(arquivo.read())
    else:
        # Quando nenhum estagiário com a matrícula informada é encontrado.
        print('\n\nEstagiário não encontrado !\n\n')

# Edita um estagiário.
def editar(data):
    dir = os.listdir(PATH)
    #Verificando se existe algum arquivo com a matrícula informada.
    if (dir.count(data[0] + '.txt') != 0):
        # Deletando o antigo arquivo.
        os.remove(PATH+data[0]+'.txt')
        # Criando um novo arquivo.
        arquivo = open(PATH+data[0]+'.txt', 'w+', encoding="utf8")
        tag = ['Matricula: ', 'Nome: ', 'RG: ', 'CPF: ', 'Endereço: ', 'Celular: ', 'Curso: ', 'Observação: ',
               'Horário de entrada: ', 'Horário de saída: ']
        # Escrevendo as informações do estagiário no arquivo.
        for pos, i in enumerate(data):
           arquivo.write('{}{}'.format(tag[pos], i + '\n'))
        print("\nEstagiário editado com sucesso !\n")
    else:
        # Estagiário não encontrado.
        print('\n\nO estagiário informado não existe !\n\n')

# Deleta um estagiário.
def deletar(matricula):
    dir = os.listdir(PATH)
    # Verificando se existe algum arquivo com a matrícula informada.
    if (dir.count(matricula + '.txt') != 0):
        # Deletando o arquivo.
        os.remove(PATH+matricula+'.txt')
        print('\n\nEstagiário deletado com sucesso !\n\n')
    else:
        # Estagiário não encontrado.
        print('\n\nEstagiário não encontrado !\n\n')

# Menu da aplicação.
def menu():
    print('[1] Cadastrar estagiário.')
    print('[2] Mostrar um estagiário.')
    print('[3] Mostrar todos estagiários.')
    print('[4] Editar estagiário.')
    print('[5] Deletar estagiário.')
    print('[6] Sair.\n')
    escolha = input('Escolha uma opção: ')
    if(escolha.isnumeric()):
        escolha = int(escolha)
    else:
        return False
    return escolha

# Enfeita atela.
def enfeite():
    print('=-'*30)

enfeite()
print('99ESTAGIÁRIOS'.center(60))
enfeite()
while True:
    while True:
        escolha = menu()
        if escolha != False:
            break
    if escolha == 1:
        tag = ['Matricula (Apenas números): ', 'Nome: ', 'RG (Apenas números): ', 'CPF (Apenas números): ', 'Endereço: ', 'Celular: ', 'Curso: ', 'Observação: ',
               'Horário de entrada: ', 'Horário de saída: ']
        data = [ input('{}'.format(i)) for i in tag]
        if(data[0].isnumeric() and data[2].isnumeric() and data[3].isnumeric()):
            registrar(data)
        else:
            print("\nInforme corretamente os campos, digite apenas números nos campos indicados ! \n")
    elif escolha == 2:
        matricula = input('Digite a matrícula do estagiário: ')
        perfil(matricula)
    elif escolha == 3:
        mostrar()
    elif escolha == 4:
        tag = ['Matricula (Apenas números): ', 'Nome: ', 'RG (Apenas números): ', 'CPF (Apenas números): ', 'Endereço: ', 'Celular: ', 'Curso: ', 'Observação: ',
               'Horário de entrada: ', 'Horário de saída: ']
        data = [input('{}'.format(i)) for i in tag]
        if(data[0].isnumeric() and data[2].isnumeric() and data[3].isnumeric()):
            editar(data)
        else:
            print("\nInforme corretamente os campos, digite apenas números nos campos indicados ! \n")
    elif escolha == 5:
        matricula = input('Digite a matrícula do estagiário: ')
        deletar(matricula)
    elif escolha == 6:
        break
    else:
        printf("\nEscolha uma opção entre 1 e 6 !\n")

"""
    And I thought I was yours forever
    Maybe I was mistaken
    But I just cannot manage to make it through the day
    Without thinking of you lately

    Fireside - Arctic Monkeys ♪♫
"""

import os

PATH = './estagiarios/'
dir = os.listdir(PATH)

# Cria um registro de estagiários.
def registrar(data):
    # Verificando se existe algum arquivo com a matrícula informada.
    if(dir.count(data[0] + '.txt') != 0):
        print('Já existe um estagiário com essa matrícula !')
    else:
        tag = ['Matricula: ', 'Nome: ', 'RG: ', 'CPF: ', 'Endereço: ', 'Celular: ', 'Curso: ', 'Observação: ', 'Horário de entrada: ', 'Horário de saída: ']
        # Criando um arquivo para o novo estagiário.
        arquivo = open(PATH+data[0]+'.txt', 'w+', encoding="utf8")
        # Escrevendo os dados do estagiário no arquivo.
        for pos, i in enumerate(data):
            arquivo.write('{}{}'.format(tag[pos], i + '\n'))

# Mostra todos os estagiários cadastrados.
def mostrar():
    if len(dir) == 0:
        print('Não existe nenhum registro de estagiário !')
    # Percorrendo a lista de arquivos.
    for i in dir:
        # Abrindo o arquivo de registro do estagiário.
        estagiario = open(PATH+i, 'r+', encoding="utf8")
        # Mostrando o conteúdo do arquivo.
        print(estagiario.read())

# Mostra um estagiário.
def perfil(matricula):
    # Verificando se a matrícula é igual ao nome do arquivo.
    if dir.count(matricula + '.txt') != 0:
        # Abrindo o arquivo do estagiário.
        arquivo = open(PATH+matricula+'.txt', 'r+', encoding="utf8")
        # Mostrando o conteúdo do arquivo.
        return (arquivo.read())
    else:
        # Quando nenhum estagiário com a matrícula informada é encontrado.
        return 'Estagiário não encontrado !'

# Edita um estagiário.
def editar(data):
    # Verificando se existe algum arquivo com a matrícula informada.
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
    else:
        # Estagiário não encontrado.
        return 'O estagiário informado não existe !'

# Deleta um estagiário.
def deletar(matricula):
    # Verificando se existe algum arquivo com a matrícula informada.
    if (dir.count(matricula + '.txt') != 0):
        # Deletando o arquivo.
        os.remove(PATH+matricula+'.txt')
        return 'Estagiário deletado com suesso !'
    else:
        # Estagiário não encontrado.
        return 'Estagiário não encontrado !'

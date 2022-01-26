import sys
import clipboard
import json

SAVE_DATA = 'clipboard.json'

def salvar_dados(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def carregar_dados(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return data
    except:
        return {}


salvar_dados("clip.json", {'chave': 'valor'})


if len(sys.argv) == 2:
    comando = sys.argv[1]
    data = carregar_dados(SAVE_DATA)

    if comando == 'salvar':
        chave = input('Digite o nome da chave desejada: ')
        data[chave] = clipboard.paste()
        salvar_dados(SAVE_DATA, data)
        print('Dados salvos com sucesso!')

    elif comando == 'carregar':
        chave = input('Digite o nome da chave desejada: ')
        if chave in data:
            clipboard.copy(data[chave])
            print('Dados copiados à chave')
        else:
            print('A chave escolhida não existe')

    elif comando == 'listar':
        print(data)
    else:
        print('Comando desconhecido')
else:
    print('Informe um comando executável')
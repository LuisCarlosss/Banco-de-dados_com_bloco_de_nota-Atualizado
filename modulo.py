def verificar_arquivo_existente(arquivo): 
    try:
        with open(arquivo):
            pass
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        print('Criando arquivo...')
        
    else:
        print('Arquivo já Existe')
        return True   

def visualizar_arquivo_sistema():
    import os
    return os.listdir()

def exibir_lista_arquivos():
    arquivos = list()
    for arquivo in visualizar_arquivo_sistema():
        if '.txt' in arquivo:
            arquivos.append(arquivo)
    print(arquivos)
if __name__ == '__main__':
    verificar_arquivo_existente()
    exibir_lista_arquivos()
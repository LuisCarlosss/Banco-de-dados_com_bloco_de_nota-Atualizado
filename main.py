import interfaces
import manipulação as txt
import modulo 

#ValueError
while True:
    interfaces.opções()
    try:
        opção = int(input('Opção: '))
    except ValueError:
        print('Digite um número inteiro!')
        print('tente novamente')
        continue
    else:
        pass
    if opção == 1: #Criar arquivo de texto
        arquivo = txt.ArquivoTexto(str(input('Nome do arquivo: ').capitalize()))
        if not modulo.verificar_arquivo_existente(arquivo.renomear_arquivo()):
            arquivo.criar()

    elif opção == 2: #Listar arquivo de texto
        modulo.exibir_lista_arquivos()

    elif opção == 3: #Escrevar no arquivo 
        modulo.exibir_lista_arquivos()
        arquivo = txt.ArquivoTexto(str(input('Nome do arquivo: ').capitalize()))
        arquivo.inserir(arquivo.renomear_arquivo(),str(input('Digite: ')))
        interfaces.interface()
        arquivo.exibir_dentro()
        interfaces.interface()
    else:#Sair do sistema
        break



class ArquivoTexto:

    def __init__(self,arquivo):
        self.arquivo = arquivo

    def criar(self):
        with open(self.arquivo,'w'):
            pass

    def renomear_arquivo(self):
        self.arquivo = str(self.arquivo) + '.txt'
        return self.arquivo

    def deletar(self):
        pass
    def inserir(self,arquivo,texto):
        with open(arquivo,'a',encoding='utf-8')as file:
            file.write(f'{texto}\n')

    def exibir_dentro(self):
        with open(self.arquivo,'r',encoding='utf-8') as file:
            print(file.read())
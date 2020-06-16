class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    nathane = Pessoa(nome = 'Nathane', idade = 27)
    layane = Pessoa(nome = 'Layane', idade = 27)
    rafael = Pessoa(nome = 'Rafael', idade = 18)
    luciano = Pessoa(nathane,rafael,layane, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())#Mesma expressão da linha 15
    print(f'Nome: {luciano.nome}')
    print(f'Idade: {luciano.idade}')
    print(f'Filhos de {luciano.nome}:')
    for filho in luciano.filhos:#Necessário porque os filhos de luciano são objetos da classe Pessoa
        print (filho.nome)

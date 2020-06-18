class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome = None, idade = 50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 45

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    nathane = Mutante(nome = 'Nathane', idade = 27)
    layane = Homem(nome = 'Layane', idade = 27)
    rafael = Pessoa(nome = 'Rafael', idade = 18)
    luciano = Homem(nathane,rafael,layane, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())#Mesma expressão da linha 15
    print(f'Nome: {luciano.nome}')
    print(f'Idade: {luciano.idade}')
    print(f'Filhos de {luciano.nome}:')
    for filho in luciano.filhos:#Necessário porque os filhos de luciano são objetos da classe Pessoa
        print(filho.nome)
    print(Pessoa.metodo_estatico(), nathane.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(nathane, Homem))
    print(isinstance(nathane, Pessoa))
    print(nathane.olhos)
    print(luciano.cumprimentar())
    print(nathane.cumprimentar())


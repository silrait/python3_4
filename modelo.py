class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__like = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        Programa.__init__(self, nome, ano)
        self.__duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        Programa.__init__(self, nome, ano)
        self.__temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
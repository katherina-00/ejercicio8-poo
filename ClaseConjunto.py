class Conjunto:
    __conjunto: list[int]= []

    def __init__(self):
        self.__conjunto = []

    def CrearConjunto(self):
        cantidad=int(input("Ingrese cantidad de elementos de la lista: "))
        for i in range(cantidad):
            num=int(input("Ingrese numero: "))
            self.__conjunto.append(num)

    def getConjunto(self):
        return self.__conjunto

    def __eq__(self, other):
        retorno=False
        if type(other) == list:
            if set(self.__conjunto) == set(other):
                retorno = True

        if type(other) == Conjunto:
            if set(self.__conjunto) == set(other):
                retorno = True

        return retorno

    def __add__(self, other):
        retorno = None
        if type(other) == list:
            for num in other:
                if num not in self.__conjunto:
                    self.__conjunto.append(num)
                    retorno = self
        if type(other) == Conjunto:
            for num in other:
                if num not in self.__conjunto:
                    self.__conjunto.append(num)
                    retorno = self
        return retorno

    def __sub__(self, other):
        retorno = None
        if type(other) == list:
            for num in other:
                if num in self.__conjunto:
                    self.__conjunto.remove(num)
                    retorno = self

        if type(other) == Conjunto:
                self.__conjunto = list(filter((other).__ne__, self.__conjunto))
                retorno = self
        return retorno

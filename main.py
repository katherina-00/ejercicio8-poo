import sys
from ClaseConjunto import Conjunto
from menu import muestraMenu

if __name__=='__main__':
    a=Conjunto()
    a.CrearConjunto()
    print("Conjunto a: {}".format(a.getConjunto()))
    b=[3,6,9]
    #b=[1,2,3,4]
    print("Conjunto b: {}".format(b))

    while True:
            op = muestraMenu()
            if op == '1':
                suma = a + b
                if suma != None:
                    print("suma: {}".format(suma.getConjunto()))
                else: print("suma :{}".format(a.getConjunto()))

            elif op == '2':
                resta = a - b
                if resta != None:
                    print("resta: {}".format(resta.getConjunto()))
                else: print("resta :{}".format(a.getConjunto()))

            elif op == '3':
                igual = a == b
                if igual:
                    print("Los conjuntos son igules")
                else: print("Los conjuntos son distintos")

            elif op == '4':
                sys.exit(0)

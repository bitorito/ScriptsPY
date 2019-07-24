"""
Guia de referencia con funcionalidades moi básicas
Cada apartado inclúe varias seccións para poder recoñecer os 
comandos por funcionalidade e executar por segmentos.
"""
def ComandoPrint():
    print('Hello world!')
    print('Hello world!')
    print('Spam and eggs...')
ComandoPrint()
print('\n')


def Operando():
    a=3**3  #3 al cubo
    print(a)
    b=21/3
    print(b)
    c=23//4  #división truncada
    print(c)
    d=21%4  #calcula resto division
    print(d)
Operando()
print('\n')


def Strings():
    texto1="Coidado co\'s apostrofes \nQue non se usen en galego, \nnon quere decir que non se usen"
    print(texto1)
    texto2='¡Pero si que hai \"comillas\" e @\'s!'
    print(texto2)  #para usar simbolos engadir \""
    print ("Spam"*7)
Strings()
print('\n')


def InOutput_and_cast():
    a=int(input("Intruduce dividendo:"))
    b=int(input("Intruduce divisor:"))
    print("O cociente vale: " + str(a//b) )
    print("O resto vale: " + str(a%b))
InOutput_and_cast()
print('\n')

def PruebaBool():
    a=(2==3)
    print("Son 2 e 3 o mesmo número? "+str(a))
    #Interesante saltar aquí
    b=input("Introduce 0 o 1:")
    if (b!=0 and b!=1):
        print("Vamos que podes. \n")
        PruebaBool()    #¿como saltar a comentario?
    b=bool(b)
    print(b)
#PruebaBool()

def ProbaWhile():
    print("\nEste programa ia equivalencia a booleano do \nnúmero que introduces mediante o teclado.")
    b=5
    while b!=0 and b!=1:
        b=int(input("Introduce 0 ou 1:  "))
        if (b!=0 and b!=1):
            if b<0: 
                print("Eres bueno, colega.")
                break
            print("Mentres non fagas caso non saes do bucle. \n")
        else:
            b=bool(b)
            print("Que equivale ó seguinte operador lóxico: " +str(b))
#ProbaWhile()

def ProbaWhile2():
    print("\nEste programa ia equivalencia a booleano do \nnúmero que introduces mediante o teclado.")
    while bool(1):
        b=int(input("Introduce 0 ou 1:  "))
        print("\n")
        if (b<0):
            b=bool(b)
            print("Eres bueno, colega.")
            print("Segundo python, b=>"+str(b))
            break
        elif (b!=0 and b!=1):
            print("Mentres non fagas caso non saes do bucle. \n")
            continue
        else:
            b=bool(b)
            print("Bo traballo. b->" +str(b))
            break
#ProbaWhile2()

def Listas():
    #Unha lista en python equivale a un array.
    print("\n\nUnha lista pode estar constituida por distintos tipos de dato:")
    lista=["CALAMIDAD", 0.001, -3]
    print("Por exemplo, a lista arbitraria \"lista\": "+str(lista)+"\n")
    while True:
        x=int(input("Introduce un numero de 0 a 2 para escoller un dos valores da lista:  "))
        if x!=0 and x!=1 and x!=2:
            print("Dende 0 ata 2, porfa.")
            continue
        else: break
    print("O "+ str(x+1) +"º elemento de \"a\" ten o valor: "+str(lista[x]))


    print("\nImaxinemos que quixeras ver o caso CALAMIDAD :) ")
    print("Poderíamos introducir agora que posición desta palabra queremos visualizar.")
    x=0 
    while True:
        y=int(input("Introduce agora un numero de 0 a 8 para escoller a letra:   "))
        if y<0 or y>8:
            print("Dende 0 ata 8, porfa.")
            continue
        else: break
    print("A " + str(y+1) + "º letra de \"a\" ten o valor: " + str(lista[x][y]))
    print("\nA efectos prácticos, unha string é moi parecido a unha lista.")
    input("Se declaramos un string: \"a=\"persevera\"\", podemos recorrelo cun \nbucle for que recorra a lista: ")
    a="persevera"
    for i in range (0, 9):
        print(str(a[i]))
#Listas()

def OperaListas1():
    i=0
    a=[]
    while True:
        a=a+[input("\nIntruduce un novo elemento, ou FIN para finalizar: ")]       
        if  a[i]!="FIN":       
            i=i+1
            print(a)        
        else: 
            break
    del(a[i])
    print(a)
#OperaListas()

def OperaListas2():
    a=[]
    while True:
        a.append(input("\nIntruduce un novo elemento, ou FIN para finalizar: "))
        if a[len(a)-1]=="FIN": #len(a) haille que restar 1 para que funcione como indice
            break
        else: print(a)
    del(a[len(a)-1])                
    print(a)
#OperaListas2()

def ProbaRange():
    print("\nUsando o comando \"list(range(3,8))\" teremos unha lista coa seguinte forma: ")
    print(list(range(3,8))) 
    print("\nUsando o comando \"list(range(0+10,100+10,10))\" teremos unha lista coa seguinte forma: ")
    print(list(range(0+10,100+10,10)))
ProbaRange()



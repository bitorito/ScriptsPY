#Definición de función que devolve valor
def CreaListaNum():
    a=[]                                        #variable local desta función
    while True:
        entradalista=input("\nIntruduce un numero ou \"FIN\" para finalizar: ")
        
        if entradalista=="FIN": 
            break
        else:
            a.append(float(entradalista))
            print(a)
    return(a)  

#Definición de función que devolve dous valores cun argumento de entrada
def MediaLista(lista):
    suma=0.0
    for i in range(len(lista)):
        suma=suma+lista[i-1]  
    media=suma/len(lista)
    return suma, media


#Chamada as funcións
a = CreaListaNum()                              #variable definida no "main"
suma, media = MediaLista(a)

print("Resultado sumatorio elementos: " + str(suma))
print("Resultado media elementos: " + str(media))
import os
def busquedaSecuencial(lista, item):
 pos = 0
 encontrado = False
 while pos < len(lista) and not encontrado:
    if lista[pos] == item:
        encontrado = True
    else:
        pos = pos+1
 return encontrado

def busquedaMayor(lista, item):
 pos = 0
 while pos < len(lista):
    if lista[pos] == item:
        return pos
    else:
        pos = pos+1
 return pos

def busquedaAEncontrar(lista, item):
    pos = 0
    while pos < len(lista):
        if lista[pos] == item:
            return pos
        else:
            pos = pos+1
    return pos
"""
print("Ejercicio 1")
listaNumeros=[]
max=0
pos=0
for i in range(1,16):
    num=int(input(f"Ingrese el {i} número: "))
    listaNumeros.append(num)
    if num>max:
        max=num
pos = busquedaMayor(listaNumeros,max)
print("El número mayor es: ",max," y su posición es la: ",pos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
"""
print("Ejercicio 2")
pos=0
listaAEncontrar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num=int(input("Ingrese el número a buscar: "))
pos = busquedaAEncontrar(listaAEncontrar,num)
if pos!=num:
    print("El número no está en la lista")
else:
    print("El número fue encontrado y está en la posición: ",pos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
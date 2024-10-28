import os
import random

#Funciones
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
 numero=0
 encontrado = False
 while pos < len(lista) and not encontrado:
    if lista[pos] == item:
        numero=pos
        encontrado = True
    else:
        pos = pos+1
 return numero,encontrado

def ingresarNumerosEnLista(lista):
   
   for i in range(1,16):
      repetido=False
      num=int(input(f"Ingrese el {i} número "))
      
      while num!=0 and repetido==True:
         
        num=int(input(f"Ingrese el {i} número que no esté repetido "))
      lista.append(num)

#Inicio programa
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

print("Ejercicio 2")
pos=0
encontrado=False
listaAEncontrar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num=int(input("Ingrese el número a buscar: "))
pos,encontrado = busquedaAEncontrar(listaAEncontrar,num)
if encontrado==False:
    print("El número no está en la lista")
else:
    print("El número fue encontrado y está en la posición:",pos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

print("Ejercicio 3")
listaNumerosRandom=[]
encontrado=False
for i in range(50):
   numRandom=random.randint(-200, 200)
   listaNumerosRandom.append(numRandom)
pos=numeroABuscar=int(input("Ingrese el número a buscar "))
pos,encontrado = busquedaAEncontrar(listaNumerosRandom,numeroABuscar)
if encontrado==False:
    print("El número no está en la lista")
else:
    print("El número fue encontrado y está en la posición:",pos)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
"""
print("Ejercicio 4")
listaDeNumeros=[]
ingresarNumerosEnLista(listaDeNumeros)

input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
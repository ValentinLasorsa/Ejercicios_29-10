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
   for i in range(1, 16):
        num = int(input(f"Ingrese el {i} número "))
        repetido = False
        for pos in range(len(lista)):
            if lista[pos] == num:
                print(f"El número {num} está repetido y se encuentra en la posición: {pos}")
                repetido = True
                break  
        if not repetido:
            lista.append(num)

def busquedaPositivos(lista):
    listaPositivos=[]
    for pos in range(len(lista)):
        if lista[pos] >0:
            listaPositivos.append(pos)
    return listaPositivos
#Inicio programa
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

print("Ejercicio 4")
listaDeNumeros=[]
ingresarNumerosEnLista(listaDeNumeros)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

print("Ejercicio 5")
nombreAlumnos=[]
notaAlumnos=[]
cantMuyBueno=0
for i in range(4):
    nombre=input("Ingrese el nombre del alumno ")
    nombreAlumnos.append(nombre)
    nota=int(input(f"Ingrese la nota de {nombreAlumnos[i]} "))
    while nota<0 or nota >10:
       nota=int(input(f"Ingrese la nota correcta de {nombreAlumnos[i]} "))
    notaAlumnos.append(nota)
    if nota>=8:
       cantMuyBueno=cantMuyBueno+1
print("La cantidad de alumnos con leyenda Muy Bueno es:",cantMuyBueno)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

print("Ejercicio 6")
listaNumeros=[]
posicionesPositivos=[]
for i in range(1,11):
   num=int(input(f"Ingrese el {i} número "))
   listaNumeros.append(num)
posicionesPositivos=busquedaPositivos(listaNumeros)
print("Las posiciones de los números positivos es",posicionesPositivos)
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')

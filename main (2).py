#LISTAS
# 1

def suma_lista(numeros):
    suma = 0
    for numero in numeros:
      suma += numero
    return suma
lista = [14, 25, 56,78, 23]  
resultado= suma_lista(lista)
print("el resultado de la lista es: ", resultado)

#2

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0 
    else:
        suma = sum(lista)
        promedio = suma / len(lista)
        return promedio
numeros = [8, 6, 3, 9, 5]
promedio = calcular_promedio(numeros)
print(promedio)

#3

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados
mi_lista = [2, 2, 3, 4,8, 2, 3, 5,3]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print(lista_sin_duplicados)

#4

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
numeros = [9, 5, 2, 7, 1, 8, 3]
numeros_ordenados = ordenar_lista(numeros)
print(numeros_ordenados)

#TUPLAS
 #1

def palabra_mas_larga(lista_palabras):
    palabra_mas_larga = ""
    longitud_maxima = 0

    for palabra in lista_palabras:
        if len(palabra) > longitud_maxima:
            palabra_mas_larga = palabra
            longitud_maxima = len(palabra)

    return palabra_mas_larga
lista = ["gato", "perro", "Foca", "jirafa","loro","Murciélago"]
palabra_mas_larga = palabra_mas_larga(lista)
print(palabra_mas_larga) 

#2

def producto_tupla(tupla):
    producto = 1

    for num in tupla:
        producto *= num

    return producto
tupla = (2, 3, 9, 7)
resultado = producto_tupla(tupla)
print(resultado) 

#3
def maximo_minimo_tupla(tupla):
    maximo = max(tupla)
    minimo = min(tupla)
    return maximo, minimo
tupla = (48, 87, 99, 13, 66)
maximo, minimo = maximo_minimo_tupla(tupla)
print("Máximo:", maximo)  
print("Mínimo:", minimo)  

#4
def contar_ocurrencias_tupla(tupla):
    diccionario = {}

    for elemento in tupla:
        if elemento in diccionario:
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1

    return diccionario
tupla = (8, 6, 8, 4, 3, 7, 6)
ocurrencias = contar_ocurrencias_tupla(tupla)
print(ocurrencias) 

#5

def encontrar_indices(tupla, elemento):
    indices = []

    for i in range(len(tupla)):
        if tupla[i] == elemento:
            indices.append(i)

    return indices
tupla = (6, 9, 4, 8, 3, 2, 9)
elemento = 2
indices = encontrar_indices(tupla, elemento)
print(indices)

#6

def separar_cadenas_por_vocal(tupla_cadenas):
    vocales = ('a', 'e', 'i', 'o', 'u')
    cadenas_con_vocal = []
    cadenas_sin_vocal = []

    for cadena in tupla_cadenas:
        if cadena.lower().startswith(vocales):
            cadenas_con_vocal.append(cadena)
        else:
            cadenas_sin_vocal.append(cadena)

    return tuple(cadenas_con_vocal), tuple(cadenas_sin_vocal)
tupla = ("manzana","loro","perro","Mono","elefante","gato","abdomen"," hígado","músculo","cuello","corazón","mente","alma","espíritu", "pecho","cintura","cadera","espalda","sangre","carne", "piel","hueso","Iglesia")
con_vocal, sin_vocal = separar_cadenas_por_vocal(tupla)
print("Cadenas con vocal:", con_vocal)  
print("Cadenas sin vocal:", sin_vocal)  

#DICCIONARIOS

#1
def contar_palabras(lista_palabras):
    contador = {}

    for palabra in lista_palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador
lista = ["SOFIA","HELEN","HELEN","SOFIA","HELEN","JULIETH", "SOFIA","HELEN","LEO","SALOME","JIRETH","SALOME","CRISTIAN","MERY","ALEJO","MATIAS"]
contador = contar_palabras(lista)
print(contador)  


#2

def promedio_calificaciones(diccionario_estudiantes):
    total_calificaciones = 0
    total_estudiantes = len(diccionario_estudiantes)

    for calificaciones in diccionario_estudiantes.values():
        total_calificaciones += sum(calificaciones)

    promedio = total_calificaciones / total_estudiantes

    return promedio

estudiantes = {
    "Juan": [78, 91,71],
    "María": [76,85,76],
    "Pedro": [68,99,87],}
promedio = promedio_calificaciones(estudiantes)
print(promedio) 



#3

def filtrar_diccionario(diccionario, valor):
    nuevo_diccionario = {}

    for clave, val in diccionario.items():
        if val == valor:
            nuevo_diccionario[clave] = val

    return nuevo_diccionario
diccionario = {"SEBASTIAN": 25, "MARIA": 30, "JIMMY": 25, "CAMILA": 40}
valor = 25
nuevo_diccionario = filtrar_diccionario(diccionario, valor)
print(nuevo_diccionario)  

#4

def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_combinado = {}

    # Combinar las claves y valores del primer diccionario
    for clave, valor in diccionario1.items():
        diccionario_combinado[clave] = valor

    # Sumar los valores de las claves comunes del segundo diccionario
    for clave, valor in diccionario2.items():
        if clave in diccionario_combinado:
            diccionario_combinado[clave] += valor
        else:
            diccionario_combinado[clave] = valor

    return diccionario_combinado
diccionario1 = {"a": 1, "b": 2, "c": 3}
diccionario2 = {"b": 5, "c": 4, "d": 6}
diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
print(diccionario_combinado) 


#5


def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}

    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador
texto = "Érase una vez un rey muy presumido, que vivía en gran castillo. Un día un comerciante de un lejano país le hizo un extraño trato"
resultado = contar_palabras(texto)
print(resultado)





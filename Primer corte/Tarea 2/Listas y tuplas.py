#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Define los cada uno de los elementos y su posición en la lista
#input()
print(my_lista) #Imprime la lista actual
print(type(my_lista)) #Imprime el tipo de lista 
print(my_lista[2]) #Imprime el tercer elemento de la lista

print("my_lista size: ", len(my_lista)) #Imprime la cantidad de elementos en la lista
print(my_lista[0:2])#Imprime los elementos con posiciones 0 y 2 de la lista
print(my_lista[:2])#Imprime los elementos con posiciones 0 y 2 de la lista

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista) #Imprime la lista actual con el elemento agregado al final de esta

my_lista.insert(3, 'Negro') #Agrega el elemento en la posicion numero 3, moviendo todos después del 3 1 posición adelante
print(my_lista) #Imprime la lista actual con el nuevo elemento en la posición concreta y los elementos adelante de este movidos 1 posición


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)#Imprime la lista con la otra que ha sido concatenada

print(my_lista.index('Azul'))#Muestra el indice de posición del elemento con nombre "Azul"

#my_lista.remove('Magenta') #Comentario de remover el elemento con nombre "Magenta"
my_lista.remove('Marron')#Remueve el elemento con nombre "Marron" y a todos los elementos adelante los desplaza una posición a la izquierda
print(my_lista) #Imprime la lista actual sin el elemento que ha sido removido

my_lista.insert(8, 'Marron') #Agrega el elemento en la posicion numero 8, moviendo todos después del 8 1 posición adelante
print(my_lista) #Imprime la lista con el elemento que ha sido agregado

print(my_lista.pop())#Remueve y vuelve a poner el último elemento de la lista 
size = len(my_lista) #Define size cómo la medida de la lista 
print("size = ", size) #Imprime la cantidad de elementos en la lista utilizando size
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #Define my_lista_3 cómo una lista que repite los nueve elementos 3 veces con el orden de la primera lista
print("my_lista_3: ", my_lista_3) #Imprime my_lista_3 con los 27 elementos. 

print("Sort:")#Imprime "Sort: "
print() #Imprime un salto de linea
my_listaSort = my_lista.sort() #Define my_listaSort cómo una lista ordenada ascendentemente y que retorna nada
print(my_listaSort) #Imprime el resultado de my_lista.sort, en otras palabras, "none"

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Define una lista de 10 elementos, siendo los numeros del 10 al 1 en orden descendente
print("Ordering my_NumList: ") #Imprime "Ordering my_Numlist"
my_NumList.sort() #Organiza los elementos de manera ascendente en la misma lista
print(my_NumList) # Imprime la lista ordenada de manera ascendente 
#OrderedLList = my_NumList.sort() #Comentario nombrando a la variable OrderedLList cómo la lista ordenada asceendentemente
#print(my_listaSort) #Imprime el resultado de my_lista.sort, en otras palabras, "none"

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True) #Se reorganiza la my_NumList de manera descendente
print("De menor a mayor: ", my_NumList) #Se imprime la lista ordenada de manera descendente



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################") #Asteriscos decorativos
print("###########################") #Asteriscos decorativos
print("###########################") #Asteriscos decorativos
print("############TUPLAS#########") #Asteriscos decorativos con el titulo de "Tuplas"
my_tupla = tuple(my_lista) #Define a la tupla desde my_lista
print() #Imprime un salto de linea
print() #Imprime un salto de linea
print("my_tuple: ", my_tupla) #Imprime la my_tupla

print(my_tupla[0]) #Imprime el elemento de la posición 0 de my_tupla
print(my_tupla[2]) #Imprime el elemento de la posición 0 de my_tupla


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla) #Verifica si el elemento entre comillas está en la tupla
print(my_tupla.count('Rojo')) #Verifica si el elemento entre comillas está en la tupla con la función count

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco') #Designa my_tupla_unitaria cómo una tupla que solo contiene el elemento "Blanco"
print(my_tupla_unitaria) #Imprime my_tupla_unitaria

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999 #Define my:tupla con 3 elementos y sin parentesis.
print(my_tupla) #Imprime my_tupla, haciendo que se imprima en una linea individual cada elemento

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla #desempeaqueta la tupla
print(nombre) #Imprime la varibale de la primera posición, siendo "Gaspar"
print(dia) #Imprime la varibale de la segunda posición, siendo "5"
print(mes) #Imprime la varibale de la tercera posición, siendo "8"
print(año) #Imprime la varibale de la cuarta posición, siendo "1999"

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año) #Imprime los elmentos de la tupla en el orden dado

#Convertir una tupla en una lista
my_lista2=list(my_tupla)#Convierte my_tupla en una lista llamada my_lista2
print(my_lista2) #Imprime my_lista2

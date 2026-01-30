"""Eliminación de Elementos Repetidos


Descripción:

 El programa debe permitir al usuario ingresar una lista de N palabras y luego eliminar los elementos repetidos, mostrando una lista sin duplicados.


Requisitos:

    Usar una lista para almacenar las palabras ingresadas.
    Recorrer la lista con una estructura repetitiva.
    Utilizar una estructura de decisión para eliminar duplicados sin usar set().


"""
# --- MENÚ DE INICIO ---
print("========================================")
print("BIENVENIDO AL LIMPIADOR DE LISTAS REPETIDAS   ")
print("========================================")

# Pedimos al usuario cuántas palabras quiere ingresar
cantidad = int(input("¿Cuántas palabras vas a ingresar?: ")) # Convierte la entrada a número entero

# Creamos la lista donde guardaremos todo lo que el usuario escriba
lista_original = [] # Esta es una lista vacía para empezar

# Usamos un ciclo para pedir cada palabra una por una
for i in range(cantidad): # Se repetirá según el número que dio el usuario
    palabra = input(f"Ingresa la palabra {i+1}: ") # Pide la palabra y muestra el número actual
    lista_original.append(palabra) # Agrega la palabra al final de nuestra lista

# --- LÓGICA PARA ELIMINAR REPETIDOS ---

# Creamos una nueva lista para guardar solo las palabras únicas
lista_sin_duplicados = [] # Aquí no habrá repetidos

# Recorremos la lista original elemento por elemento
for elemento in lista_original: # "elemento" va tomando el valor de cada palabra
    # Usamos una decisión para ver si la palabra YA está en la lista nueva
    if elemento not in lista_sin_duplicados: # Si NO está presente...
        lista_sin_duplicados.append(elemento) # ...entonces la agregamos

# --- MOSTRAR RESULTADOS ---
print("\n--- RESULTADOS ---") # Salto de línea para que se vea ordenado
print("Tu lista original era:", lista_original) # Muestra todo lo ingresado
print("Tu lista sin repetidos es:", lista_sin_duplicados) # Muestra la lista limpia
print("========================================")
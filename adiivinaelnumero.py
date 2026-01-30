"""Descripción del Reto:

Vas a programar uno de los juegos más clásicos de la iniciación a la programación: "Adivina el Número". El objetivo es crear un programa en el que la computadora "piensa" en un número y el jugador debe adivinarlo en la menor cantidad de intentos posible.


Para este reto, el programa comenzará con un número secreto predefinido (por ejemplo, el número 42). Luego, solicitará al usuario que ingrese un número para intentar adivinarlo. El programa debe continuar pidiendo números hasta que el jugador adivine correctamente. En cada intento fallido, el programa debe darle al jugador una pista, indicándole si su número es demasiado alto o demasiado bajo en comparación con el número secreto. Una vez que el jugador adivine el número, el programa debe felicitarlo y mostrarle cuántos intentos le tomó.

0

·

0"""

# --- MENÚ DE BIENVENIDA ---
print("==========================================")
print("   ¡BIENVENIDO A ADIVINA EL NÚMERO!   ")
print("==========================================")
print("He pensado un número. ¿Podrás adivinarlo?")

# --- CONFIGURACIÓN INICIAL ---
numero_secreto = 42 # Definimos el número que el usuario debe buscar
intentos = 0 # Esta variable contará cuántas veces ha probado el usuario
adivinado = False # Usamos esta variable para saber cuándo terminar el juego

# --- BUCLE DEL JUEGO ---
# El ciclo seguirá funcionando MIENTRAS "adivinado" sea Falso
while adivinado == False: 
    # Pedimos al usuario su apuesta
    intento_usuario = int(input("\nIntroduce tu número: ")) # Convertimos la entrada a número
    intentos = intentos + 1 # Sumamos 1 al contador de intentos en cada vuelta

    # --- ESTRUCTURA DE DECISIÓN ---
    if intento_usuario == numero_secreto: # Si el número es igual al secreto...
        print("¡Felicidades! Has acertado.") # Saludamos al ganador
        adivinado = True # Cambiamos a True para que el bucle "while" se detenga
    
    elif intento_usuario < numero_secreto: # Si el número es menor...
        print("Pista: El número secreto es MÁS ALTO.") # Damos una ayuda
        
    else: # Si no es igual ni menor, por lógica es mayor
        print("Pista: El número secreto es MÁS BAJO.") # Damos una ayuda

# --- CIERRE DEL PROGRAMA ---
print("------------------------------------------")
print(f"Lograste adivinar el {numero_secreto} en {intentos} intentos.")
print("¡Gracias por jugar!")
print("==========================================")
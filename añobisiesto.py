"""Estás colaborando en la creación de una aplicación de calendario y tu tarea es implementar una función crucial: un validador de años bisiestos. Para que el calendario funcione correctamente, el programa necesita saber cuándo el mes de febrero tiene 29 días.


Tu programa debe solicitar al usuario que ingrese un año. A continuación, deberá aplicar las reglas del calendario gregoriano para determinar si ese año es bisiesto o no.

Las reglas son las siguientes:

    Un año es bisiesto si es divisible por 4.
    Excepción: Los años que son divisibles por 100 no son bisiestos.
    Excepción a la excepción: A menos que el año también sea divisible por 400, en cuyo caso sí es bisiesto."""


# --- MENÚ DE INICIO ---
print("========================================")
print("    RETO: ENCUENTRA UN AÑO BISIESTO    ")
print("========================================")
print("Tu misión es escribir un año que sea bisiesto.")
print("El programa no terminará hasta que lo logres.")

# Creamos una variable para controlar el bucle
# La ponemos en False porque al principio aún no han acertado
acierto = False 

# Iniciamos el bucle: "Mientras acierto sea igual a Falso..."
while acierto == False:
    
    # Pedimos el año al usuario
    entrada = input("\nIntroduce un año: ") # El \n es para dejar un espacio en blanco
    
    # Verificamos que sean números para que no de error
    if entrada.isdigit():
        anio = int(entrada) # Convertimos el texto a número
        
        # Aplicamos la lógica matemática de bisiestos
        # (Divisible por 4 Y NO por 100) O (Divisible por 400)
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"¡LOGRADO! El año {anio} es bisiesto.") # Mensaje de éxito
            print("Felicidades, has completado el reto.")
            acierto = True # CAMBIAMOS A TRUE: Esto rompe el bucle y el programa termina
        else:
            # Si no es bisiesto, le damos una pista al usuario
            print(f"El año {anio} no es bisiesto (febrero tiene 28 días).")
            print("Inténtalo de nuevo, busca uno que sea múltiplo de 4...")
            
    else:
        # Si el usuario escribe letras o símbolos
        print("¡Cuidado! Debes ingresar un número de año válido.")

# --- MENSAJE FINAL ---
print("========================================")
print("       GRACIAS POR PARTICIPAR           ")
print("========================================")
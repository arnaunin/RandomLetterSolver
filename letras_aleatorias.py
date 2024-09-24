### Falta traducir los comentario y añadir mas comprovaciones para la palabra introducida

import random as rd
import string as str
import time

counter = 0 # Contador de palabras generadas 
string = '' # Variable en la que se almacena la palabra generada
word = input("Introduce un palabra con un maximo de 5 letras: ")

# Comprovamos que la palabra introducida tenga 5 o menos letras
while len(word) > 5:
    word = input("Introduce un palabra con un maximo de 5 letras: ")

# Imprimimos un mensaje de espera ya que la ejecución puede tardar unos segundos
print("Espera a que se termine de ejecutar el codigo.")
time.sleep(2)

# Bucle para ir generando palabras y comprovando si es la palabra introducida mientras la palabra resultante no sea igual a la introducida
while string != word:
    counter += 1 # Actualizamos contador
    string = '' # Vaciamos la variable ya que se va a generar una palabra nueva

    # Bucle para ir generando letras hasta que la palabra tenga la la longituud de a palabra intrudcida
    for i in range(len(word)):
        letter = rd.choice(str.ascii_lowercase) # Generamos una letra minuscula aleatoria
        string += letter # Añadimos la letra a la string

print(f"Intentos requeridos para genrar la palabra {word}: {counter}")

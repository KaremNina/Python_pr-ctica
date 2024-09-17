print ("¡Hola, Mundo!")


# Este es un comentario de una sola línea

"""
Este es un comentario
de varias líneas
"""
"""Suma (+): suma dos valores.
Resta (-): resta el segundo valor del primero.
Multiplicación (*): multiplica dos valores.
División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
División entera (//): divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
Módulo (%): devuelve el resto de la división entre el primer valor y el segundo.
Exponenciación (**): eleva el primer valor a la potencia del segundo."""

"""a = 10
b = 3


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1 
exponenciacion = a ** b   # 1000  (10*10*10)"""


"""COMPARACION = 
Igual a (==): devuelve True si ambos valores son iguales.
Diferente de (!=): devuelve True si los valores son diferentes.
Mayor que (>): devuelve True si el primer valor es mayor que el segundo.
Menor que (<): devuelve True si el primer valor es menor que el segundo.
Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo.
Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo."""

"""Ejemplos:

a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
mayor que = a > b   # True
menor que = a < b   # False
mayor o igual = a >= b   # True
menor o igual = a <= b   # False"""

"""LOGICOS

Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones. Los operadores lógicos en Python son:

AND (and): devuelve True si ambas condiciones son verdaderas.
OR (or): devuelve True si al menos una de las condiciones es verdadera.
NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.

Ejemplo:

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False 
"""


"""Python sigue las reglas de precedencia de operadores, 
donde ciertos operadores tienen prioridad sobre otros.
En general, la precedencia sigue el orden: paréntesis,
exponenciación, multiplicación/división, 
suma/resta, operadores de comparación y operadores lógicos."""



"""Ejemplo:

calificacion = 85


if calificacion >= 90:
print ("Excelente")

elif calificacion >= 80:
print ("Muy bueno")

elif calificacion >= 70:
print ("Bueno")

else:
print ("Necesita mejorar")"""

#BUCLES
"""
For
El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente:

for variable in secuencia:

    # Bloque de código a repetir
    instrucciones
Ejemplo:

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)
"""

"""
While
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:

while condicion:

    # Bloque de código a repetir
    instrucciones
Ejemplo:

contador = 0


while contador < 5:

Print(contador)
contador += 1

En este ejemplo, el bucle while se ejecuta mientras la variable contador sea menor que 5.
En cada iteración, se imprime el valor de contador y 
luego se incrementa en 1 mediante la instrucción contador += 1. 
El bucle se detendrá cuando contador alcance el valor de 5.
Es importante tener cuidado al usar el bucle while, ya que, 
si la condición nunca se vuelve falsa, el bucle se ejecutará indefinidamente, 
lo que se conoce como un bucle infinito.
"""
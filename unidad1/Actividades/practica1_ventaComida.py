

#Practica diagnostico_nombre.py
#Simula un ticket de venta
#Objetivo: Aplicar funciones, bucles, condiciones, listas y variables

#Elegir una tematica de un negocio que vende 3 productos

Productos = ["hotdog", "quesadilla", "refresco"]
precios = [40, 70, 50]

#Funciones para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range (len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Menu de usuario
print(f"..:: Bienvenido a nuestro negocio ::..")
nombre = input("Por favor, ingresa tu nombre: ")

cantidades = []  

print("Selecciona qué deseas ordenar:")
for i in range(len(Productos)):
    print(f"{i + 1}. {Productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {Productos[i]} deseas ordenar? "))
    cantidades.append(cantidad)  # Agrega la cantidad a la lista

    #calcular total
    total = calcular_total(cantidades, precios)

    # Mostrar ticket
print("\n ..:: TICKET DE COMPRA ::.. ")
print(f"Cliente: {nombre}")
print("-" * 30)
for i in range(len(Productos)):
    subtotal = cantidades[i] * precios[i]
    print(f"{Productos[i].capitalize():<12} x {cantidades[i]:<2} = ${subtotal}")
print("-" * 30)
print(f"Total a pagar: ${total}")
print("¡Gracias por tu compra!")
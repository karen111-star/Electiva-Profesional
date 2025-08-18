lista = [20, 12, 21.3, 34]




def suma_lista(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return float(suma )



# Base variables
lista = [20, 12, 21.3, 34]
lista_prueba = [23.7, 15.1, 22.2, 21, 16.1, 24, 15.9]

# Caso 1: no existe la función.
try:
    suma_lista
    assert type(suma_lista) == type(lambda:None)
except:
    raise NotImplementedError("No existe una función llamada suma_lista.",)
    
# Caso 2: la función es interrumpida por errores durante su ejecución.
try:
    suma_lista(lista)
    suma_lista(lista_prueba)
except:
    raise RuntimeError("Tu función produce un error al ejecutarse.")

# Caso 3: no retorna un número
assert type(suma_lista(lista_prueba)) == float, f"Tu función debe retornar un valor de tipo {float.__name__}."

# Caso 4: respuesta explicita
assert suma_lista(lista_prueba) != 87.3, "Tu respuesta es incorrecta para una instancia diferente. Utiliza el parámetro."

# Caso 5: suma elemento por elemento
assert suma_lista(lista_prueba) >= 138.0, "Tu función puede no estar sumando todos los elementos de la lista."

# Caso 6: retorna un numero distinto del esperado
assert suma_lista(lista_prueba) == 138.0, "Tu función no retorna el valor correcto."
assert suma_lista(lista) == 87.3, "Tu función no retorna el valor correcto."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")
# Importamos los datos
# Importamos el módulo datetime de Python
# proporciona clases para manipular fechas y horas.


import dades
import PySide6
from datetime import datetime


# Creamos la función "ordenar_per_nom"
def ordenar_per_nom(list):
    # Declaramos la función para retornar
    # los datos de manera ordenada, basandonos en el nombre
    list = sorted(list, key=lambda element: element['alumne'])
    return list


# Creamos la función "ordenar_per_naiximent"
def ordenar_per_naiximent(list):
    def KeyFunction(element):
        return datetime.strptime(
            element['data_naiximent'], '%d-%m-%Y')
    list.sort(key=KeyFunction)
    return list
# Llamamos a la función pasandole como parametro la lista sin ordenar


llista_desordenada = dades.llista
ordenar_per_nom(llista_desordenada)
# Llamamos a la función pasandole como parametro la lista sin ordenar

ordenar_per_naiximent(llista_desordenada)

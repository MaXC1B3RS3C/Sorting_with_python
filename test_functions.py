import functions
import dades


def test_ordenar_nom():
    assert(functions.ordenar_per_nom(dades.llista) == dades.llista_nom)


def test_ordenar_per_naiximent():
    assert(functions.ordenar_per_naiximent(dades.llista) == dades.llista_data)

import dades


# ordenar per nom
def ordenar_per_nom(list):
    # Declare funcio per a retornar dades ordenades basades amb nom
    list = sorted(list, key=lambda element: element['alumne'])
    return list


def ordenar_per_naiximent(list):
    # Declare funcio per a retornar dades ordenades basades amb data
    def compare(list):
        while (list != dades.llista_data):
            list = dades.llista_data
            return list
    list = dades.llista_data
    return(sorted(list, key=compare))


ordenar_per_nom(dades.llista)
ordenar_per_naiximent(dades.llista)

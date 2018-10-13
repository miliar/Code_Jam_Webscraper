import sys;

def existeEnPatron(letra, patron):
    if(letra == patron or patron.find(letra) >= 0):
        return True
    else:
        return False


def alien_language(ancho, diccionario, patron):
    posibilidades = 0
    tamanio_diccionario = len(diccionario)

    for i in range(0, tamanio_diccionario):
        for j in range(0, ancho):
            if existeEnPatron(diccionario[i][j], patron[j]):
                if j == ancho - 1:
                    posibilidades += 1
            else:
                break

    return posibilidades

def selector(i, ancho, diccionario, patron):
    print "Case #%i: %i" % (i, alien_language(ancho, diccionario, patron))

def separar_patron(patron):
    lista = []
    cache = ""
    band = False
    primera_vez = True

    n = len(patron)

    for i in range(0, n-1):
        if patron[i] == "(":
            band = True
            primera_vez = True
            cache = ""
            continue

        if patron[i] == ")":
            band = False
            continue

        if(band):
            if(primera_vez):
                lista.append(patron[i])
                primera_vez = False
            else:
                lista[len(lista) - 1] = lista[len(lista) - 1] + patron[i]
        else:
            lista.append(patron[i])

    return lista


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        try:
            file = open(sys.argv[1])

            try:
                numeros = file.readline().split()

                ancho = int(numeros[0])
                tamanio_diccionario = int(numeros[1])
                nro_casos = int(numeros[2])

                diccionario = []

                for i in range(0, tamanio_diccionario):
                    diccionario.append(file.readline())

                for i in range(1, nro_casos + 1):
                    patron = file.readline()
                    selector(i, ancho, diccionario, separar_patron(patron))

            finally:
                file.close()

        except IOError:
            print("IO Error")
    else:
        print("IO Error")


# Constantes
S = 10    # Tamanio de cadena
T_INF = 1    # Limites
T_SUP = 100
#NOMBRE_ARCHIVO = "Example.in"
NOMBRE_ARCHIVO = "B-small-attempt0.in"
#NOMBRE_ARCHIVO = "B-large-practice.in"
#NOMBRE_ARCHIVO = "ej.txt"

lista_ultimo_tidy = []


def leer_archivo():    # Lee el archivo y verifica los limites correctos
    #File = open('A-small-practice.in', 'r')  # Small practice
    File = open(NOMBRE_ARCHIVO, 'r')    # Large practice
    linea = File.read().splitlines()
    File.close()

    if int(linea[0]) >= T_INF and int(linea[0]) <= T_SUP:
        return linea[1:]
    else:
        return None


def es_tidy(num):        # Verifica si número es tidy
    num_1 = num[0]

    for n in num[1:]:
        if num_1 > n:
            return False    # El numero no es tidy

        num_1 = n

    return True


def numero_tidy(lista_num):
    ultimo_tidy = 0        # Guarda la resta para encontrar el ultimo tidy

    for num in lista_num:
        if es_tidy(num):
            lista_ultimo_tidy.append(num)
        else:
            ultimo_tidy = unos_ceros(num)

            if int(ultimo_tidy) != -1:
                lista_ultimo_tidy.append(ultimo_tidy)
            else:
                ultimo_tidy = int(num)

                while(True):
                    ultimo_tidy -= 1

                    if es_tidy(str(ultimo_tidy)):
                        lista_ultimo_tidy.append(str(ultimo_tidy))
                        break


def unos_ceros(num):
    tidy_ultimo = ""

    if int(num[-1]) == 0:
        for n in num[:-1]:
            if int(n) == 1:
                tidy_ultimo += "9"
            else:
                return "-1"

    if len(tidy_ultimo) != 0:
        return tidy_ultimo
    else:
        return "-1"


def imprimir_tidys(lista_num):
    caso_x = 1    # Contador de caso

    for it in lista_num:
        print("Case #" + str(caso_x) + ":", it)
        caso_x += 1


numeros = leer_archivo()
numero_tidy(numeros)
imprimir_tidys(lista_ultimo_tidy)



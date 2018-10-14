# -*- coding: utf-8 -*-
# Constantes
#S = 10    # Tamanio de cadena
#T_INF = 1    # Limites
#T_SUP = 100
#NOMBRE_ARCHIVO = "Example.in"
#NOMBRE_ARCHIVO = "B-small-practice.in"
#NOMBRE_ARCHIVO = "B-large-practice.in"
#NOMBRE_ARCHIVO = "A-small-attempt0.in"
#NOMBRE_ARCHIVO = "ej.txt"
NOMBRE_ARCHIVO = "A-large.in"


def leer_archivo():    # Lee el archivo y verifica los limites correctos
    #File = open('A-small-practice.in', 'r')  # Small practice
    File = open(NOMBRE_ARCHIVO, 'r')    # Large practice
    linea = File.read().splitlines()
    File.close()

    return linea[1:]


def signo_igual(lista, signo):    # Boolean
    for it in lista:
        if it != signo:
            return False
    return True


def girar(lista, ini, fin):
    for i in range(ini, fin):
        if lista[i] == '+':
            lista[i] = '-'
        else:
            lista[i] = '+'


def contar_signo(lista, s):
    cont = 0

    for it in lista:
        if it == s:
            cont += 1
        else:
            return cont


def pos_menos(lista):    # Retorna la posicion de un menos
    p = 0

    for it in lista:
        if it == '-':
            break
        p += 1

    return p


lista_param = leer_archivo()
#print(lista_param)
#s, k = lista_param[0].split(' ')
#print(s, k)
caso = 0       # Variable contador de casos
pos_ini = 0
pos_fin = 0
n_giros = 0


for it in lista_param:
    caso += 1        # incremento caso
    s, k = it.split(' ')    # donde s es string (+-+-+) && k es la ventana
    #print(type(k))
    s_list = list(s)
    n_giros = 0

    if signo_igual(s, '+'):
        print("Case #" + str(caso) + ":", 0)
    else:
        while(True):
            pos_ini = pos_menos(s_list)
            pos_fin = pos_ini + int(k)

            if pos_fin <= len(s_list):
                girar(s_list, pos_ini, pos_fin)
                n_giros += 1
            else:
                break

        if signo_igual(s_list, '+'):
            print("Case #" + str(caso) + ":", n_giros)
        else:
            print("Case #" + str(caso) + ": IMPOSSIBLE")

























'''
cont_iter = None
lista_s = []
lista_tmp = []
caso = 1
n_girar = 0

for s in lista_param:
    cont_iter = 0

    for it in s:
        lista_s.append(it)

    while(signo_igual(lista_s, '+') is not True):
        if signo_igual(lista_s, '-') is True:
            girar(lista_s, len(lista_s))
        elif lista_s[0] == '+':
            n_girar = contar_signo(lista_s, '+')
            girar(lista_s, n_girar)
        else:
            n_girar = contar_signo(lista_s, '-')
            girar(lista_s, n_girar)
        cont_iter += 1

    print("Case #" + str(caso) + ": " + str(cont_iter))
    caso += 1
    lista_s.clear()    # Limpiamos lista
'''
#!/usr/bin/python

MAX_HIGH = 999999

def direccion(mapa, x, y):
    N, W, E, S = MAX_HIGH, MAX_HIGH, MAX_HIGH, MAX_HIGH
    if (x > 0):
        if (mapa[x-1][y] < mapa[x][y]):
            N = mapa[x-1][y]
    if (y > 0):
        if (mapa[x][y-1] < mapa[x][y]):
            W = mapa[x][y-1]
    if (y < len(mapa[0]) - 1):
        if (mapa[x][y+1] < mapa[x][y]):
            E = mapa[x][y+1]
    if (x < len(mapa) - 1):
        if (mapa[x+1][y] < mapa[x][y]):
            S = mapa[x+1][y]
#    print 'Min %s, %s, %s, %s = %s' % (N, W, E, S, min(N, W, E, S))
    minimo = min(N, W, E, S)
    if (minimo == MAX_HIGH):
        return 'o'
    if (N == minimo):
        return 'N'
    if (W == minimo):
        return 'W'
    if (E == minimo):
        return 'E'
    if (S == minimo):
        return 'S'
    return 'o'

def busca_zona(mapa, i, j, resultado, index):
    if (i > 0):
        dir = direccion(mapa, i-1, j)
        if ((dir == 'S') and (resultado[i-1][j] == 0)):
            resultado[i-1][j] = index
            resultado = busca_zona(mapa, i-1, j, resultado, index)
    if (j > 0):
        dir = direccion(mapa, i, j-1)
        if ((dir == 'E') and (resultado[i][j-1] == 0)):
            resultado[i][j-1] = index
            resultado = busca_zona(mapa, i, j-1, resultado, index)
    if (j < len(mapa[0]) - 1):
        dir = direccion(mapa, i, j+1)
        if ((dir == 'W') and (resultado[i][j+1] == 0)):
            resultado[i][j+1] = index
            resultado = busca_zona(mapa, i, j+1, resultado, index)
    if (i < len(mapa) - 1):
        dir = direccion(mapa, i+1, j)
        if ((dir == 'N') and (resultado[i+1][j] == 0)):
            resultado[i+1][j] = index
            resultado = busca_zona(mapa, i+1, j, resultado, index)
    return resultado

def pinta_matriz(resultado):
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            print resultado[i][j],
        print ''

for case in range(input()):
    print 'Case #%s:' % (case + 1)
    x, y = map(int, raw_input().split())
    mapa = []
    for i in range(x):
        mapa.append(map(int, raw_input().split()))

#    for i in range(x):
#        for j in range(y):
#            print direccion(mapa, i, j),
#        print ''

#    resultado = [[0]*y]*x
    resultado = []
    for i in range(x):
        resultado.append([0]*y)
    index = 10
    for i in range(x):
        for j in range(y):
            dir = direccion(mapa, i, j)
            if ((dir == 'o') and (resultado[i][j] == 0)):
                resultado[i][j] = index
#                pinta_matriz(resultado)
#                print ''
                resultado = busca_zona(mapa, i, j, resultado, index)
#                pinta_matriz(resultado)
#                print ''
                index += 1

    letra = 97
    dict = {}
    for i in range(x):
        for j in range(y):
            if (resultado[i][j] not in dict):
                dict[resultado[i][j]] = chr(letra)
                letra += 1

    for i in range(x):
        linea = ' '.join(map(str, resultado[i]))
#        linea += ' '
#        print '#%s#' % linea
        for key, value in dict.iteritems():
            if ((str(key)) in linea):
#                print '%s, %s' % (key, value)
#                linea = linea.replace(' ' + str(key) + ' ', ' ' + value + ' ')
                linea = linea.replace(str(key), value)
        print linea

#    pinta_matriz(resultado)
#    print ''

    #print 'Case #%s: %s %s triangle' % (case + 1, w1, w2)

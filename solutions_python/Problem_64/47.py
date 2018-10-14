#!/usr/bin/python

hexbin = {'0':[0,0,0,0],
        '1':[0,0,0,1],
        '2':[0,0,1,0],
        '3':[0,0,1,1],
        '4':[0,1,0,0],
        '5':[0,1,0,1],
        '6':[0,1,1,0],
        '7':[0,1,1,1],
        '8':[1,0,0,0],
        '9':[1,0,0,1],
        'A':[1,0,1,0],
        'B':[1,0,1,1],
        'C':[1,1,0,0],
        'D':[1,1,0,1],
        'E':[1,1,1,0],
        'F':[1,1,1,1]}

fila = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

def multi(a1, a2):
    neg = 0
    if (a1[0][0] != a2[0][0]):
        neg = 1
#    print len(a1), len(a1[0]), len(a2), len(a2[0])
    for i in range(len(a2)):
        for j in range(len(a2)):
            if (a1[i][j] == -1) or ((abs(a1[i][j]-a2[i][j])-neg) != 0):
                return 0

    return 1

def correlate(org, par):
    suma = 0
    despx = len(org) - len(par) + 1
    despy = len(org[0]) - len(par) + 1
    dim = len(par)
#    if (dim == 2):
#        print ' * ',
#        print len(org), len(org[0]), despx, despy, dim
    for ix in range(despx):
        for jx in range(despy):
            aux = []
            for aux2 in org[ix:(dim+ix)]:
                aux.append(aux2[jx:(dim+jx)])

            valido = multi(aux, par)
#            if (dim == 2) and (valido == 1):
#                print '   ',
#                print ix, jx
#                print aux

            if (valido == 1):
                for x in range(dim):
                    for y in range(dim):
                        org[ix+x][jx+y] = -1
                suma += 1

    return suma

boards = {}
for i in range(1, 33):
    tablero = []
    par = fila[:i]
    impar = fila[1:i+1]
    for j in range(i):
        if (j%2 == 0):
            tablero.append(par)
        else:
            tablero.append(impar)

    boards[i] = tablero

for case in range(input()):
    M, N = map(int, raw_input().split())
    board = []
    for i in range(M):
        line = raw_input()
        temp = []
        for c in line:
            temp.extend(hexbin[c])
        board.append(temp)

    desp = min(M,N)
    cuenta_t = 0
    sol = 0
    res = []
    for i in range(desp, 1, -1):
        cuenta = correlate(board, boards[i])
        if (cuenta != 0):
            cuenta_t += cuenta*i*i
            sol += 1
            res.append(str(i) + ' ' + str(cuenta))
    if (cuenta_t < M*N):
        sol += 1
        res.append('1 ' + str(M*N-cuenta_t))

    print 'Case #%s: %d' % (case + 1, sol)
    for line in res:
        print line

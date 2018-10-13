#!/usr/bin/python

import sys


T = int(sys.stdin.readline())
for t in xrange(T):
    P = [int(x) for x in sys.stdin.readline().split()][0]
    N = int(2**(P-1))
    Mtmp = [P - int(x) for x in sys.stdin.readline().split()]
    M = []
    for i in xrange(N):
        M.append(max([Mtmp[2*i], Mtmp[2*i+1]]))
    p = [[]] * P
    for i in xrange(P):
        p[P-i-1] = [int(x) for x in sys.stdin.readline().split()]

    def copri(m, liv, a, b):
#        print "MMM", m
        MMAX = max(m[a:b])
        if MMAX <= 0:
            return 0
        if MMAX > P-liv:
            return -1
        if liv == P-1:
            if m[a] <= 0:
                esito = 0
            elif m[a] == 1:
                esito = p[P-1][a]
            else:
                esito = -1
#            print "SUBITO: ", m, liv, a, b, esito
            return esito

        nscaglioni = int(2**liv)
        inscagl = int(N/nscaglioni)
        if MMAX == P-liv:
            somma1a = -1
            somma1b = -1
        else:
            somma1a = copri(m, liv+1, a, (a+b)/2)
            if somma1a != -1: somma1b = copri(m, liv+1, (a+b)/2, b)
            else: somma1b = -1
        
        nm = [x for x in m[:a]] + [x-1 for x in m[a:b]] + [x for x in m[b:]]
        somma2a = copri(nm, liv+1, a, (a+b)/2)
        if somma2a != -1: somma2b = copri(nm, liv+1, (a+b)/2, b)
        else: somma2b = -1
        abb1 = somma1a != -1 and somma1b != -1
        abb2 = somma2a != -1 and somma2b != -1
        esito = -1
        if (abb1 and abb2): esito = min(somma1a+somma1b, somma2a+somma2b+p[liv][a/inscagl])
        elif abb1: esito = somma1a+somma1b
        elif abb2: esito = somma2a+somma2b+p[liv][a/inscagl]
#        print m, liv, a, b, esito
        return esito

    Tot = copri(M, 0, 0, N)
        

    print "Case #%d: %d" % (t+1, Tot)

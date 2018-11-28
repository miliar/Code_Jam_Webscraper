#!/usr/bin/env python

from sys import stdin

def f(R, k, N, G):
    D = range(N)

    for orig_i in xrange(N):
        i = orig_i
        this = 0
        groups = 0

        # lleno el tren
        while groups<N:
            if this+G[i] <= k:
                this += G[i]
                groups += 1
                i = (i+1) % N
            else:
                break

        D[orig_i] = (this, i)

    curr = 0
    sum = 0
    iba = {}
    early = False

    for i in xrange(R):
        if curr in iba.keys():
            early = True
            ct = i - iba[curr][0]
            cs = sum - iba[curr][1]
            break

        iba[curr] = (i, sum)

        sum += D[curr][0]
        curr = D[curr][1]

    if not early:
        return sum

    primero = iba[curr][1]
    falta = 0
    restantes = R-iba[curr][0]

    for i in xrange(restantes%ct):
        falta += D[curr][0]
        curr = D[curr][1]

    return primero + falta + (restantes/ct * cs)

T = int(stdin.readline())

for CASO in xrange(T):
    (R, k, N) = [int(x) for x in stdin.readline().split(" ")]
    G = [int(x) for x in stdin.readline().split(" ")]

    print "Case #%d: %d" % (CASO+1, f(R, k, N, G))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = int(raw_input())

for n in range(N):
    line = raw_input().split()

    C = int(line[0])
    comb = line[1:C+1]
    assert len(comb) == C
    D = int(line[C+1])
    opp = line[C+2:C+2+D]
    assert len(opp) == D
    N = int(line[-2])
    seq = line[-1]
    assert len(seq) == N

    # diccionario con los elementos opuestos de cada uno
    dopp = {}
    for a,b in opp:
        if a not in dopp:
            dopp[a] = set()
        if b not in dopp:
            dopp[b] = set()
        dopp[a].add(b)
        dopp[b].add(a)

    # diccionario de combinaciones
    dcomb = {}
    for a,b,c in comb:
        dcomb[a+b] = c
        dcomb[b+a] = c

    elems = []
    for elem in seq:
        # intenta combinar
        if len(elems) > 0:
            last = elems[-1]
            if last+elem in dcomb:
                elems[-1] = dcomb[last+elem]
                continue

        # el elemento actual es opuesto a alguno de la lista
        if elem in dopp and len(set(elems).intersection(dopp[elem])) > 0:
            elems = []
            continue

        elems.append(elem)

    print 'Case #{0}: {1}'.format(n+1, str(elems).replace("'", ""))


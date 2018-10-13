#!/bin/python

import sys

def solve_case(ng, ns, bs, notes, j):
    ok = 0
    notes.sort(reverse=True)
    for i in range(ng):
        if (notes[i] == 0):
            if bs == 0:
                ok += 1
                continue
            else:
                continue
        if (notes[i] / 3) >= bs:
            ok += 1
            continue
        notes[i] -= bs
        if notes[i] % 2 == 0:
            if (notes[i] / 2) >= bs -1:
                ok += 1
            elif (notes[i] / 2) >= bs -2 and ns:
                ok += 1
                ns -= 1
        else:
            notes[i] += 1
            lownote = (notes[i] / 2) -1
            if lownote >= bs -1:
                ok += 1
            elif lownote >= bs -2 and ns > 0:
                ok += 1
                ns -= 1
    print "Case #%d: %d" % (j+1, ok)

fs = open(sys.argv[1])
line = fs.readline()
nb_line = int(line)
for i in range(nb_line):
    line = fs.readline()
    tab = line.split()
    nb_googlers = int(tab[0])
    nb_surprising = int(tab[1])
    best_score = int(tab[2])
    notes = []
    for j in range(nb_googlers):
        notes.append(int(tab[j+3]))
    solve_case(nb_googlers, nb_surprising, best_score, notes, i)


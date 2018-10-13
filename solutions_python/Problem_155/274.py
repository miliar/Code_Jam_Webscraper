#!/usr/bin/python

# c.durr - google code jam - 2015
# Standing Ovation
#
# Pour chaque Si>9, on calcule la somme up = S0+S1+..S_{i-1}
# si up < i, alors il faut ajouter i-up personnes

import sys;

for idxCase in range(int(sys.stdin.readline())):
    tab = sys.stdin.readline().split()
    up = 0
    add = 0
    for i in range(int(tab[0])+1):
        si = int(tab[1][i])
        if si>0 and up<i:
            add += i-up
            up += add
        up += si
    print "Case #%d: %d"%(idxCase+1, add)

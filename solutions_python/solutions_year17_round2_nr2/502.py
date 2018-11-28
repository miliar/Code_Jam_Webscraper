#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

with open(sys.argv[1], 'r') as f:
    def compatible(a, b):
        if a == '' or b == '':
            return True
        elif a == 'R':
            return b in ['G', 'B', 'Y']
        elif a == 'Y':
            return b in ['B', 'R', 'V']
        elif a == 'B':
            return b in ['R', 'Y', 'O']
        elif a == 'G':
            return b in ['R']
        elif a == 'V':
            return b in ['Y']
        elif a == 'O':
            return b in ['B']
    def next(tab, pred, size):
        i = 0
        (n, color) = tab[i]
        while (not compatible(pred, color)) or n <= 0:
            i = i+1
            if i == size:
                return None, None
            (n, color) = tab[i]
        return color, i

    def reorganize(counts, first):
        counts.sort(reverse=True)
        if len(counts) > 1:
            if counts[1][1] == first and counts[0][0] == counts[1][0]:
                temp = counts[0]
                counts[0] = counts[1]
                counts[1] = temp
        return counts
    
    for n in range(int(f.readline())):
        N, R, O, Y, G, B, V = [int(i) for i in f.readline().split()]
        counts = [(R, 'R'), (G, 'G'), (O, 'O'), (B, 'B'), (Y, 'Y'), (V, 'V')]
        counts.sort(reverse=True)
        pred = ''
        res = ''
        for i in range(N):
            color, i = next(counts, pred, len(counts))
            if color == None:
                res = 'IMPOSSIBLE'
                break
            res += color
            pred = color
            counts[i] = (counts[i][0]-1, counts[i][1])
            counts = reorganize(counts, res[0])
        if not compatible(res[0], res[-1]):
            res = 'IMPOSSIBLE'
        print("Case #"+str(n+1)+": "+res)

#!/usr/bin/python

from sys import *

def read_int_list(f):
    l = f.readline().split('\n')[0].split(' ')
    l = map(int, l)
    return list(l)
 
def verso_basso(a):
    return a[0] > a[1]

def ordina(w, i, j):
    if w[i][0] < w[j][0]:
        return (w[i], w[j])
    else: return (w[j], w[i])

def inters(w, i, j):
    a, b = ordina(w, i, j)
    if verso_basso(a) and verso_basso(b):
        return a[1] > b[1]
    # il caso opposto?
    if not verso_basso(a) and verso_basso(b):
       return a[1] > b[1]
    if not verso_basso(a) and not verso_basso(b):
        return a[1] > b[1]
    return a[1] > b[1]


f = open(argv[1])
T = read_int_list(f)[0]
for t in range(T):
    w = []
    N = read_int_list(f)[0]
    for n in range(N):
        w.append(tuple(read_int_list(f)))
    #print(w)
    res = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if inters(w, i, j):
                res += 1
    res_str = "Case #%d: %d" %(t+1, res)
    print(res_str)



#!/usr/bin/python

import sys

def cambia(s, l):
    return int(s[l:] + s[:l])

def generaPermu(num):
    st = str(num)
    return set([ cambia(st,j) for j in range(1,len(st)) ])

with open(sys.argv[1]) as f:
    lines = f.readlines();

# Quito primera linea que suele ser el numero de casos que hay
# y se puede deducir del numero de lineas del fichero restantes
lines = lines[1:]

n_case = 0
for line in lines:
    A,B = [c for c in line.split(' ')]
    a = int(A)
    b = int(B)
    ret = 0
    for i in range(a, b):
        permu = generaPermu(i)
        for p in permu:
            if p > i and p <= b:
                ret += 1
    n_case += 1
    print("Case #"+str(n_case)+": "+str(ret))

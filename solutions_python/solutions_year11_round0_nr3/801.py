#!/usr/bin/env python

import sys

def xor(x,y): return x^y
def add(x,y): return x+y

filename = sys.argv[1]
f = open(filename, 'r')
T = int(f.readline())

fout = open("output", 'w') 

for i in range(T):
    N = int(f.readline())
    l = f.readline().split()
    l = [int(x) for x in l]
    xres = reduce(xor, l)
    if xres != 0:
        fout.write("Case #" + str(i+1) + ": " + "NO" + "\n")
    else:
        mres = reduce(add,l) - min(l)
        fout.write("Case #" + str(i+1) + ": " + str(mres) + "\n")

fout.close()



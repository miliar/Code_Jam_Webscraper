from sys import *
from math import *

A = 0
B = 1
NA = 2
NB = 3

def split(n):
    if n % 2 == 0:
        return str(int(n/2)) + " " + str(int(n/2-1))
    else:
        return str(int((n-1)/2)) + " " + str(int((n-1)/2))

def calc_ranges(n, k):
    r = [n, n+1, 1, 0]
    while True:
        if k > r[NA]+r[NB]:
            k -= (r[NA] + r[NB])
            if r[A] % 2 == 0:
                s = split(r[A])
                r = [ int(r[A]/2 - 1), int(r[A]/2), r[NA], r[NA]+2*r[NB] ]
            else:
                r = [ int(r[B]/2 - 1), int(r[B]/2), 2*r[NA]+r[NB], r[NB] ]
            if k == 0:
                return str(r[B]) + " " + str(r[A])
        elif k > r[NB]:
            return split(r[A])
        else:
            return split(r[B])

fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')
    
ncases = int(fin.readline())
for c in range(0, ncases):
    (n, k) = tuple([ int(x) for x in fin.readline().split() ])

    result = calc_ranges(n, k)
    fout.write("Case #" + str(c+1) + ": " + result + "\n")

fin.close()
fout.close()


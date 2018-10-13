#!/usr/bin/python

import sys

def gcd(a, b):
    while a != 0:
        if a > b:
            (a, b) = (b, a)
        else:
            (a, b) = (b % a, a)
    return b

f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    arr = f.readline().split()
    N = int(arr[0])
    times = map(int, arr[1:])
    times.sort()
    deltas = []
    for j in range(0, N - 1):
        deltas.append(times[j + 1] - times[j])
    G = reduce(gcd, deltas, 0)
    
    print "Case #%d: %d" % (i + 1, (G - (times[0] % G)) % G)


    

    

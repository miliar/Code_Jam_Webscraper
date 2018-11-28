from math import sqrt, pow, log, ceil, log10, floor
from sys import stdin, setrecursionlimit
import copy
import random

setrecursionlimit(100000)
debug = 0

def digits(N):
    l = []

    while N >= 1:
        l.append(N % 10)
        N = int(N / 10)

    l.reverse()        
    return l

def fromdigits(array):
    res = 0
    for d in array:
        res = res * 10 + d

    return res        

def spe(N):
    l = digits(N)
    l.reverse()
    return fromdigits(l)

def supersolve(N, cur):
    if N == 1:
        return 1

    return solve(N, cur)

def solve(N, cur):
    array = digits(N)
    already = {}

    while 1:
        newcur = []

        for c in cur:
            (val, cost) = c
            x0 = val + 1
            x1 = spe(val)

            if (x0 == N) or (x1 == N):
                return cost + 1

            if x0 not in already:
                already[x0] = 1
                newcur.append((x0, cost + 1))

            if x1 not in already:
                already[x1] = 1
                newcur.append((x1, cost + 1))

        cur = newcur

T = int(stdin.readline())

for i in range(1,T+1):
    
    N, = map(int, stdin.readline().split(' '))
    
    print "Case #" + str(i) + ":", 

    if debug:
        print
        print N

    cur = [(1,1)]
    rep = supersolve(N, cur)

    print rep



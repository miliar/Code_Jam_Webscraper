#!/usr/bin/python

from sys import stdin
from operator import mul

def f1(A, B, p):
    # keep typing
    y = 0
    # all A char correct
    q = reduce(mul, p)
    k = B - A + 1
    y += k * q
    # at least 1 incorrect
    q = 1.0 - q
    k += B + 1
    y += k * q
    #print 'f1',y
    return y

def p2(p, i):
    # prob of first i-1 all correct
    q = reduce(mul, p[:i], 1.0)
    if i < len(p):
        q *= 1.0 - p[i]
    return q

def f2(A, B, p):
    # back n times
    y = 1e30
    e = [0] * A
    for i in range(0, A + 1): # first incorrect char
        q = p2(p, i)
        for j in range(1, A + 1): # num of back pressed
            if A - j <= i: # all wrong char deleted
                k = j * 2 + B - A + 1
            else:
                k = j * 2 + B - A + 1 + B + 1
            #print 'i j q k',i,j,q,k
            e[j - 1] += k * q
    y = min(e)
    #print 'e',e
    #print 'f2',y
    return y

def f3(A, B, p):
    # press enter
    y = B + 2
    #print 'f3',y
    return y

T = int(stdin.readline())
for x in range(1, T + 1):
    A, B = map(int, stdin.readline().split())
    p = map(float, stdin.readline().split())
    y = min(f1(A, B, p), f2(A, B, p), f3(A, B, p))
    print "Case #%d: %.6f" % (x, y)


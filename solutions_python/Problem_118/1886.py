#!/usr/bin/env python
import sys
from math import sqrt

Ptable = range(0, 10000001)

def palindrome(n):
    on = n
    pn = 0
    while(n>=10):
        pn = pn*10 + n%10
        n = n / 10
    pn = pn*10 + n

    return on == pn

def solve(A, B):
    N = 0
    s = int(sqrt(A))
    e = int(sqrt(B))+1
    for i in xrange(s, e):
        i2 = i*i
        if i2<A:
            continue
        if i2>B:
            break

        if Ptable[i]:
            #print i2
            N = N + 1

    return N

def gen():
    for i in xrange(1, 1000001):
        if palindrome(i) and palindrome(i*i):
            Ptable[i] = 1
        else:
            Ptable[i] = 0

if __name__ == '__main__':
    gen()
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        r = sys.stdin.readline().split()
        A, B = [int(r[0]), int(r[1])]
        print 'Case #%d: %d' % (t, solve(A, B))

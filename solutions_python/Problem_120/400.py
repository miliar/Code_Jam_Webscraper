#!/usr/bin/python

# google code jam - c.durr - 2013
# Bullseye
# ad-hoc


def enough(n,r,t):
    return 2*n*r + n + 2*(n-1)*n <= t

def solve(r,t):
    n1 = 1
    while enough(n1,r,t):
        n1 *= 2
    n0 = n1/2
    while n0<n1:
        m = (n0+n1)/2
        if enough(m,r,t):
            n0 = m+1
        else:
            n1 = m
    return n0-1
    
T = int(raw_input())

for test in range(T):
    r,t = [int(i) for i in raw_input().split()]
    

    print 'Case #%d: %d' % (test+1, solve(r,t))

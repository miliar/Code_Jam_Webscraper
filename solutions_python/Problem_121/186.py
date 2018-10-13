#!/usr/bin/env python

n=int(raw_input())

def solver(fulle,e,r,n,v):
    max=0
    if n==1:
        return e*v[0]
    else:
        tempi=0
        for i in xrange(0,e+1):
            if e-i+r>=fulle:
                temp = solver(fulle,fulle,r,n-1,v[1:])+i*v[0]
            else:
                temp = solver(fulle,e-i+r,r,n-1,v[1:])+i*v[0]
            if temp>max:
                max=temp
        return max

for i in xrange(0,n):
    s=raw_input()
    (e,r,n)=[int(k) for k in s.split(' ')]
    s=raw_input()
    v=[int(k) for k in s.split(' ')]
    print('Case #%d: %d' % (i+1, solver(e,e,r,n,v)))

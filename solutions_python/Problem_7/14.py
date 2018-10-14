#!/usr/bin/python

from sol import *

c = next_int()

def gen(A,B,C,D,x0,y0,M,n):
    res = []
    
    X = x0
    Y = y0
    res.append( (X,Y) )
    for i in range(n):
      X = (A * X + B) % M
      Y = (C * Y + D) % M
      res.append( (X,Y) )

    return res



for v in range(1,c+1):
    n, A, B, C, D, x0, y0, M = [ next_int() for i in range(8) ]

    t = gen(A,B,C,D,x0,y0,M,n)

    res = 0

    for x in range(n):
        for y in range(x+1,n):
            for z in range(y+1,n):
                if (t[x][0] + t[y][0] + t[z][0]) % 3 == 0  and (t[x][1] + t[y][1] + t[z][1]) % 3 == 0:
                    res += 1


    print 'Case #%d: %d' % (v, res)

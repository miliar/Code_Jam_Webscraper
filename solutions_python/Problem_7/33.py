#!/usr/bin/python
import sys, time, collections
sys.setrecursionlimit(10096)

for caseno in range(input()):
    n, A, B, C, D, x0, y0, m  = map(int, raw_input().split())
    
    X = x0
    Y = y0
    dd = [ (X, Y) ]
    #dx = set([X])
    #dy = set([Y])
    for i in range(1, n):
        X = (A * X + B) % m
        Y = (C * Y + D) % m
        dd.append( (X, Y ) )
        #dx.add(X)
        #dy.add(Y)

    #print >> sys.stderr, dd, n
    s=0
    
    for i in range(len(dd)-2):
        x1, y1 = dd[i]
        for j in range(i+1, len(dd)-1):
            x2, y2 = dd[j]
            for k in range(j+1, len(dd)):
                x3, y3 = dd[k]
                m = ((x1 + x2 + x3) / 3.0, (y1 + y2 + y3) / 3.0)
                if (m[0] - int(m[0]) != 0.0) or (m[1] - int(m[1]) != 0.0):
                    continue
                m = (int(m[0]), int(m[1]))
                s+=1
                
  
    print "Case #%i: %i" %(caseno+1, s)

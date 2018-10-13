#!/usr/bin/env python
T = int(raw_input())
for i in xrange(T):
    sum = 0
    G = raw_input().split()
    N = int(G[0])
    S = int(G[1])
    p = int(G[2])
#    print N, S, p
    for j in xrange(N):
        n = int(G[j+3])
        x = n/3
        y = n%3
#        print "--",n, x, y
        if n == 0:
            if p == 0:
                sum += 1
            else:
                pass
        elif x >= p:
            sum += 1
        elif y>=1 and x+1 >= p:
            sum += 1
        elif S>0 and y==0 and x+1 >= p:
            S -= 1
            sum += 1
        elif S>0 and y==2 and x+2 >= p:
            S -= 1
            sum += 1
        
    print "Case #%d: %s" % (i+1, sum)
    
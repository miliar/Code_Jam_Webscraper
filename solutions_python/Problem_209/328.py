import numpy as np
import math



#------------------------------------
# Read inputs
t = int(raw_input())
for i in xrange(1, t + 1):
    N,K = [int(s) for s in raw_input().split(" ")]
    p = []
    for j in range(0,N):
        tp = [int(s) for s in raw_input().split(" ")]
        p.append((math.pi*tp[0]*tp[0], 2*math.pi*tp[0]*tp[1]))
    p = sorted(p, reverse=True)

    max_a = []
    for j1 in range(0,N-K+1):
        max_a.append(0)
        max_a[-1] += (p[j1][0]+p[j1][1])
        tp = []
        for j2 in range(j1+1,N):
            tp.append(p[j2][1])
        tp = sorted(tp, reverse=True)
        for j2 in range(0,K-1):
            max_a[-1] += tp[j2]

    print "Case #{}:".format(i) ,
    print '%.14f' % max(max_a)

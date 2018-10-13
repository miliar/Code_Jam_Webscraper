#!/bin/python

import sys

inf = sys.stdin
T = int(inf.readline())
    
for t in range(T):
    N = int(inf.readline())
    lines = []
    points = set()
    for n in range(N):
        lines.append(map(int, inf.readline().split()))
        for l in lines:
            crossers = [l2 for l2 in lines if ((l2[0] > l[0] and l2[1] < l[1]) or (l2[0] < l[0] and l2[1] > l[1]))]
            for x in crossers:
                points.add('%d.%d' % (l[0], x[0]))
        
    #print points
    print 'Case #%d: %s' % (t+1, len(points) / 2)

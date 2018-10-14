#!/usr/bin/python

import sys

f = sys.stdin

T = int(f.readline().strip())

for t in range(T):
    n = int(f.readline().strip())
    d = []
    ret = []
    for nn in range(n):
        d.append([float(s) for s in f.readline().strip().split(' ')])
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if (d[i][0]-d[j][0])*(d[i][1]-d[j][1]) < 0:
                tt = (d[i][1]-d[j][1])/(d[j][0]-d[i][0])
                x = 1.0/(1+tt)
                y = d[i][0] + (d[i][1]-d[i][0])/(1+tt)
                flag = True
                for xx,yy in ret:
                    if (abs(xx-x) < 0.000001) and (abs(yy-y) < 0.000001):
                        flag = False
                if flag:
                    ret.append((x,y))
    print "Case #%d: %d" % (t+1, len(ret))

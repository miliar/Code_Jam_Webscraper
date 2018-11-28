import sys
from math import pi
sin = sys.stdin
T = int(sin.readline().strip())
for i in xrange(1, T+1):
    N, K = map(int, sin.readline().strip().split())
    RH = []
    for j in xrange(N):
        Ri, Hi = map(int, sin.readline().strip().split())
        RH.append((Ri, Hi))
    RHs = sorted(RH, key=lambda (r, h): r*10**6+h)
    #print N, K, RHs
    combs = [[x] for x in xrange(N)]
    areas = []
    max_area = 0
    for cidx, c in enumerate(combs):
        if len(c) < K:
            for k in xrange(N):
                if k not in c:
                    d = [x for x in c]
                    d.append(k)
                    combs.append(d)
        else:
            area = 0
            for kidx, k in enumerate(c):
                r, h = RH[k]
                if kidx == len(c) - 1:
                    area += pi*r**2 + 2*pi*r*h
                else:
                    nr = RH[c[kidx+1]][0]
                    area += 2*pi*r*h + (pi*r**2 - pi*nr**2)
            max_area = max(area, max_area)
    mar = '{0:.6f}'.format(round(max_area*10**6)/10**6)
    print 'Case #{0}: {1}'.format(i, max_area)

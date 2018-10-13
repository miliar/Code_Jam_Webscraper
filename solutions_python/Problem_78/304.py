#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def pos(n, pd, pg):
    if pg == 0:
        if pd == 0:
            return 'Possible'
        else:
            return 'Broken'
    if pg == 100:
        if pd == 100:
            return 'Possible'
        else:
            return 'Broken'
    ppd = []
    for i in range(1, n+1):
        wd = i * pd / 100.0
        if abs(int(wd) - wd) < 1e-6:
            ppd.append((int(wd), i))
    if ppd:
        print n, pd, pg, ppd
        for w, a in ppd:
            lim = math.ceil((a - w + 1)/(100.0 - pg)) * pg
            j = 0
            while j > -1:
                wg = 100.0 * (w + j) / pg
                if abs(int(wg) - wg) < 1e-6:
                    print wg, w+j, lim
                    if lim < w + j:
                        return 'Broken'
                    if wg >= a + j:
                        return 'Possible'
                j += 1
    else:
        return 'Broken'

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    n, pd, pg = [int(x) for x in l]
    #print 'Case #%d: %s' % (i, pos(n, pd, pg))
    g.write('Case #%d: %s\n' % (i, pos(n, pd, pg)))

g.close()

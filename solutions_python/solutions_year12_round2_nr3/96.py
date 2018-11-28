#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

# http://wiki.python.org/moin/Powerful%20Python%20One-Liners
ss = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

def esum(l):
    l.pop(0)
    lss = ss(l)
    lsum = [sum(x) for x in lss]
    ssum = set(lsum)
    if len(lsum) == len(ssum):
        return ['Impossible']
    else:
        tmp = []
        for s in lsum:
            if s in tmp:
                break
            else:
                tmp.append(s)
        ret = []
        for x in lss:
            if sum(x) == s:
                ret.append(' '.join([str(i) for i in x]))
                if len(ret) == 2:
                    break
        return ret           

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split()
    l = [int(x) for x in l]
    ret = esum(l)
    #print 'Case #%d: \n%s' % (i, '\n'.join(ret))
    g.write('Case #%d: \n%s\n' % (i, '\n'.join(ret)))

g.close()

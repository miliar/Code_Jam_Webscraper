import psyco
psyco.full()
import sys

import re

def calc(cs,ops,ser):
    csd = {}
    for c in cs:
        bp = ''.join(sorted(c[0:2]))
        csd[bp] = c[2]
    opsd = {}
    for o in ops:
        oa,ob = o
        if not opsd.has_key(oa):
            opsd[oa] = set()
        if not opsd.has_key(ob):
            opsd[ob] = set()
        opsd[oa].add(ob)
        opsd[ob].add(oa)
    
    res = [ser[0]]
    #print 'asfasdf', ser
    for s in ser[1:]:
        ok = False
        if len(res) > 0:
            bp = ''.join(sorted(res[-1]+s))
            if csd.has_key(bp):
                res[-1] = csd[bp] # combine
                ok = True
                cs = csd[bp]
            else:
                cs = s
            if opsd.has_key(cs):
                reset = False
                for c in res:
                    if c in opsd[cs]:
                        reset = True
                        break
                if reset:
                    res = [] # clear due to oppose
                    ok = True
        if not ok:
            res.append(s)
    #print 'qqq', res
    return "[" + ', '.join(res) + "]"


def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    sets = re.split(r'\d+', line)[1:]
    #print "\n",line, "--------", sets
    bs,ops,ser = [a.strip().split() for a in sets]
    ser = ser[0]
    
    v = calc(bs, ops, ser)
    print "Case #%d: %s" % (cn,v)
    cn += 1

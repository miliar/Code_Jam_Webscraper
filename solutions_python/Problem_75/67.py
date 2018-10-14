# -*- coding: utf-8 -*-
def popn(line):
    n = int(line[0])
    return (line[1:n+1], line[n+1:])
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    line = fin.readline().split()
    pairs, line = popn(line)
    opposed, line = popn(line)
    seq = line[1]
    replace = {}
    for pair in pairs:
        a,b,c = list(pair)
        replace[(a,b)] = c
        replace[(b,a)] = c
    destroy = set()
    for o in opposed:
        a,b = list(o)
        destroy.add((a,b))
        destroy.add((b,a))
    #print replace, destroy, seq
    l = []
    for c in seq:
        if not l:
            l.append(c)
        else:
            k = (l[-1], c)
            if k in replace:
                l[-1] = replace[k]
            else:
                d = False
                for cc in l:
                    if (cc,c) in destroy:
                        d = True
                        break
                if d:
                    l = []
                else:
                    l.append(c)
                        
    print "Case #%d: %s" % (case, str(l).replace("'",""))

#!/usr/bin/env python2.6
import sys

def enlarge(ns):
    k = min(n for n in ns if n > 0)
    del ns[ns.index(k)]
    ns.sort()
    ns.insert(0, 0)
    ns.insert(0, k)
    
def next_number(n):
    ns = [int(v) for v in n]
    for i in range(len(n) - 2, -1, -1):
        p = ns[i]
        try:
            next, next_pos = min((k, -(j + i + 1)) for j, k in enumerate(ns[i+1:]) if k > p)
        except ValueError:
            continue
        next_pos = -next_pos
        ns[i], ns[next_pos] = ns[next_pos], ns[i]
        ns = ns[:i+1] + sorted(ns[i+1:])
        break
    else:
        enlarge(ns)
    return "".join(str(p) for p in ns)
        
        
with open(sys.argv[1], "r") as f:
    tests = int(f.readline().strip())
    numbers = [f.readline().strip() for k in range(tests)]


for i, n in enumerate(numbers):
    print "Case #%d: %s" % (i + 1, next_number(n))


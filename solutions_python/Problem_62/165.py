#/usr/bin/python


def solve(h):
    starts = h.keys()
    starts.sort()
    n = len(starts)
    ct = 0
    for i in xrange(n):
        for j in xrange(i + 1, n):
            if h[starts[i]] > h[starts[j]]:
                ct += 1
    return ct

import sys
f = open(sys.argv[1])
num_cases = int(f.next())

for caseno in xrange(1, num_cases + 1):
    h = {}
    num_wires = int(f.next())
    for i in xrange(num_wires):
        s, t = map(int, f.next().split(' '))
        h[s] = t
    print 'Case #%i: %i'%(caseno, solve(h))

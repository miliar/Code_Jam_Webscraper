#!/usr/bin/env python

def iscons(l):
    return l not in ['a', 'e', 'i', 'o', 'u']

def ncons(name, n, i):
    return all(name[i:i+n])

def nvalue(name, n):
    name = [iscons(l) for l in name]
    starts = [i for i in xrange(len(name)-n+1) if ncons(name, n, i)]
    if starts == []:
        return 0
    ln = len(name)
    nval = (starts[0] + 1) * (ln - starts[0] - n + 1)
    for i in xrange(1, len(starts)):
        nval += (starts[i] - starts[i-1]) * (ln - starts[i] - n + 1)
    return nval

t = int(raw_input())

for caseno in xrange(1, t+1):
    name, nstr = raw_input().split()
    n = int(nstr)
    print "Case #%d: %d" % (caseno, nvalue(name, n))

#!/usr/bin/python

import sys

G = [
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv',
]
E = [
    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up',
]

g2e = { 'z':'q', 'q':'z' }
g2e.update((gl, el) for g, e in zip(G, E) for gl, el in zip(g, e))

T = int(next(sys.stdin))
for x in xrange(1, T+1):
    print "Case #%d: %s" % (x, "".join(g2e[l] for l in next(sys.stdin).strip()))

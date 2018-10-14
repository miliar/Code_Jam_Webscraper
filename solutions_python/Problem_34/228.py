from __future__ import with_statement
import sys
import re

with open(sys.argv[1]) as f:
    L, D, N = map(int, f.readline().split())

    words = [f.readline().strip() for w in xrange(D)]
    cases = [f.readline().strip() for c in xrange(N)]

    regexps = [re.compile(re.sub(r'\((.*?)\)', r'[\1]', c, L))
               for c in cases]

    for i, r in enumerate(regexps):
        print "Case #%d: %d" % (i+1, len(filter(r.search, words)))
        

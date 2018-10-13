#!/usr/bin/env python

import sys
import re
from sets import Set

f = open(sys.argv[1], 'r')
(L, D, N) = [int(x) for x in f.readline().split(' ')]
valid_words = Set([f.readline()[0:L] for i in range(D)])

for i in range(N):
    p = f.readline().rstrip()
    p = p.replace('(','[').replace(')',']')
    cre = re.compile(p)
    cx = 0
    for w in valid_words:
        if cre.match(w):
            cx += 1
    print "Case #%d: %d" % (i + 1, cx)

f.close()

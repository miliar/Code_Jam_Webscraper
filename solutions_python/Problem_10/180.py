from __future__ import with_statement

import sys

with open(sys.argv[1]) as f:
    n = int(f.readline())
    for c in range(1,n+1):
        (p, k, l) = map(int, f.readline().split(' '))
        lts = map(int, f.readline().split(' '))
        lts.sort(reverse=True)
#        print "lts: %s" % lts
        res = 0
        i = 0
        for pos in range(p):
            for key in range(k):
#                i =  key*p+pos
#                print "key: %s, pos: %s, i: %s" % (key, pos, i)
                if i < l:
#                    print "lts[i]: %s, lts[i] * (pos+1): %s" % (lts[i], lts[i] * (pos+1))
                    res += lts[i] * (pos+1)
                    i += 1
        print "Case #%s: %s" % (c, res)

#!/usr/bin/env python
"""
Google Code Jam: Saving the Universe
http://code.google.com/codejam/contest/dashboard?c=agdjb2RlamFtcg8LEghjb250ZXN0cxjqOQw

n = number of cases
ss = search engines
qs = queries
"""

n = input()
for i in xrange(n):
    ss = [raw_input() for x in xrange(input())]
    qs = [raw_input() for x in xrange(input())]
    ssm = dict.fromkeys(ss)

    changes = 0
    curs = None
    leftss = ssm.copy()
    for q in qs:
        if q in leftss: del leftss[q]
        if not leftss:
            changes += 1
            leftss.update(ssm)
            del leftss[q]
    print "Case #%d: %d" % (i+1, changes)


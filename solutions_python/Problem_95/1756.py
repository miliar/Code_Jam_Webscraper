#!/usr/bin/env python

import sys

g="y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s="a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

gte = dict(zip(g,s))
gte['z']='q'

cases_no = int(sys.stdin.readline())
for case_no in xrange(cases_no):
    print "Case #%d: %s" % (case_no+1, ''.join(map(lambda c: gte[c], sys.stdin.readline()[:-1])))


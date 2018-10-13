#!/usr/bin/python

import sys
import string

trans = string.maketrans('ynficwlbkuomxsevzpdrjgthaq',
                         'abcdefghijklmnopqrstuvwxyz')
cases = sys.stdin.readline()
n = int(cases)
for i in xrange(1, n+1):
    line = sys.stdin.readline()
    line = line.rstrip('\n')
    print "Case #%d: %s" % (i, line.translate(trans))

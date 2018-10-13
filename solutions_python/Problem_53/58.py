#!/usr/bin/env python

import sys

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    x, y = map(long, inputfile.readline().strip().split())

    mask = (1 << x) - 1
    if (y & mask) == mask:
	M = 'ON'
    else:
	M = 'OFF'

    # output is Case #N: M
    print "Case #%d: %s" % (case, M)

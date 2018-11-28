#!/usr/bin/python

from sys import stdin as st

te = int(st.readline())

for i in xrange(1, te + 1):
    s = st.readline()
    n, t = s.split()
    n = int(n) + 1

    ac = 0
    xc = 0
    for i2 in xrange(n):
	x = i2 - ac
	if x < 0:
	    x = 0
	xc += x
	ac += int(t[i2]) + x


    print "Case #%d: %d" % (i, xc)




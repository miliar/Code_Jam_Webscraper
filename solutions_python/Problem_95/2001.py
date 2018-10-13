#!/usr/bin/env python
import sys
english="abcdefghijklmnopqrstuvwxyz "
google ="ynficwlbkuomxsevzpdrjgthaq "
indata = open(sys.argv[1], 'r').readlines()
indata = [x.strip() for x in indata]
tlines = int(indata[0])
for i in range(1, tlines+1):
	line = indata[i]
	engline = "".join([english[google.find(x)] for x in line])
	print "Case #%d: %s" % (i, engline)

#!/bin/env python

import sys,re

lines = sys.stdin.readlines()
L,D,N = [long(x) for x in lines[0].strip().split(" ")]
words = [w.strip() for w in lines[1:1+D]]
tests = [t.strip() for t in lines[1+D:1+D+N]]
for x in range(len(tests)):
	t = tests[x]
	t = t.replace("(","[")
	t = t.replace(")","]")
	p = re.compile(t)
	k = len([w for w in words if p.match(w)])
	print "Case #%d: %d" % (x+1,k)

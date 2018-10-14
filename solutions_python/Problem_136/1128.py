#!/usr/bin/env python

n = int(raw_input())
for i in range(n):
	C,F,X = tuple(map(float,raw_input().strip().split()))
	r = 2.0
	t = 0.0
	twf = 0.0
	if (C/r) > (X/r):
		twf = X/r
		print "Case #"+str(i+1)+":",twf
		continue
	while True:
		twf = t
		t += C/r
		twf += X/r
		r += F
		if t+X/r > twf:
                	print "Case #"+str(i+1)+": %.7f" % twf
                	break

#!/usr/bin/python3
import math

t = input()
t = int(t)
for test in range(t):
	c, f, x = (float(x) for x in input().split(" "))
	n = math.floor((f*x-f*c-2*c)/(c*f))
	if (n < 0):
		res = x/2
	else:
		res = x/((n+1)*f+2)
		for i in range(n+1):
			res += c/(2+i*f)
	print ("Case #%d: %.7f" % (test+1, res))
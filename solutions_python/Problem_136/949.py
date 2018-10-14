#!/usr/bin/python3

t = int(input())
for i in range(t):
	c, f, x = map(float, input().split())
	r = 2.0
	s = 0.0
	while c/r + x/(r+f) < x/r:
		s += c/r
		r += f
	s += x/r
	print('Case #%d: %.7f' % (i+1, s))

#!/usr/bin/python

T = int(raw_input())

for tc in range(1, T + 1):
	n = raw_input()
	s = raw_input()
	a = map(lambda x: int(x) - 1, s.split())
	res = 0
	for i in range(len(a)):
		if a[i] == -1: continue
		x = a[i]
		a[i] = -1
		l = 1
		while x != i:
			l += 1
			nx = a[x]
			a[x] = -1
			x = nx
		
		if l > 1: res += l
	print "Case #%d: %d.000000" % (tc, res)

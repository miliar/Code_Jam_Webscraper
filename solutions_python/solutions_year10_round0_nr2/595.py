#!/usr/bin/env python

def gcd(a, b):
	while b > 0: a,b = b,a % b
	return a

c = int(raw_input())
for case in xrange(1,c + 1):
	t = [int(x) for x in raw_input().split()][1:]
	n = len(t)
	T = abs(t[0] - t[1])
	for i in xrange(n-1):
		for j in xrange(i+1, n):
			T = gcd(T, abs(t[i] - t[j]))
	k = min(t) / T
	if min(t) % T != 0:
		k += 1
	print "Case #%d: %d" % (case, k * T - min(t))

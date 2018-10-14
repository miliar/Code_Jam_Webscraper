#!/usr/bin/python

def gcd(a, b):
	while a != 0:
		(a, b) = (b % a, a)
	return b

T = int(raw_input())
for cas in range(1, T + 1):
	t = str.split(raw_input())
	n = int(t[0])
	a = []
	for i in range(1, n + 1):
		a.append(int(t[i]))
	for i in range(1, n):
		for j in range(1, n):
			if a[j - 1] > a[j]:
				(a[j - 1], a[j]) = (a[j], a[j - 1])
	p = a[1] - a[0]
	for i in range(2, n):
		t = a[i] - a[i - 1]
		p = gcd(p, t)
	p = (p - a[0] % p) % p
	print "Case #", cas, ": ", p

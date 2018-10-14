#!/usr/bin/python

def gcd(a, b):
	if (b > 0):
		return gcd(b, a%b)
	else:
		return a

T = int(raw_input())
for t in range(T):
	l = [int(item) for item in raw_input().split()][1:]
	p = abs(l[1] - l[0])
	for i in range(2, len(l)):
		p = gcd(p, abs(l[i] - l[0]))
	ans = p - ((l[0] - 1)%p + 1)
	print "Case #" + str(t + 1) + ": " + str(ans)
	
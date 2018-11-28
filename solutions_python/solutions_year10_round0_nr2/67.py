#!/usr/bin/python

def mdc(a, b):
	if a < 0: return mdc(-a, b)
	if b < 0: return mdc(a, -b)
	if b > a: return mdc(b, a)
	if b == 0: return a
	return mdc(b, a%b)

C = int(raw_input())
for i in xrange(C):
	l = [int(x) for x in raw_input().split(" ")]
	N = l[0]
	l = l[1:]
	l.sort()
	m = l[1]-l[0]
	for j in xrange(N):
		for k in xrange(j):
			m = mdc(m, l[j]-l[k])

	print "Case #%d: %d" % (i+1, -l[0] % m)

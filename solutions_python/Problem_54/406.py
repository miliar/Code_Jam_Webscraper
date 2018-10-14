#!/usr/bin/python
from sys import stdin
import gmpy

C = int(stdin.readline())
for c in xrange(1, C+1):
	sa = stdin.readline().split()
	sa.pop(0)
	a = sorted(gmpy.mpz(x) for x in sa)
	aa = a[1:]
	diffs = [aa[i] - a[i] for i in xrange(len(aa))]
	gcdiff = reduce(gmpy.gcd, diffs, 0)
	more = [(gcdiff - x % gcdiff) % gcdiff for x in a]
	more = (gcdiff - a[0] % gcdiff) % gcdiff
	print 'Case #%d: %s' % (c, gmpy.digits(more))

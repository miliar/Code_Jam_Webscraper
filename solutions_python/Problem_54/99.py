#!/usr/bin/env python2.6

import sys, fractions

num = int(sys.stdin.readline());

for cs in range(1, num + 1):
	num = map(int, sys.stdin.readline().split()[1:])
	gcd = abs(num[0] - num[1])
	for i in range(2, len(num)):
		gcd = fractions.gcd(gcd, abs(num[i] - num[i-1]))
	
	print "Case #%d: %d"%(cs, (gcd - num[0] % gcd) % gcd)

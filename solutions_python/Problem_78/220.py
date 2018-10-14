#!/usr/bin/python
import sys

lines = sys.stdin.read().split('\n')[1:]

def gcd(n):
	for x in (100, 50, 25, 20, 10, 5, 4, 2, 1):
		if n % x == 0:
			return x
case = 0
while lines:
	case += 1
	line = lines.pop(0)
	if not line:
		continue

	n, pd, pg = [int(x) for x in line.split()]

	if (pg <= 0) and pd > 0:
		result = 'Broken'
	elif (pg >= 100) and pd < 100:
		result = 'Broken'
	elif (max(100/gcd(pd), 100/gcd(100-pd)) > n):
		result = 'Broken'
	else:
		result = 'Possible'

	print "Case #%d: %s" % (case, result)

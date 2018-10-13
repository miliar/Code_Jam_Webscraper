#!/usr/bin/python
import sys, operator, time

lines = sys.stdin.read().split('\n')[1:]

case = 0

def _harmony(jeff, fs):
	for f in fs:
		if jeff % f != 0 and f % jeff != 0:
			return False
	return True

def harmony(l, h, fs):
	for jeff in xrange(l, h + 1):
		if _harmony(jeff, fs):
			return jeff
	
	return False

while lines:
	case += 1
	line = lines.pop(0)
	if not line:
		continue

	n, l, h  = [int(x) for x in line.split()]
	fs = [int(x) for x in lines.pop(0).split()]

	result = harmony(l, h, fs)

	if result:
		print "Case #%d: %d" % (case, result)
	else:
		print "Case #%d: NO" % case






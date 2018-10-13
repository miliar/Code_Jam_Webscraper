from sys import *

def snappy(_, n, k):
	print "Case #%d:" %(_ + 1),
	if (k % 2 ** n) == (2 ** n - 1):
		print "ON",
	else:
		print "OFF",
	print

cases = int(raw_input())
for _ in xrange(cases):
	n, k = stdin.readline().split()
	snappy(_, int(n), int(k))


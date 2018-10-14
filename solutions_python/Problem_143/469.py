import psyco
import sys
import itertools
import re

psyco.full()

test_input = r'''6
3 4 2
4 5 2
7 8 5
45 56 35
103 143 88
1000000 1000000 1000000'''.split('\n')

DEBUG = False

KNOWN = {

}

def debug(s):
	if not DEBUG:
		return
	sys.stderr.write(str(s) + '\n')

def readline():
	if DEBUG:
		return test_input.pop(0)
	return raw_input()				


def case(casenum):

	# old machine will always generate 0 -> (A-1)	 A > x >= 0
	# new machine will always generate 0 -> (B-1)	 B > y >= 0
	# buy all < K
	# given A, B, K, calculate n pairs that win
	
	a, b, k = map(int, readline().split())
	
	pairs = 0
	
	for x in xrange(a):
		for y in xrange(b):
			if (x & y) < k:
				pairs += 1
	
	
	output = pairs
	
	print "Case #%d: %s" % (casenum, output)
	
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()

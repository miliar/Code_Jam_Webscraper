from copy import deepcopy
import plex

from mpmath import *
mp.dps = 20
import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

def debug(message):
	if sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

for tc in xrange(t):
	debug("case %d" % (tc+1))
	a, b, k = [int(x) for x in inp.readline().split()]
	debug("%d %d %d" % (a, b, k))
	n = 0
	for i in xrange(a):
		for j in xrange(b):
			if (i & j)<k:
				n += 1
	print_case(tc+1, n)
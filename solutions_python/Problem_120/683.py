import re
import sys
import math

inp = open("in.txt")
out = open("out.txt","w+")


def solve():
	cases = int(inp.readline())
	for case in xrange(cases):
		radius, paint = [int(x) for x in inp.readline().split()]
		
		rings = 0
		while True:
			required = paint_required(radius)
			radius += 2
			if paint - required >=0:
				paint = paint - required
				rings += 1
			else:
				break
		
		write_case(case + 1, rings)

def paint_required(radius):
	return ((radius + 1) ** 2) - radius **2

def write_case(case, *args):
	print "printing case", case, args
	out.write("Case #%s: %s\n" % (case, " ".join([str(a) for a in args])))
	
solve()
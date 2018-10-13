import re
import sys
import math

inp = open("in.txt")
out = open("out.txt","w+")

cache = {}

def solve():
	cases = int(inp.readline())
	for case in xrange(cases):
		inputs = [int(x) for x in inp.readline().split()]
		
		found = []
		print inputs
		a, b = inputs
	
		n = 0
		sqa = a ** (1/2.0)
		sqb = b ** (1/2.0)
		
		for i in xrange(int(math.ceil(sqa)), int(math.floor(sqb +1))):
			if is_fair(i) and is_fair(i**2):
				found.append(i)
				n += 1
		print "found", found
		write_case(case + 1, str(n))

def is_fair(n):
	if type(n) is int:
		return is_fair(str(n))
	else:
		return n == n[::-1]

def write_case(case, *args):
	print "printing case", case, args
	out.write("Case #%s: %s\n" % (case, " ".join([str(a) for a in args])))
	
solve()
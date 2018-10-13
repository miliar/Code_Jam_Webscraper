from mpmath import *
mp.dps = 20
import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out

t = int(inp.readline())

def print_case(case, result):
	if isinstance(result, list):
		result = " ".join([str(x) for x in result])
	print "Case #%d: %s" % (case, str(result))


for tc in xrange(t):
	b = int(inp.readline())
	p1 = sorted([float(x) for x in inp.readline().split()])
	p2 = sorted([float(x) for x in inp.readline().split()])
	p1d = list(p1)
	p2d = list(p2)
	w = 0
	dw = 0
	for i in xrange(b):
		if p1[0] < p2[0]:
			del p1[0]
			del p2[-1]
		else:
			del p1[0]
			del p2[0]
			dw += 1
		
		if p1d[-1] > p2d[-1]:
			del p1d[-1]
			del p2d[0]
			w += 1
		else:
			del p1d[-1]
			del p2d[-1]
	
	print_case(tc+1, [dw, w])
		
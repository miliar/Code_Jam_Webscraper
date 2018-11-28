from itertools import *

infile = "C-large.in"

lines = [s.rstrip() for s in open(infile, "rb").readlines()]
NCases=int(lines[0])

for i in range(NCases):
	values = [int(c) for c in lines[i * 2 + 2].split(" ")]
	if reduce(lambda x, y: x^y, values) != 0:
		result = "NO"
	else:
		svalues = sorted(values)
		result = str(reduce(lambda x, y: x+y, svalues[1:]))
	print "Case #%d: %s" % (i+1, result)

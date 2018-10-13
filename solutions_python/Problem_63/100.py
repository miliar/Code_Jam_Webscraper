#!/usr/bin/env python
# Google CodeJam Round 1C-B

from math import log, ceil
def main(L,P,C):
	if L*C>=P: return 0
	m = log(P/L,C)
	n = log(m,2)
	return int(ceil(n))
	
if __name__ == "__main__":
	prog = main
	import sys
	for filename in sys.argv[1:]:
		f = open(filename)
		line = f.readline()
		for case in range(int(line)):
			[L, P, C] = [float(value) for value in f.readline().split()[:3]]
			print "Case #%i: %s" % (case+1, prog(L,P,C))
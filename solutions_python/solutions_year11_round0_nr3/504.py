#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

#
def int2bin(n, numdigits):
	return [((n >> y) & 1) for y in range(numdigits-1, -1, -1)]

def binsum(a, b):
	return [sum(x)%2 for x in zip(a, b)]

#int2bin(n, 21)

numcases = int(indata[0].strip())
lines = [x.strip().split(' ') for x in indata[1:]]

for j in range(0, numcases):
	numpiles = int(lines[2*j][0])
	case = lines[2*j+1]
	assert(numpiles == len(case))
	#print case

	total = int2bin(0, 21)
	for i in range(0, numpiles):
		total = binsum(total, int2bin(int(case[i]), 21))
	#print total
	if total == int2bin(0, 21):
		#We're good, matches
		print "Case #" + str(j+1) + ": " + str(sum(sorted([int(x) for x in case])[1:]))
	else:
		print "Case #" + str(j+1) + ": " + "NO"

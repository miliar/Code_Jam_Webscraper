

import sys
import math

f = open("B-small-attempt0.in")

f2 = open("outpb", "w")
testcases = int(f.readline())


for i in xrange(testcases):
	peeps = int(f.readline())
	pancakes = map(lambda x: (int(x),1), f.readline().split())
	pancakes.sort(key=lambda x: x[0], reverse=True)
	maxval = max(pancakes, key=lambda x: x[0])[0]
	curbest = maxval
	flips = 0
	for j in xrange(maxval):
		pancakes[0] = (pancakes[0][0], pancakes[0][1] + 1)
		pancakes.sort(key=lambda x: math.ceil(float(x[0])/x[1]), reverse=True)
		flips += 1
		newmaxval = math.ceil(float(pancakes[0][0])/pancakes[0][1]) + flips
		curbest = min(newmaxval, curbest)
	print "Case #" + str(i+1) + ": " + str(int(curbest))


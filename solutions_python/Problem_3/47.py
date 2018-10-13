from __future__ import with_statement
from math import *

def aasectorarea(x, y, r):
	if x**2 + y**2 >= r**2:
		return 0.0
	alpha = acos(y/r)
	beta = acos(x/r)
	usegmentArea = r**2 * (2 * beta - sin(2 * beta)) / 4  
	rsegmentArea = r**2 * (2 * alpha - sin(2 * alpha)) / 4
	blarea = x * y
	quarterarea = pi * r**2 / 4
	return usegmentArea + rsegmentArea + blarea - quarterarea
	
print aasectorarea(0.1, 0.1, 1)

def intersect(x1, y1, x2, y2, r):
	if x1**2 + y1**2 >= r**2:
		return 0.0
	if x2**2 + y2**2 <= r**2:
		return None
	return aasectorarea(x1, y1, r) - aasectorarea(x1, y2, r) - aasectorarea(x2, y1, r) 

def processFile(fin, outf):
	
	numCases = int(fin.readline())
	for caseNumber in xrange(1, numCases + 1):
		f, R, t, r, g = map(float, fin.readline().strip().split())
		quarterarea = pi * R**2 / 4
		step = g + 2 * r
		startOffset = r + f
		endOffset = r + g - f
		effectiveRadius = R - t - f
		print startOffset, endOffset, effectiveRadius
		freeSq = 0.0
		wholeSquares = 0
		if startOffset < endOffset and effectiveRadius > 0:
			for x in xrange(1000000):
				stopFlag = True
				for y in xrange(10000000):
					x1 = startOffset + step*x
					y1 = startOffset + step*y
					x2 = endOffset + step*x
					y2 = endOffset + step*y
					ia = intersect(x1, y1, x2, y2, effectiveRadius)
					if ia is None:
						wholeSquares += 1
						stopFlag = False
					elif ia > 0:
						freeSq += ia
						stopFlag = False
					else:
						break
				if stopFlag: 
					break 
			freeSq += wholeSquares * ((endOffset - startOffset)**2)
			print wholeSquares 
		
		s = "Case #" + str(caseNumber) + ": " + ("%1.6f" % (1.0 - freeSq / quarterarea))
		print s
		print >> outf, s

	


input = "C-large"
with open(input + ".in") as f:
	with open(input + ".out", "w") as fout:
		processFile(f, fout)
print "OK!"
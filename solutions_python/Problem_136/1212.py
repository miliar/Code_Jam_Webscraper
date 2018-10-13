import pdb
import sys
import getopt
from collections import defaultdict

def getN(C, F, X, count):
	n = 1
	while (True):
		k = 1.0*(C*(2 + n*F) - X*F) / ((2 + n*F)*(2 + (n-1)*F))
		if (k > 0):
			break
		n += 1
	if (n == 1):
		retsum = X/2.0
	if (n > 1):
		s1 = [C/(2.0 + p*F) for p in xrange(n-1)]
		s1 = sum(s1)
		s2 = X / (2.0 + (n-1)*F)
		retsum = s1 + s2
	strout = "Case #"+str(count)+": "+"%.7f" % retsum
	return strout



def main():
	fname = sys.argv[1]
	fname = sys.argv[1]
	fh = open(fname, 'r')
	outname = "/Users/adityajitta/Desktop/output2.txt"
	fh1 = open(outname, 'w')
	count = 0
	for l in fh:
		if(count == 0):
			print l.strip()
		if(count > 0):
			argsl = map(float,l.strip().split())
			tstr = getN(argsl[0], argsl[1], argsl[2], count)
			print >>fh1, tstr
		count +=1
	fh.close()
	fh1.close()

main()
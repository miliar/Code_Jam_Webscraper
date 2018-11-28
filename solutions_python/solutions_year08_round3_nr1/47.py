#!/usr/bin/python

import sys
import string
from sets import Set

def minKeyPress(P, K, L, ltrs):

	count = 0
	
	l = []
	for i in xrange(0, len(ltrs)):
		l.append(int(ltrs[i]))
	
	l.sort()
	l.reverse()
	print "ltrs: " + str(l)
	
	# init keys
	k = {}
	for i in xrange(1, K+1):
		k[i] = []
			
	kcount = 1
	for i in l:
		k[kcount].append(i)
		kcount = kcount + 1
		if kcount > K:
			kcount = 1

	#print k
	# now count key presses
	for i in xrange(1, K+1):
		klist = k[i]
		#print "klist: " + str(klist)
		for j in xrange(0, len(klist)):
			#print "klist[j]: " + str(klist[j])
			count = count + (j+1)*int(klist[j])

	return count
	
# usage: problem <input file> <output file>
if len(sys.argv) != 3:
	print "usage: problem <input file> <output file>"
	sys.exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]

# open the input file and read in the contents
infile = open(inputfile, "r")
outfile = open(outputfile, "w")

# read in the number of test cases
N = int(infile.readline())
print "The number of test cases is: " + str(N)
curCase = 1
for i in xrange(1, N+1):

	count = 0
	line = infile.readline()
	items = line.split(' ')

	P = int(items[0])
	K = int(items[1])
	L = int(items[2])

	line = infile.readline().strip()
	ltrs = line.split(' ')

	count = minKeyPress(P, K, L, ltrs)
	print "Count: " + str(count)
	
	outfile.write("Case #%d: %d\r\n" % (curCase, count))
	curCase = curCase + 1


infile.close()
outfile.close()
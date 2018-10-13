#!/usr/bin/python

import sys


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Give one input file!'
		exit()
	
	#read all input lines
	f = open(sys.argv[1], 'r')
	data = f.readlines()
	f.close()
	
	#how many test cases
	TC = int(data[0])
		
	#solve all test cases
	for t in xrange(TC):
		solution1 = int(data[10*t+1])
		matrix1 = [None]*4
		row1 = list(data[10*t+solution1+1].strip('\n').split())
		
		solution2 = int(data[10*t+6])
		matrix2 = [None]*4
		row2 = list(data[10*t+solution2+6].strip('\n').split())
		
		cnt = 0
		solution = None
		for a in row1:
			if a in row2:
				cnt += 1
				solution = a
		
		if cnt == 0:
			print "Case #%u: Volunteer cheated!" % (t+1)
		if cnt == 1:
			print "Case #%u: %s" % (t+1, solution)
		if cnt >= 2:
			print "Case #%u: Bad magician!" % (t+1)


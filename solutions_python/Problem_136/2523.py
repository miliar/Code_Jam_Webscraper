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
		[C, F, X] = map(float, data[t+1].strip('\n').split())
		

		time = 0.0
		last_time = X
		build_time = 0.0
		n = 0
		while True:
			time = X / (n*F + 2.0) + build_time
			build_time += C / (n*F + 2.0)
			n += 1
			if time > last_time:
				break
			last_time = time
				
		print "Case #%u: %.7f" % (t+1, last_time)


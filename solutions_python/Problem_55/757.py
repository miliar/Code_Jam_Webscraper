#!/usr/bin/env python

import numpy
import sys



def doCase(r,k,q, pointer = 0):
	boats = dict()
	
	rides = 0
	profit = 0
	while rides < r:
		boat = ""
		boatsize = 0
		start_profit = profit
		start = pointer
		while boatsize+q[pointer] <= k and not(pointer == start and boatsize > 0):
			boat += str(pointer)+"-"
			
			profit  += q[pointer] 
			boatsize  += q[pointer] 
			pointer += 1
			pointer = pointer % len(q)

		if boat in boats:
			#Calculate profit before start of cycle
			begin = boats[boat][0]
			start_length = boats[boat][1]
			
			
			#Calculate cycle profit
			middle = start_profit - begin
			middleLength = (rides - start_length)

			nrMiddle = ((r-start_length)/middleLength)
			centre = nrMiddle*middle
			
			pointer = start

			
			einde = doCase(r-rides-(middleLength*(nrMiddle-1)) ,k,q, pointer = pointer)
		
			return begin+centre+einde
			
		boats[boat] = [start_profit,rides]
	
		rides += 1

	return profit
	



def run():
	nrCases = int(f.readline())

	for case in xrange(nrCases):
		print "Case #%d:"%(case+1),
		l = f.readline().split()
		r,k,n = int(l[0]), int(l[1]), int(l[2])
		q = [int(j) for j in f.readline().split()]
		print doCase(r,k,q)


f = open(sys.argv[1],'r')

run()


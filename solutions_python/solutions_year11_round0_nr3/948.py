#! /usr/bin/env python

import operator

fin = open('in.txt','r')

numtests = int(fin.readline().rstrip('\n'))
casenum = 0

for casenum in range(numtests):
	numcandies = int(fin.readline().rstrip('\n'))
	candies = fin.readline().rstrip('\n').split(' ')
	int_candies = map(lambda x: int(x), candies)
	xor_total = reduce(lambda x, y: operator.xor(x,y), int_candies)
	
	if (xor_total != 0):
		result = 'NO'
	else:
		result = str(sum(int_candies) - min(int_candies))
		
	casenum += 1	
	print 'Case #' + str(casenum) + ': ' + result
		

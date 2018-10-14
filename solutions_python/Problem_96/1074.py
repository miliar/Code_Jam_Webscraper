#!/usr/bin/python

import sys

numCases = int(sys.stdin.readline())

for case in xrange(1,numCases+1,1):
	sys.stdout.write ("Case #%d: " % case)
	line = sys.stdin.readline()

	data = line.split(' ')
	
	numGooglers = int(data[0])
	surprisesLeft = int(data[1])
	minBestResult = int(data[2])
	
	numBestGooglers = 0
	for i in xrange(3, 3 + numGooglers, 1):
		#print shift[i-3]
		totalResult = int(data[i])
		baseResult = totalResult/3
		shift = totalResult-(baseResult*3)
		
		if shift == 0:
#			possibleTriplets.append ([baseResult, baseResult, baseResult])
#			possibleTriplets.append (baseResult, baseResult+1, baseResult-1]) #Surprising
			normalBestResult = baseResult
			surpriseBestResult = baseResult+1
		elif shift == 1:
#			possibleTriplets.append ([baseResult, baseResult, baseResult+1])
			# No point to this one as it doesn't increase our best result
			#possibleTriplets.append (baseResult-1, baseResult+1, baseResult+1]) #Surprising	
			normalBestResult = baseResult+1
			surpriseBestResult = baseResult+1			
		else:
#			possibleTriplets.append ([baseResult, baseResult+1, baseResult+1])
#			possibleTriplets.append (baseResult, baseResult, baseResult+2]) #Surprising
			normalBestResult = baseResult+1			
			surpriseBestResult = baseResult+2
			
		# Deal with ones above 28
		if surpriseBestResult > 10:
			surpriseBestResult = 10
		
		# Deal with ones below 3
		# For instance 0 will come back with 0 0 0, which will move to 0 0 1
		if normalBestResult > totalResult:
			normalBestResult = baseResult
		if surpriseBestResult > totalResult:
			surpriseBestResult = baseResult
			
	# Set the ones that can reach the minBestResult as surprising first, until we run out of them
		if normalBestResult >= minBestResult:
			numBestGooglers += 1
		elif surpriseBestResult >= minBestResult and surprisesLeft > 0:
			numBestGooglers += 1
			surprisesLeft -= 1
	
	print numBestGooglers
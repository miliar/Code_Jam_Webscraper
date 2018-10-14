f = open('B-small-attempt0.in','r');
fOut = open('result_assignment_2.txt','w')

firstLine = f.readline()

def maxDivisor(numA, numB):
	while numB != 0:
		numRem = numA % numB
		numA = numB
		numB = numRem
	return numA

	
caseNr = 1

#x = 10**50
#print 'x:' + str(int(x))


while True:# in range (0, sum([1 for line in f]) -1 ):
	params = f.readline()
	
	if(params == ''):
		break;
	#print params
	nrOfTimeSpots = params.split(" ")[0]
	
	times = []
	
	for time in params[0:-1].split(" "):
		times.append(int(time))
		
	times.pop(0)
	#print times
	
	
	
	#algorithm starts, get diffs:
	diffs = []
	for t1 in times:
		for t2 in times:
			diff = t1 - t2
			if diff > 0:
				diffs.append(diff)
				
	maxDenom = 0
	
	for d1 in diffs:
		for d2 in diffs:
			denom = maxDivisor(d1, d2)
			if( denom < maxDenom or maxDenom == 0):
				maxDenom = denom
				
	#print 'We got max denominator for diffs: '  + str(maxDenom)
	
	#find a time when the first one matches, and check everyone else. continue doing this until "everyfings ok"
	
	startMark = times[0]
	baseTime = startMark
	
	diffTime = - baseTime % maxDenom  - maxDenom
	
	actualTime = 0
	
	#print 'maxDenom: ' + str(maxDenom)
	#print 'diffTime: ' + str(diffTime)
	
	while True:
		
		diffTime += maxDenom
		#print 'DIFFTIME: '  + str(diffTime)
		#print 'baseTime: ' + str(baseTime)
		ok = True
		for time in times:
			#print time
			#print time + diffTime
			if ((time + diffTime) % maxDenom != 0):
				#print '0 modolus: ' + str(time + diffTime) + ' and ' + str(maxDenom)
				#ok = False
				#break
			#else :
				#print 'non 0 modolus: ' + str(time + diffTime) + ' and ' + str(maxDenom)
				ok = False
		
		if(not ok):
			continue;
		#if we reach here we can safely quit and have the correct time marked
		actualTime = diffTime
		break;

	print 'Case #' + str(caseNr) + ': ' + str(actualTime)
	fOut.write('Case #' + str(caseNr) + ': ' + str(actualTime) + '\n')
	
	caseNr += 1
	
fOut.close()
f.close()
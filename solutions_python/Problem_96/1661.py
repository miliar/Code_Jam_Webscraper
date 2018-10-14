#! /usr/bin/python
import sys
inFile = file(sys.argv[1])

T = None
caseNum = 0
for line in inFile:
	if T == None:
		T = int(line[:-1])
	else:
		caseNum += 1
		toks = line.split()
		N = int(toks[0])
		S = int(toks[1])
		p = int(toks[2])
		ts = toks[3:]
		yesCount = 0
		maybeCount = 0
	
		#print "N=%d, S=%d, p=%d, ts=%s" % (N, S, p, ts)	
		yesThreshold = max(3 * p - 2, p)
		maybeThreshold = max(yesThreshold - 2, p)
		for t in ts:
			if int(t) >= yesThreshold: 
				yesCount += 1
			elif int(t) >= maybeThreshold:
				maybeCount += 1
	
		answer = yesCount + min(maybeCount,S)
		print "Case #%d: %d" %(caseNum, answer)
		
		
	if caseNum >= T:
		break

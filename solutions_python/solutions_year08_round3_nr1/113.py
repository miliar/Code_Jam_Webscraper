import sys

f = open(sys.argv[1])
numProblems = int(f.readline())

for i in xrange(numProblems):
	line = f.readline().split()
	maxPerKey = int(line[0])
	numKeys = int(line[1])
	numLetters = int(line[2])
	letterFreq = []
	
	for l in f.readline().split():
		letterFreq.append(int(l))
	
	if len(letterFreq) > maxPerKey * numKeys:
		print 'Impossible'
		sys.exit()
	
	letterFreq.sort()	
	letterFreq.reverse()	
	
	num = 0
	done = False
	for p in xrange(maxPerKey):
		if done:
			break
		for k in xrange(numKeys):
			num += ((p+1) * letterFreq[0])
			letterFreq = letterFreq[1:]
			if len(letterFreq) == 0:
				done = True
				break
	print ("Case #%d: %d" % (i+1, num))
	
	

    
def runSequence(oppose,combine,seq):
	currentList = []
	for ch in seq:
		processed = False
		currentList.append(ch)
		for s in combine:
			src = set(s[0:2])
			out = s[-1]
			lenS = len(src)
			if 2 > len(currentList) or processed:
				continue
			sub = set(currentList[-2:])
			if sub == src:
				currentList[-2:] = [out]
				#print "comb",src,out
				processed = True
				break
		for x,y in oppose:
			if not processed and ch==x and y in currentList:
				currentList = []
				#print "oppose",x,y
				processed = True
			if not processed and ch==y and x in currentList:
				currentList = []
				#print "oppose",x,y
				processed = True
		if not processed:
			pass
	return currentList
	
def handleLine(line):
	tokens = line.split(' ')
	#print tokens
	pos = 0
	combine = []
	numComb = int(tokens[pos])
	for i in xrange(numComb):
		combine.append(tokens[pos+i+1])
	pos += numComb+1
	numoppose = int(tokens[pos])
	oppose = []
	for i in xrange(numoppose):
		oppose.append(tokens[pos+i+1])
	return str(runSequence(oppose,combine,tokens[-1].strip())).translate(None,'\'')
	
def solveMagicka():
	f = open('gcjdata.txt','r')
	lines = f.readlines()
	for i in range(1,len(lines)):
		print "Case #{0}: {1}".format(i,handleLine(lines[i]))

solveMagicka()
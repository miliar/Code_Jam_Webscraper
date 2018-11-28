import sys

def getMinFreq(engs,seq):
	engset = set(engs)
	minval = 0
	tmpset = set([])
	for s in seq:
		tmpset.add(s)
		if len(engset - tmpset) == 0 :
			minval += 1
			tmpset = set([s])
		
	return minval		

def getInput(f):
	
	engs, seq = [], []
	for i in range(0, int(f.readline())):
		engs.append(f.readline().strip())

	lastquery = ''
	for j in range(0, int(f.readline())):
		query = f.readline().strip()
		if query != lastquery:
			seq.append(query)
			lastquery = query
		
	return engs, seq
	
if __name__ == "__main__":
	infile = open("A-large.in", 'r')
	numCases = int(infile.readline())

	for i in range(0, numCases):
		print "Case #%s: %s" % (i + 1, getMinFreq(*getInput(infile)))
		
	infile.close()
	
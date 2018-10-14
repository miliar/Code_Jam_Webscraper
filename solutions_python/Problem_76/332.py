
file = open("C-large.in")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])

for nCase in range(1, nCases + 1):
	nCandies = int(aStrLines[nCase * 2 - 1])
	
	nXor = 0
	nCandyMin = pow(10, 7)
	nCandySum = 0
	
	for chCandy in aStrLines[nCase * 2].split():
		nCandy = int(chCandy)
		nCandySum += nCandy
		nXor = nXor ^ nCandy
		if nCandy < nCandyMin:
			nCandyMin = nCandy

	strResult = "NO"
	
	if nXor == 0:
		strResult = str(nCandySum - nCandyMin)
		
	print "Case #" + str(nCase) + ": " + strResult
	
	
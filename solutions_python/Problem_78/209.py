
file = open("A-large.in")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])

for nCase in range(1, nCases + 1):
	strLine = aStrLines[nCase]
	aStrToks = strLine.split()
	nGamesTodayMax = int(aStrToks[0])
	rWinToday = int(aStrToks[1])
	rWinLife = int(aStrToks[2])
	
	strResult = ""
	
	if rWinLife == 100 or rWinLife == 0:
		if rWinToday == rWinLife:
			strResult = "Possible"
		else:
			strResult = "Broken"
	else:
		rFactor = 1
		rWinTemp = rWinToday
		
		if (rWinTemp % 2 == 0):
			rWinTemp = rWinTemp / 2
			rFactor = rFactor * 2
		
		if (rWinTemp % 2 == 0):
			rWinTemp = rWinTemp / 2
			rFactor = rFactor * 2
		
		if (rWinTemp % 5 == 0):
			rWinTemp = rWinTemp / 5
			rFactor = rFactor * 5
		
		if (rWinTemp % 5 == 0):
			rWinTemp = rWinTemp / 5
			rFactor = rFactor * 5
			
		nTotDay = 100 / rFactor
		
		if nTotDay <= nGamesTodayMax:
			strResult = "Possible"
		else:
			strResult = "Broken"
	
	print "Case #" + str(nCase) + ": " + strResult
		
	
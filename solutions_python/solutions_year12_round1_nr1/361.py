def getMinimumTypes( typedChr, totalChr, probsCorrect ):
	candidates = []
	for left in range( 0, typedChr + 1 ):
		probRight = 1
		for j in range( left ):
			probRight *= probsCorrect[j]
		firstTry = (typedChr - left) + (totalChr - left) + 1
		keystroke = firstTry*probRight + (firstTry + totalChr + 1)*(1-probRight)
		candidates.append( keystroke )

	candidates.append( totalChr + 2 )
	return float(min(candidates))


import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open( fileNameIn, 'r' )
lines = fileIn.readlines()

testcnt = int( lines[0] )
lineIdx = 1

fileOut = open( fileNameOut, 'w' )

for test in range( testcnt ):
	line = lines[lineIdx].split( ' ' )
	lineIdx += 1

	typedChr = int( line[0] )
	totalChr = int( line[1] )

	line = lines[lineIdx].split( ' ' )
	lineIdx += 1

	probsCorrect = [ float(n) for n in line ]

	res = getMinimumTypes( typedChr, totalChr, probsCorrect )

	fileOut.write("Case #{0}: {1:06f}\n".format(test + 1, res))

normalBests = []
surprisingBests = [0]

for i in range( 31 ):
	q = i // 3
	r = i % 3

	if r == 0:
		best = q
	else:
		best = q + 1
	normalBests.append( best )

for i in range( 1, 29 ):
	q = i // 3
	r = i % 3

	if r == 2:
		best = q + 2
	else:
		best = q + 1
	surprisingBests.append( best )

surprisingBests.append( 10 )
surprisingBests.append( 10 )

#print normalBests
#print surprisingBests


def getMaximumPasser( dancerCnt, surprisingCnt, cutline, totalPoints ):
	successCnt = 0
	surprisingSuccessCnt = 0
	for i in range( dancerCnt ):
		if normalBests[ totalPoints[i] ] >= cutline:
			successCnt += 1
		elif surprisingBests[ totalPoints[i] ] >= cutline:
			surprisingSuccessCnt += 1
	if surprisingSuccessCnt > surprisingCnt:
		surprisingSuccessCnt = surprisingCnt
	return successCnt + surprisingSuccessCnt


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

	dancerCnt = int( line[0] )
	surprisingCnt = int( line[1] )
	cutline = int( line[2] )
	totalPoints = []
	for i in range( 3, len(line) ):
		totalPoints.append( int( line[i] ) )

	res = getMaximumPasser( dancerCnt, surprisingCnt, cutline, totalPoints )

	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))

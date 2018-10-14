def getCycledNumberCount( number, lower, higher, visited ):
	visited.add( number )
	cycledSet = set()
	cycledSet.add( number )
	s = str( number )
	strlen = len( s )
	for i in range( strlen ):
		s = s[-1] + s[0:-1]
		if s[0] != '0':
			n = int( s )
			if (n >= lower) and (n <= higher):
				cycledSet.add( n )
	for i in cycledSet:
		visited.add( i )
	return len( cycledSet )


def getCycledPairCounts( lower, higher ):
	visited = set()
	cycledPairCnt = 0
	for i in range( lower, higher+1 ):
		if i in visited:
			continue
		cycledCnt = getCycledNumberCount( i, lower, higher, visited )
		if cycledCnt >= 2:
			cycledPairCnt += cycledCnt * (cycledCnt-1) / 2
	return int( cycledPairCnt )



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

	lower = int( line[0] )
	higher = int( line[1] )

	res = getCycledPairCounts( lower, higher )

	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))

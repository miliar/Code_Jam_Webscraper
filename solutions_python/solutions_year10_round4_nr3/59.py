import sys

def step( grid, liveList ):
	newGrid = []
	for row in range( len(grid) ):
		newGrid += [ [0] * len(grid[0]) ]
	newLiveList = []
	
	for bacteria in liveList:
		(x,y) = bacteria
		if not(grid[y-1][x] == 0 and grid[y][x-1] == 0):
			newGrid[y][x] = 1
			newLiveList += [bacteria]
		if grid[y][x+1] == 0 and grid[y-1][x+1] == 1:
			newGrid[y][x+1] = 1
			newLiveList += [(x+1,y)]
		
	return( newGrid, newLiveList )

def readListOfChars( inputFile ):
	return inputFile.readline().strip().split(" ")

def readListOfInts( inputFile ):
	return map( int, readListOfChars( inputFile ) )

if( len(sys.argv) > 1 ):
	inputFile = file( sys.argv[1] )
else:
	inputFile = file("C-tiny.in")
	
if( len(sys.argv) > 2 ):
	outputFile = file( sys.argv[2], "w")
else:
	outputFile = None

NumCases = int(inputFile.readline())

for case in range(NumCases):
	
	NumGroups = int( inputFile.readline() )
	
	maxX = 0
	maxY = 0
	
	groups = []
	for group in range(NumGroups):
		(x1,y1,x2,y2) = readListOfInts( inputFile )
		if( x2 > maxX ):
			maxX = x2
		if( y2 > maxY ):
			maxY = y2
		groups += [[x1,y1,x2,y2]]
		
	print maxX, maxY
		
	liveList = []
	grid = []
	for row in range( maxY+2 ):
		grid += [ [0] * (maxX+2) ]
		
	for group in range(NumGroups):
		print groups[group]
		for x in range( groups[group][0], groups[group][2]+1 ):
			for y in range( groups[group][1], groups[group][3]+1 ):
				grid[y][x] = 1
				liveList += [(x,y)]
		
		
	count = 0
	while len(liveList) > 0:
		#print
		#for r in range(len(grid)):
		#	print grid[r]
		(grid, liveList) = step( grid, liveList )
		#print len(liveList)
		count += 1

	output = "Case #%d: %d" % ( case+1, count )
	print output
	
	if outputFile:
		outputFile.write( output + "\n" )
	
	

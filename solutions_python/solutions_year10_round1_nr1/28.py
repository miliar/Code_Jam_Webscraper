import sys

def readListOfChars( inputFile ):
	return inputFile.readline().strip().split(" ")

def readListOfInts( inputFile ):
	return map( int, inputFile.readline().strip().split(" ") )

def printGrid( grid ):
	for x in range( len(grid) ):
		print "".join( grid[x] )

def stripPad( gridLine ):
	newGridLine = gridLine[::-1]
	newGridLine = "".join( newGridLine.split(".") )
	newGridLine = newGridLine + "." * (len(gridLine)-len(newGridLine))
	return newGridLine

def tipGrid( grid, size ):
	return map( stripPad, grid )

def CalcWinners( grid, length ):
	
	red = False
	blue = False
	for x in range( len(grid) ):
		for y in range( len(grid) ):
			if (grid[x][y] == 'R' and not red) or (grid[x][y] =='B' and not blue):
				possible = ""

				if len(grid) - x >= length:
					possible = grid[x][y]
					for p in range( 1, length ):
						if grid[x][y] != grid[x+p][y]:
							possible = ""
				
				if possible == "" and len(grid) - y >= length:
					possible = grid[x][y]
					for p in range( 1, length ):
						if grid[x][y] != grid[x][y+p]:
							possible = ""
				
				if possible == "" and len(grid) - y >= length and len(grid) - x >= length:
					possible = grid[x][y]
					for p in range( 1, length ):
						if grid[x][y] != grid[x+p][y+p]:
							possible = ""

				if possible == "" and len(grid) - y >= length and x >= length:
					possible = grid[x][y]
					for p in range( 1, length ):
						if grid[x][y] != grid[x-p][y+p]:
							possible = ""

				if possible == "R":
					red = True
				if possible == "B":
					blue = True
					
	if not (red or blue):
		return "Neither"
	if red and blue:
		return "Both"
	if red:
		return "Red"
	if blue:
		return "Blue"

if( len(sys.argv) > 1 ):
	input = file( sys.argv[1] )
else:
	input = file("A-tiny.in")

NumCases = int(input.readline())

for case in range(NumCases):
	(GridSize, NumInARow) = readListOfInts( input )
	
	Grid = []
	for row in range(GridSize):
		Grid = Grid + readListOfChars( input )
		
	NewGrid = tipGrid( Grid, GridSize )
	
	winners = CalcWinners( NewGrid, NumInARow )
	
	output = "Case #%d: %s" % ( case+1, winners )
	print output
	

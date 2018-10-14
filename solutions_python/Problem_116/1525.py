#P1
class FileManager:
	handler = False;

	def open(self, file):
		self.handler = open( file, 'r' )

		if self.handler == False:
			return False

		return True

	def getLine( self ):
		if self.handler == False:
			return False

		line = self.handler.readline()

		if not line:
			return False

		return line

	def close( self ):
		if self.handler == False:
			return True;

		close( self.handler )

		return True

def getWinnerFromGrid( cellA, cellB ):
	if( cellA == 3 ):
		realCell = cellB
	else:
		realCell = cellA

	if( cellA == 2 ):
		return "X won"

	return "O won"

FM = FileManager()
#FM.open( "./sample.txt" )
FM.open( "./A-small-attempt0.in" )

numberOfCases = int( FM.getLine() )

for currentCaseIndex in xrange(1, numberOfCases+1, 1):
	grid = { 0: [0, 0, 0, 0], 1: [0, 0, 0, 0], 2: [0, 0, 0, 0], 3: [0, 0, 0, 0] }
	gameFinished = True

	for currentGridIndex in xrange(0, 4):
		gridLine = FM.getLine()
	
		for currentGridOffset in xrange(0, 4):
			if( gridLine[currentGridOffset:currentGridOffset+1] == 'O' ):
				grid[currentGridIndex][currentGridOffset] = 1

			if( gridLine[currentGridOffset:currentGridOffset+1] == 'X' ):
				grid[currentGridIndex][currentGridOffset] = 2
			
			if( gridLine[currentGridOffset:currentGridOffset+1] == '.' ):
				gameFinished = False
				grid[currentGridIndex][currentGridOffset] = 0
			
			if( gridLine[currentGridOffset:currentGridOffset+1] == 'T' ):
				grid[currentGridIndex][currentGridOffset] = 3

	trash = FM.getLine()

	#two diagonals
	if( (grid[0][0] & grid[1][1] & grid[2][2] & grid[3][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][0], grid[1][1] ) )
	elif( (grid[0][3] & grid[1][2] & grid[2][1] & grid[3][0] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][3], grid[1][2] ) )
	#four rows
	elif( (grid[0][0] & grid[0][1] & grid[0][2] & grid[0][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][0], grid[0][1] ) )
	elif( (grid[1][0] & grid[1][1] & grid[1][2] & grid[1][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[1][0], grid[1][1] ) )
	elif( (grid[2][0] & grid[2][1] & grid[2][2] & grid[2][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[2][0], grid[2][1] ) )
	elif( (grid[3][0] & grid[3][1] & grid[3][2] & grid[3][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[3][0], grid[3][1] ) )
	#four cols
	elif( (grid[0][0] & grid[1][0] & grid[2][0] & grid[3][0] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][0], grid[1][0]) )
	elif( (grid[0][1] & grid[1][1] & grid[2][1] & grid[3][1] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][1], grid[1][1]) )
	elif( (grid[0][2] & grid[1][2] & grid[2][2] & grid[3][2] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][2], grid[1][2]) )
	elif( (grid[0][3] & grid[1][3] & grid[2][3] & grid[3][3] ) ):
		print "Case #%u: %s" % ( currentCaseIndex, getWinnerFromGrid( grid[0][3], grid[1][3]) )
	#game not finished
	elif( gameFinished == False ):
		print "Case #%u: Game has not completed" % ( currentCaseIndex )
	#draw
	else:
		print "Case #%u: Draw" % ( currentCaseIndex )
	#print grid
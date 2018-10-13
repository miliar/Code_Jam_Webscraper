#file=look for FM.open()

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

def gridScan( grid, gridH, gridW):
	lineFound = True
	coords = []
	allBigger = False

	for h in xrange( 0, gridH ):
		cell = grid[h][0]
		lineFound = True
		coords = [ [h, 0] ]
		if( cell >= 900 ):
			allBigger = True
		else:
			allBigger = False

		
		for w in xrange( 1, gridW ):
			if( cell >= 900 and (cell-900) <= grid[h][w] ):
				if( cell >= 900 and grid[h][w] >= 900 and cell >= grid[h][w] ):
					pass
				else:
					cell = grid[h][w]

			#print "Cell: %u grid:%u at w: %u h:%u" % (cell, grid[h][w],w,h)

			if cell != grid[h][w]:
				if( grid[h][w] < 900 or grid[h][w]-900 > cell ):
					lineFound = False
					break

			if( grid[h][w] < 900 ):
				allBigger = False

			coords.append( [h, w] );

		if( lineFound == True and allBigger == False):
			#print "ret true"
			return coords

	#print grid

	for w in xrange( 0, gridW ):
		cell = grid[0][w]
		coords = [ [0, w] ]
		lineFound = True
		if( cell >= 900 ):
			allBigger = True
		else:
			allBigger = False

		for h in xrange( 1, gridH ):
			if( cell >= 900 and (cell-900) <= grid[h][w] ):
			#	cell = grid[h][w]
				if( cell >= 900 and grid[h][w] >= 900 and cell >= grid[h][w] ):
					pass
				else:
					cell = grid[h][w]

			#print "V Cell: %u grid:%u at w: %u h:%u" % (cell, grid[h][w],w,h)

			if cell != grid[h][w]:
				if( grid[h][w] < 900 or grid[h][w]-900 > cell ):
					lineFound = False
					break

			if( grid[h][w] < 900 ):
				allBigger = False

			coords.append( [h, w] );

		#print "-- lineFound: %u allBigger: %u" % (lineFound, allBigger) 
		if( lineFound == True and allBigger == False ):
			return coords

	#print "not found"
	return []


FM = FileManager()
#FM.open( "./sample.txt" )
FM.open( "./B-small-attempt4.in");
#FM.open( );

numberOfCases = int( FM.getLine() )

for currentCase in xrange( 1, numberOfCases+1 ):
	( gridH, gridW ) = FM.getLine().split(" ")
	gridW = int( gridW )
	gridH = int( gridH )

	if( gridH == 1 or gridW == 1):
		print "Case #%u: YES" % ( currentCase )
		for s in xrange(0,gridH):
			FM.getLine();
		continue

	grid = {} 
	fillingH = 0
	for fillingH in xrange( 0, gridH ):
		grid[fillingH] = [ 0 for x in xrange( 0, gridW )]

	for currentRow in xrange( 0, gridH ):
		grid[currentRow] = map( lambda x: int(x), filter( lambda x: False if x is " " else True, list(FM.getLine().strip("\n"))))

	remainingCells = gridH * gridW
	failed = False

	#look for the straight line... 
	while remainingCells > 0:
		coords = gridScan( grid, gridH, gridW )
		#replace each one with a new value
		cs = len(coords)
		if( cs == 0 ):
			failed = True
			break

		for z in xrange(0, cs):
			(h,w) = coords[z]
			if( grid[h][w] <= 900 ):
				grid[h][w] = grid[h][w] + 900
				remainingCells -= 1
		#print "remainingCells " + str(remainingCells)
		#print grid

	if( failed == True ):
		print "Case #%u: NO" % ( currentCase )
		#print grid
		continue

	print "Case #%u: YES" % ( currentCase )

	#print grid 

import sys

# open file
try:
	fileIn = open( "A-small-attempt0.in", "r" ) # open file in read mode
	fileOut = open ( "output.txt", "w" )		# open file in write mode
except IOError, message: # file open failed
	print >> sys.stderr, "File could not be opened:", message
	sys.exit( 1 )

records = fileIn.readlines()
record = records[0]
T = int(records[0].split()[0])

for counter in range( 1, T + 1 ):
	# if it isn't the first case, so print a new line
	#if ( counter != 1 ):
	#	fileOut.write( "\n" )

	if ( counter != 1 ):
		fileOut.write( "\n" )
	A1 = int ( records[ counter * 10 - 9 ].split()[ 0 ] )
	A2 = int ( records[ counter * 10 - 4 ].split()[ 0 ] )
	Arrange1 = []
	Arrange2 = []

	# transform 	 input to integer values row by row
	for i in range ( 8, -1, -1 ):
		if ( i > 4 ):
			Items = records[ counter * 10 - i ].split()	
			ItemsInt = []
			integer = 0
			for Item in Items:				
				integer = int(Item)
				ItemsInt += [ integer ]
			Arrange1 += [ ItemsInt ]

		if ( i < 4 ):
			Items = records[ counter * 10 - i ].split()	
			ItemsInt = []
			integer = 0
			for Item in Items:				
				integer = int(Item)
				ItemsInt += [ integer ]
			Arrange2 += [ ItemsInt ]

	print Arrange1 [ A1 - 1 ]
	print Arrange2 [ A2 - 1 ]

	Answer = [ 0, 0, 0, 0 ]
	

	for i in range ( 0, len( Arrange1 ) ):
		for j in range ( 0, len( Arrange2 ) ):
			if ( Arrange1[A1-1][i] == Arrange2[A2-1][j] ):
				Answer[i] += 1
	
	N = 0
	for i in range (0, 4):
		if Answer[i] > 0:
			N += 1

	if N == 0:
		Y = "case #%d: Volunteer cheated!" % counter
	elif N == 1:
		for i in range ( 0, 4 ):
			for j in range ( 0, 4 ):
				if ( Arrange1[A1 - 1][i] == Arrange2[A2 - 1][j] ):
					break
			if ( Arrange1[A1 - 1][i] == Arrange2[A2-1][j] ):
				break
		print i
		Y = "case #%d: %d" % ( counter, Arrange1[ A1 - 1 ][i] )
	else:
		Y = "case #%d: Bad magician!" % counter

	fileOut.write( Y )


fileIn.close()
fileOut.close()
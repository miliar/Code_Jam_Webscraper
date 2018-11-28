import sys

# open file
try:
	fileIn = open( "B-large.in", "r" ) # open file in read mode
	fileOut = open ( "output.txt", "w" )		# open file in write mode
except IOError, message: # file open failed
	print >> sys.stderr, "File could not be opened:", message
	sys.exit( 1 )

records = fileIn.readlines()
record = records
N = int(records[0].split()[0])
for i in range( 1, N + 1):
	if ( i != 1 ):
		fileOut.write( "\n" )
	fields = records[i].split()
	
	# obtain values
	C = float(fields[0])
	F = float(fields[1])	
	X = float(fields[2])
	
	b = 0
	totalTime = X
	aux = X * 2

	if C / 2 + X / (F + 2) <= X / 2: 
		while ( True ):	
			if ( b == 0 ):
				totalTime = 0
				totalTimeNext = 0		
			aux = totalTime
			increment = C / ( ((F * b) + 2) )
			totalTime += increment
			#print "aux: ", aux + ( X / ( (F * b) + 2 ) )
			#print "totaTime: ", totalTime + ( X / ( (F * (b + 1)) + 2 ) )
			if b != 0:
				if aux + ( X / ( (F * b) + 2 ) ) < totalTime + ( X / ( (F * (b + 1)) + 2 ) ):				
					break		
			b += 1
	
		print "aux: ", aux + ( X / ( (F * b) + 2 ) )
		print "totaTime: ", totalTime + ( X / ( (F * (b + 1)) + 2 ) )
		fileOut.write ( "Case #%d: %.7f" % ( i, aux + ( X / ( (F * b) + 2 ) ) ) )
	else:
		print "time: ", (X / ( ( F * b ) + 2 ) )
		fileOut.write( "Case #%d: %.7f" % (i, X / ( ( F * b ) + 2) ) )

fileOut.close()
fileIn.close()
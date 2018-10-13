def timeToWin( x, rate ):
	return ( x / rate )

def timeWithOneUpgrade( c, x, f, rate ):
	newFarm = timeToWin( c, rate )
	NewTime =  timeToWin( x, ( rate+f ) )
	timeTaken = newFarm + NewTime
	return ( timeTaken )

def main():
	input_file = "b2.in"
	infile = open(input_file)

	lines = infile.readlines();
	t = int( lines[0] )
	lines = lines[ 1: ]
	for i in range( t ):
		print "Case #" + str(i+1) + ": ",
		[c,f,x] = [ float(x) for x in lines[ i ].rstrip().split(" ") ]
		rate = 2
		elapsedTime = 0
		oldTime = 0
		while True:
			oldTime = timeToWin(x, rate)
			newTime = timeWithOneUpgrade(c,x,f,rate)
			if newTime < oldTime:
				elapsedTime += timeToWin(c,rate)
				rate += f
			else:
				break
		print ( elapsedTime + oldTime )

main()

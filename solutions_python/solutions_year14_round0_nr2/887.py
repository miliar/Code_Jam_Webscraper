import decimal

decimal.getcontext().prec = 20

fin = open("input.txt", "r" )
fout = open("output.txt", "w" )

testcases = int( fin.readline().split()[0] )

for test_id in range( testcases ):

	line = fin.readline().split()

	c = decimal.Decimal( line[0] )
	f = decimal.Decimal( line[1] )
	x = decimal.Decimal( line[2] )
	answer = x / decimal.Decimal( 2 )
	tmp = decimal.Decimal( 0 )

	cur = decimal.Decimal( 2 )

	for iterations in range( 1000000 ):
		answer = min( answer, tmp + x / cur )
		tmp = tmp + c / cur
		cur = cur + f

	fout.write( "Case #%d: %s\n" % ( test_id + 1, str( answer ) ) )





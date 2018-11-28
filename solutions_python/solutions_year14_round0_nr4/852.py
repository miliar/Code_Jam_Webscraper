import itertools

def KenMove( value, ken ):
	for i in range( len( ken ) ):
		if ken[i] > value:
			return i
	return 0

def DeceitfulWar( naomi, ken ):
	result = 0
	for i in range( len( naomi ) ):
		pos = KenMove( 1000000, ken )
		if naomi[i] > ken[pos]:
			result = result + 1
			del ken[ pos ]
	return result	

def War( naomi, ken ):
	result = 0
	naomi.reverse()
	for i in range( len( naomi ) ):
		pos = KenMove( naomi[i], ken )
		if naomi[i] > ken[pos]:
			result = result + 1
		del ken[ pos ]
	return result

fin = open("input.txt", "r" )
fout = open("output.txt", "w" )

testcases = int( fin.readline().split()[0] )

for test_id in range( testcases ):

	n = int( fin.readline().split()[0] )

	naomi = [ x for x in fin.readline().split() ]

	ken = [ x for x in fin.readline().split() ]

	for i in range( len( naomi ) ):
		naomi[i] = "".join( naomi[i][ 2:7 ] )
		while len( naomi[i] ) < 5:
			naomi[i] = naomi[i] + '0'
		naomi[i] = int( naomi[i] )

	for i in range( len( ken ) ):
		ken[i] = "".join( ken[i][ 2:7 ] )
		while len( ken[i] ) < 5:
			ken[i] = ken[i] + '0'
		ken[i] = int( ken[i] )

	naomi.sort()
	ken.sort()

	fout.write( "Case #%d: %d %d\n" % ( test_id + 1, DeceitfulWar( naomi[:], ken[:] ), War( naomi[:], ken[:] ) ) )

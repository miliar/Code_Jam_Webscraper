#! c:\python33\python.exe

import sys

def isPalandrome( num ):
	forwards = str( num )
	backwards = forwards[::-1]
	return( backwards == forwards )

def findFSNums( a, b ):

	num = 1
	num_squared = 1
	fs_count = 0
	
	while( num_squared < a ):
		num += 1
		num_squared = num**2
		
	
	while num_squared <= b :
		if isPalandrome( num ) and isPalandrome( num_squared ):
			fs_count += 1
			
		num += 1
		num_squared = num**2
			
	return fs_count
	
########################################################

input = open( sys.argv[1], "r" )
output = open( sys.argv[2], "w" )

tc_count = int( input.readline().rstrip() )

for tc in range( 1, tc_count + 1 ):
	
	(a,b) = input.readline().rstrip().split()
	a = int( a )
	b = int( b )
	
	fs_nums = findFSNums( a, b )
	output.write( "Case #{}: {}\n".format( tc, fs_nums ) )
	
input.close()
output.close()
#! c:\python33\python.exe

import sys
	
def isPossible( grid, rows, cols ):
	#every square has to be the 
	
	if rows == 1 or cols == 1:
		return True
		
	col_maxs = {}
	row_maxs = {}
	
	for i in range( rows ):
		for j in range( cols ):
			test_max = grid[i][j]
			if ( not j in col_maxs ) or col_maxs[j] < test_max:
				col_maxs[j] = test_max
			if ( not i in row_maxs ) or row_maxs[i] < test_max:
				row_maxs[i] = test_max
				
	for i in range( rows ):
		for j in range(cols):
			if (grid[i][j] != row_maxs[i] and
				grid[i][j] != col_maxs[j]):
				
				return False
			
	return True
	

###############################################################

input = open( sys.argv[1], "r" )
output = open( sys.argv[2], "w" )

tc_count = int( input.readline().rstrip() )

for tc in range( 1, tc_count + 1 ):

	print( "*** case {} ***".format( tc ) )

	(rows,cols) = input.readline().rstrip().split()
	rows = int( rows )
	cols = int( cols )
	
	print( "rows: {} cols: {}".format( rows, cols ) )
	
	grid = []
	
	for i in range(rows):
		row = list(input.readline().rstrip().split())
		for j in range(len(row)):
			row[j] = int( row[j] )
			
		grid.append( row )
		
	can_cut = False
	if isPossible( grid, rows, cols ):
		can_cut = "YES"
	else:
		can_cut = "NO"
	
	output.write( "Case #{}: {}\n".format( tc, can_cut ) )
	
input.close()
output.close()
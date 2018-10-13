import sys

def solveCase( infile ):
	answer = ""
	
	string_count = int( infile.readline().strip() )
	strings = []
	
	for i in range(string_count):
		strings.append( infile.readline().strip() )
			
	#check if all the same string
	if len( set(strings) ) == 1:
		return 0
		
	letter_counts = []
	for s in strings:
		lc = []
		while( s != "" ):
			char = s[0]
			count = 1
			s = s[1:]
			while s != "" and s[0] == char:
				count += 1
				s = s[1:]
				
			lc.append( (char,count) )
			
		letter_counts.append( lc )
		
	#make sure same length
	if len( set( [len(x) for x in letter_counts] ) ) != 1:
		return "Fegla Won"
		
	changes = []
	for i in range( len(letter_counts) ):
		change = 0
		#assume we are choosing this string to change the others to.  How many total changes?
		lc = letter_counts[i]
		for j in range( len(lc) ):
			(char,count) = lc[j]
			print( "char {} count {}\n".format( char, count ) )
			
			for k in range( len(letter_counts) ):
				(other_char, other_count) = letter_counts[k][j]
				print( "other_char {} other_count {}\n".format( other_char, other_count ) )
				
				if char != other_char:
					return "Fegla Won"
					
				change += abs( count - other_count )
				
		changes.append( change )
		print( "change {}\n".format( change ) )
		
	return min( changes )
		
	
		
	

def solve(infile):
	output = ""
	t_count = int( infile.readline() )
	
	for i in range( t_count ):
		print( "*** Test {} ***\n".format( i + 1 ) )
		answer = solveCase( infile )
		output += "Case #{}: {}\n".format( i+1, answer )
		
	return output.strip()

if( __name__ == "__main__" ):
	infile_name = sys.argv[1]
	
	output = "__null__"
	with open( infile_name ) as f:
		output = solve( f )
		
	with open( infile_name + ".out", "w" ) as of:
		of.write( output )
	
	exit(0)
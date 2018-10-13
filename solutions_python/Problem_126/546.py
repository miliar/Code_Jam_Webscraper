#! c:\python33\python.exe

import sys
import re

CV_MAP = {}

def genMap():
	global CV_MAP
	vowels = re.compile( r"[aeiou]" )
	cord = ord('c')
	vord = ord('v')
	
	for c in range( ord('a'), ord('z') + 1 ):
		char_ord = chr(c)
		if vowels.match( char_ord ):
			CV_MAP[c] = vord
		else:
			CV_MAP[c] = cord
	
def solve( input ):
	global CV_MAP
	
	name, n = input.readline().rstrip().split()
	
	name = name.translate( CV_MAP )
	n = int(n)
	nstring = "c" * n
	nstring_ct = 0
	
	#print( "name {} nstring {}".format( name, nstring ) )
	
	count = 0
	
	for i in range( len( name ) ):
		for j in range( i + 1, len(name) + 1 ):
			if nstring in name[i:j]:
				count += 1
				#print( "match: {}".format( name[i:j] ) )
		
	return count

if __name__ == '__main__':
	input = open( sys.argv[1], "r" )
	output = open( sys.argv[2], "w" )
	
	tc_count = int( input.readline().rstrip() )
	genMap()
	
	for tc in range( 1, tc_count + 1):
		print( "Solving case: {}".format( tc ) )
		
		output.write( "Case #{}: {}\n".format( tc, solve( input ) ) )
	
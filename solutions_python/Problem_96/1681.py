from sys import *

case = 1
for line in [x for x in stdin][1:]:

	parts = line.split()
	
	surprising = int(parts[1])
	p = int(parts[2])
	easy = 0
	potential_surprising = 0
	
	for score in [ int(x) for x in parts[3:]]:
		if score >= p + 2 * max(0, (p -1) ):
			easy += 1
		elif score >= p + 2 * max(0, (p-2) ):
			potential_surprising += 1
	
	count = easy + min( surprising, potential_surprising )
	print( "Case #{0}: {1}".format( case, count ) )
	case = case + 1
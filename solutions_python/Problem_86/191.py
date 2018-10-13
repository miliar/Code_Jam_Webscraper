#! /usr/bin/python
import sys

T = int( sys.stdin.readline() )


for i in range( T ) :


	line = sys.stdin.readline().split()
	line = [ int(n) for n in line ]
	N = line[0]
	L = line[1]
	H = line[2]

	notes = sys.stdin.readline().split()
	notes = [ int(n) for n in notes ]

	#print "notes is :",notes
	#print "L is :",L
	#print "H is :",H

	result = -1 
	found = True
	for n in range( L,H+1 ) :

		first = True
		counter = 0 
		if found == False :
			break
		#print "notes ops is :",notes
		#print "\n\n\n\ngoing for n :",n
		for x in notes :
			#print "x in notes is :",x
			#print "n in notes is :",n
			counter += 1

			if ( first == True ) and ( ( x % n ) == 0 or ( n % x) == 0 ) :
				#print "first c ",x
				result = n
				first = False
			elif ( counter == len( notes ) ) and  ( ( x % n ) == 0 or ( n % x) == 0 ):
				found = False
			elif ( ( x % n ) == 0 or ( n % x) == 0 ) :
				#print "second c :",x
				pass
			else :
				#print "third case :",x
				break
	if found == True :
		print "Case #%d: %s"%((i+1),"NO"  )
		continue
	print "Case #%d: %d"%((i+1),result  )

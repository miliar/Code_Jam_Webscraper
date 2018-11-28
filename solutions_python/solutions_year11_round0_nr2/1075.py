#! /usr/bin/python
import sys


N = int( sys.stdin.readline() )


for i in range( N ) :

	line = sys.stdin.readline().split()
	#print "line is :", line

	C = int( line[0] )


	combine = {}
	cancel = {}

	for j in range( 1,C+1 ) :
		com = line[j]
		a = line[j][0]
		b = line[j][1]
		c = line[j][2]

		combine[(a,b)] = c		
		combine[(b,a)] = c

	#print "combine is :", combine
	D = int(line[C+1])
	#print "D is :",D
	for j in range( C+2,C+2+D ) :
		canc = line[j]
		#print "canc is :", canc
		a = canc[0]
		b = canc[1]

		cancel[a] = b
		cancel[b] = a
		
	#print "cancel is :",cancel
	result = []

	test_string = line[-1]

	#print "test string is :",test_string

	result.append( test_string[0] )
	test_string = test_string[ 1: ]
	#print "final test_string :",test_string
	for c in test_string :
		#print "c is :",c	
		#print "result is :",result
		try :
			#print "combine in try is :",combine
			val = combine[ (result[-1],c) ]
			#print "value found in try and result is :",result
			#print "Before popping result is :",result
			result.pop( -1 )
			#print "After popping result is :",result
			result.append( val )

		except :
			#print "in except"
			if ( c in cancel ) and ( cancel[c] in result ) :
				#print "doing zero"
				result = []
			else :
				#print "simply appending"
				result.append( c )
		

	as_str = "["
	if result :
		as_str += result[0]
		result.pop( 0 )
		for s in result :
			as_str += ', '
			as_str += s

	as_str += ']'
		#print "Case #%d:%s"%((i+1),result)
	print "Case #%d: %s"%( (i+1),as_str)

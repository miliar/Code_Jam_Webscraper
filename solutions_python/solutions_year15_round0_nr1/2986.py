#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	exit()

f = open( sys.argv[1], 'r' )

cases = int( f.readline() )

case = 1
for line in f:
	Smax, audience = line.rstrip("\r\n").split(" ")
	Smax = int(Smax)
	audience = map( int, list(audience))
	
	friends = 0
	standing = 0
	i = 0
	for a in audience:
		needed = 0
		if standing < i:
			needed = i - standing
			friends += needed
 		
		standing += a + needed 
		i += 1

	print "Case #" + str(case) + ": " + str(friends)
	case += 1

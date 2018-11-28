import sys
import numpy as np

def validate( N, R, O, Y, G, B, V, sol ):
	assert( len(sol) == N )
	assert( sol.count("R") == R )
	assert( sol.count("O") == O )
	assert( sol.count("Y") == Y )
	assert( sol.count("G") == G )
	assert( sol.count("B") == B )
	assert( sol.count("V") == V )

	compatibles = [ "BR", "RB", "RY", "YR", "BY", "YB",   "BO", "OB",  "GR", "RG",  "YV", "VY" ]
	for i in xrange(N-1):
		if sol[i:i+2] not in compatibles:
			print sol[i:i+2]
			print R, O, Y, G, B, V, sol 
			asdf

	if sol[-1]+sol[0] not in compatibles:
		print R, O, Y, G, B, V, sol 
		asdf

def solve( N, R, O, Y, G, B, V ):
	# B-O-B, R-G-R,	Y-V-Y
	if B < O or R < G or Y < V:
		return "IMPOSSIBLE"

	#if max(B-O, R-G, Y-V) - min(B-O, R-G, Y-V) > 1:
	#	return "IMPOSSIBLE"

	B_part = R_part = Y_part = ""

	if O >= 1:
		B_part = "OB" * O
		B -= O

	if G >= 1:
		R_part = "GR" * G
		R -= G

	if V >= 1:
		Y_part = "VY" * V
		Y -= V


	odd = False
	if (R+B+Y)%2 == 1:
		odd = True
		R -= 1
		B -= 1
		Y -= 1

	rb = (R+B-Y)/2
	by = (-R+B+Y)/2
	yr = (R-B+Y)/2

	if min(rb,by,yr) < 0:
		return "IMPOSSIBLE"

	ret = ""

	if rb + by + yr == 0:
		ret += B_part + R_part + Y_part

	elif rb > 0:
		ret += "R"+R_part +  ("RB" * rb)[1:] + B_part   + "YB" * by +  "RY" * yr + Y_part
	elif by > 0:
		ret += "B"+B_part +  ("BY" * by)[1:] + Y_part   + "RY" * yr +  "BR" * rb + R_part
	elif yr > 0:
		ret += "Y"+Y_part +  ("YR" * yr)[1:] + R_part   + "BR" * rb +  "YB" * by + B_part


	if odd == True:
		if len(ret) > 0:
			for cycle in [ "BRY", "BYR", "RBY", "RYB", "YRB", "YBR"]:
				if ret[-1] != cycle[0] and ret[0] != cycle[-1]:
					ret += cycle
					break
		else:
			ret += "BRY"

	return ret

if __name__ == "__main__":
	fd_input = open( sys.argv[1] )
	fd_output = open( sys.argv[1].replace(".in", ".out"), "w" )

	T = int( fd_input.readline().strip() )
	for t in range(T):
		line = fd_input.readline().strip().split(" ")
		N, R,O,Y,G,B,V = [ int(x) for x in line ]
		sol = solve( N,R,O,Y,G,B,V )
		if sol != "IMPOSSIBLE":
			validate( N,R,O,Y,G,B,V,  sol )
		fd_output.write( "Case #%d: %s\n" % (t+1, sol) )

	fd_input.close()
	fd_output.close()


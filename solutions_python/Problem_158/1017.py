#! /usr/bin/env python3.4
import operator

def FindWinner(X, R, C):
	if X == 1:
		return "GABRIEL"

	# Square with a hole in it
	if X >= 7: return "RICHARD"
		
	# Empty squares left over when not divisible  
	if (R*C) % X != 0: return "RICHARD"
	
	# Board is too narrow
	if X >= 3 and (R == 1 or C == 1): return "RICHARD"
	if X > R and X > C: return "RICHARD"
	# Can fill up an entire dimension with bits sticking out of both sides
	if min(R,C)*2 <= X and X >=4: return "RICHARD"

	# More squares in Omino than entire board
	if X > (R*C): return "RICHARD"
	
	# Config T4 with width 2 means an edge square is inacessible
	if X == 4 and (R == 2 or C == 2): return "RICHARD"
	
	# Gabriel wins if 2 squares in an even board
	if (X == 2) and ((R*C) % 2 == 0): return "GABRIEL"
		
	return "GABRIEL"
	
# Start
file = open("D-small-attempt2.in")
T = int(file.readline())
outputFile = open("DTest.txt", 'w')
for i in range(T):
	X,R,C = map(int,file.readline().split())
	result = FindWinner(X, R, C)
	print("Case #{0}: {1}".format(i+1, result))
	''' # Debug
	if X > 1 and not ((R*C) % X != 0 and result == "RICHARD"):
		outputFile.write("Case #{0}: {1} {2} {3} {4}\n".format(i+1, result, X, R, C))
	'''
	outputFile.write("Case #{0}: {1}\n".format(i+1, result))

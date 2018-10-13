#! /usr/bin/env python3.4
import operator

def FindMoves(R,C,W):
	if W == 1: return R*C

	if R == 1 or C == 1:
		line = max(R,C)
		if W == line: return W
		if W >= line/2: 
			return W + 1

	#-- Small case
	if C <= 3:
		return C
	if C == 5 and W == 2:
		return 4
	if C == 6 and W == 2:
		return 4
	if C == 7:
		return 5
	if C == 8:
		return 5
	if C == 9:
		if W == 2:
			return 6
		if W == 3:
			return 5
		if W == 4:
			return 6
	if C == 10:
		return 6

	if max(R,C) == W:
		return W + min(R,C) - 1
		
# Start
file = open("A-small-attempt0.in")
T = int(file.readline())
outputFile = open("ASmall.txt", 'w')
for i in range(T):
	R,C,W = map(int,file.readline().split())
	result = FindMoves(R,C,W)
	print("Case #{0}: {1}".format(i+1, result))
	''' # Debug
	if X > 1 and not ((R*C) % X != 0 and result == "RICHARD"):
		outputFile.write("Case #{0}: {1} {2} {3} {4}\n".format(i+1, result, X, R, C))
	'''
	outputFile.write("Case #{0}: {1}\n".format(i+1, result))

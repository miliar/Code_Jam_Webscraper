#!/usr/bin/python

import sys

def solve(cases):
	sols = []
	
	for case in cases:
		oTotal = 0
		bTotal = 0
		bPos = 1
		oPos = 1
		bCurr = 0
		oCurr = 0

		
		last = case[0][0]
		for move in case:
			if move[0] == last:					# The current color has more moves
				if last == 66:					# Blue moves..
					bCurr += abs(move[1] - bPos) + 1
					bTotal += abs(move[1] - bPos) + 1
					bPos = move[1]
				else:						# Orange moves..
					oCurr += abs(move[1] - oPos) + 1
					oTotal += abs(move[1] - oPos) + 1
					oPos = move[1]
			else:							# Color swapping
				if last == 66:					# Blue->Orange swap
					oCurr = max(0,abs(move[1] - oPos) - bCurr) + 1 
					oTotal += max(abs(move[1] - oPos),bCurr) + 1
					oPos = move[1]
				else:						# Orange->Blue swap
					bCurr = max(0,abs(move[1] - bPos) - oCurr) + 1
					bTotal += max(abs(move[1] - bPos),oCurr) + 1
					bPos = move[1]
				last = move[0]


		sols.append(max(oTotal,bTotal))
	
	return sols

# Reading up the data 
f = open(sys.argv[1],'r')
caseCount = int(f.readline().strip('\n'))
#print caseCount
tmpcases = []
for i in range(caseCount):
	tmpcases.append(f.readline().strip('\n').split(' ')[1:])

cases = []
for tmpcase in tmpcases:
	cases.append([])
	for j in range(len(tmpcase) / 2):
		cases[-1].append((ord(tmpcase[2 * j]),int(tmpcase[2 * j + 1])))

#print cases
solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": " + str(solution[i])

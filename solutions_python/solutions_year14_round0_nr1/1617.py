#!/usr/bin/env python3
import sys
argc = len(sys.argv)
filename = sys.argv[1]
if argc > 2:
	casenumbers = list(map(int, sys.argv[2:]))
file = open(filename)
T = int(file.readline().rstrip())
for case in range(1,T+1):
	row1 = int(file.readline().rstrip())
	grid1 = []
	for i in range(4):
		row = list(map(int, file.readline().rstrip().split()))
		grid1.append(row)
	row2 = int(file.readline().rstrip())
	grid2 = []
	for i in range(4):
                row = list(map(int, file.readline().rstrip().split()))
                grid2.append(row)
	if argc > 2 and not(case in casenumbers):
		continue
	possiblenumbers = {}
	for number in grid1[row1-1]:
		if number in possiblenumbers:
			possiblenumbers[number] += 1
		else:
			possiblenumbers[number] = 1
	for number in grid2[row2-1]:
		if number in possiblenumbers:
			possiblenumbers[number] += 1
		else:
			possiblenumbers[number] = 1
	solution = []
	for number in possiblenumbers:
		if possiblenumbers[number] == 2:
			solution.append(number)
	print ("Case #", case, ": ", sep="", end="")
	if len(solution) == 1:
		print(solution[0])
	elif len(solution) > 1:
		print("Bad magician!")
	elif len(solution) == 0:
		print("Volunteer cheated!")

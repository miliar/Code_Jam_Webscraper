#!/usr/bin/env python3

import os

file = open("input", "r")

cases = file.readline()

for line_nr in range(1,int(cases)+1):
	line = file.readline()
	X = int(line.split(" ")[0])
	R = int(line.split(" ")[1])
	C = int(line.split(" ")[2])

	# check 1 : see if the number of cells on the grid can be filled with chosen onimo
	if R*C % X != 0:
		print("Case #" + str(line_nr) + ": RICHARD")
		continue

	# check 2 : all lengths / widths can fill in the grid ?
	check2=False
	for i in range(X):
		if (X-i > C or i+1 > R) and (i+1 > C or X-i > R):
			check2=True
			break
	if check2:
		print("Case #" + str(line_nr) + ": RICHARD")
		continue

	# check 3 (HORRIBLE): if X=4, and a piece takes 50% of space, check.
	if X==4 and R*C/2<=X:
		print("Case #" + str(line_nr) + ": RICHARD")
		continue

	print("Case #" + str(line_nr) + ": GABRIEL")

file.close()

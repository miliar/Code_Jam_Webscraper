# Qualification Round : Problem B

import sys
import os
import math

# array of entries : columns, rows, size, grid
def ReadInput(filename):
	f = open(filename,'r')
	count = int(f.readline())
	entries = []

	failure = False

	for i in range(count):
		temp = f.readline()
		entry = []
		grid = []
		if len(temp) == 0:
			failure = True
			break
		dim = temp.strip().split()
		entry.append(int(dim[1]))
		entry.append(int(dim[0]))
		entry.append(entry[0]*entry[1])

		for j in range(entry[1]):
			temp = f.readline()
			if len(temp) == 0:
				failure = True
				break
			row = temp.strip().split()			
			for i in range(entry[0]):
				grid.append(int(row[i]))

		if failure:
			break

		entry.append(grid)
		entries.append(entry)

	f.close()

	return entries

def DetermineFeasiblity(e):
	rMax = [0] * e[1]
	cMax = [0] * e[0]
	bGrid = [False] * e[2]

    # find maximum values
	for j in range(e[1]):
		for i in range(e[0]):
			temp = e[3][j*e[0]+i]

			if rMax[j] < temp:
				rMax[j] = temp
			if cMax[i] < temp:
				cMax[i] = temp

    # if cell is the same as the maximum value in some row or col
    # then it can be cut by sending the mover across that line
	for j in range(e[1]):
		for i in range(e[0]):
			idx = j*e[0]+i
			temp = e[3][idx]
			if temp == rMax[j] or temp == cMax[i]:
				bGrid[idx] = True

    # if all cells can be cut
    # the pattern is feasible
	bSum = True
	for i in range(e[2]):
   	    bSum = bSum and bGrid[i] 

	return "YES" if bSum else "NO"

# beginning of main script
if len(sys.argv) < 3:
	sys.exit('    usage: <input> <output>')

filename = sys.argv[1]
outputFile = sys.argv[2]
f = open(outputFile,'w')

entries = ReadInput(filename)

for i in range(len(entries)):
	f.write("Case #%d: %s\n" % (i+1, DetermineFeasiblity(entries[i])))

f.close()

#!/usr/bin/env python

def solve(line):
	items = (line.strip()).split()
	buttonCount = int(items.pop(0))

	ORANGE = 'O'

	orangeLoc = 1
	orangeArrive = 0
	blueLoc = 1
	blueArrive = 0

	for button in xrange(buttonCount):
			color = items[2 *button]
			number = int(items[1 + 2 * button])

			if color == ORANGE:
				orangeTime = orangeArrive + abs(number-orangeLoc) + 1
				orangeArrive = max(blueArrive + 1, orangeTime)
				orangeLoc = number
			else:
				blueTime = blueArrive + abs(number-blueLoc) + 1
				blueArrive = max(orangeArrive + 1, blueTime)
				blueLoc = number
			
			print "\t\t", color, number
			print orangeLoc, orangeArrive
			print blueLoc, blueArrive
			print
	
	print "result:", orangeArrive, blueArrive
	return max(orangeArrive, blueArrive)

def solveFile(Filename):
	inFile = file(Filename, "r")
	outFile = file(Filename[:-2]+"out", "w")
	L = int(inFile.readline())
	for i, line in enumerate(inFile.readlines(),1):
		outFile.write("Case #{0}: {1}\n".format(i, solve(line)))

solveFile("example.in")
solveFile("A-large.in")


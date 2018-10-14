import re

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1]
	
def getMult():
	return getLine().strip().split()

def getMultInt():
	return map(int, getMult())
	
def getMultFloat():
	return map(float, getMult())

while curTest < int(numTests):	
	X, R, C = getMultInt()
	
	if (R*C) % X != 0:
		winner = "RICHARD"
	elif X == 1:
		winner = "GABRIEL"
	elif X == 2 and (R >= 2 or C >= 2):
		winner = "GABRIEL"
	elif X >= 7:
		winner = "RICHARD"
	elif (R*C) < X:
		winner = "RICHARD"
	elif R < X and C < X:
		winner = "RICHARD"
	elif X > 2 and (C == 1 or R == 1):
		winner = "RICHARD"
	elif X == 4 and (R <= 2 or C <= 2):
		winner = "RICHARD"
	elif X == 4 and R == 3 and C == 3:
		winner = "RICHARD"
	else:
		winner = "GABRIEL"
	
	fw.write("Case #%d: %s\n" % (curTest+1, winner))
	curTest += 1
					
fr.close()
fw.close()
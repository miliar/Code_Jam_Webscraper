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

while curTest < int(numTests):	
	a, b = getLine().strip().split()
	
	numShyness = int(a)
	curStanding = 0
	curShyness = 0
	numFriends = 0
	
	for people in b:
		if int(people) > 0 and curShyness > curStanding:
			numFriends += (curShyness - curStanding)
			curStanding += numFriends
			
		curStanding += int(people)
		curShyness += 1
	
	fw.write("Case #%d: %s\n" % (curTest+1, numFriends))
	curTest += 1
					
fr.close()
fw.close()
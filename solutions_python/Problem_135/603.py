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
	firstNum = int(getLine())
	
	for i in range(4):
		a, b, c, d = getLine().strip().split()
		if (i+1) == firstNum:
			vals = [a,b,c,d]
			
	secondNum = int(getLine())
	
	for i in range(4):
		a, b, c, d = getLine().strip().split()
		if (i+1) == secondNum:
			vals2 = [a,b,c,d]
			
	combined = set(vals) & set(vals2)
	if len(combined) < 1:
		s = "Volunteer cheated!"
	elif len(combined) > 1:
		s = "Bad magician!"
	else:
		s = combined.pop()
	
	fw.write("Case #%d: %s\n" % (curTest+1, s))
	curTest += 1
					
fr.close()
fw.close()
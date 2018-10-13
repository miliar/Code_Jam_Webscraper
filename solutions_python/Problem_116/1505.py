import os
import re
import sys
import time

print (time.strftime('%d/%m/%y %H:%M;%S',time.localtime()))

inputFile = "E:/Workspaces/codeJam/A-large.in" 
outputFile = "E:/Workspaces/codeJam/output.txt"
file = open(inputFile, "r")
fileout = open(outputFile, "w")


#READ COUNT
countCase = int(file.readline())
print("\nCase count: %d" % countCase)


# READ
cases = []
lineCount = 0
caseTemp = []

for line in file.readlines():
	#print ("\nRead {0} {1} {2}".format(line, lineCount+1, lineCount % 5))
	lineCount = lineCount+1
	if lineCount % 5 == 0:
		cases.append(caseTemp)
		caseTemp = []
		continue
	
	#Beware \n added too
	caseTemp.append(list(line))
	
#cases.append(caseTemp)
file.close()

#RESOLVE
def resolveLine(case, x, y, dX, dY):
	player = ' '
	draw = False
	
	for i in range(0, 4):
		val = case[x][y]
		#print(("\nSolve {0} {1} {2}").format(x, y, val))
		
		if(val == '.'):
			return "Game has not completed";
		if(player == ' ' and val != 'T'):
			player = val
		if(val != 'T' and val != player):
			draw = True
		
		x += dX
		y += dY
	
	if draw:
		return "Draw"
	return "%s won" % player
	

	
def getResult(case):
	notCompleted = False

	for i in range(0, 4):
		str = resolveLine(case, i, 0, 0, 1)
		if(str == "Game has not completed"):
			notCompleted = True
		if(str == "O won" or str == "X won"):
			return str
			
	for i in range(0, 4):
		str = resolveLine(case, 0, i, 1, 0)
		if(str == "Game has not completed"):
			notCompleted = True
		if(str == "O won" or str == "X won"):
			return str
		
	str = resolveLine(case, 0, 0, 1, 1)
	if(str == "Game has not completed"):
		notCompleted = True
	if(str == "O won" or str == "X won"):
		return str
			
	str = resolveLine(case, 3, 0, -1, 1)
	if(str == "Game has not completed"):
		notCompleted = True
	if(str == "O won" or str == "X won"):
		return str
			
			
	if(notCompleted):
		return "Game has not completed"
	return "Draw"
	

#START RESOLVE
for i in range(0, len(cases)):
	case = cases[i]
	print(("\nCase {0} {1}").format(len(case), len(case[0])))
	str = getResult(case)
	
	print(("\nCase result: {0}").format(str))
	fileout.write(("Case #{0}: {1}\n").format((i+1),str))
	
fileout.close()
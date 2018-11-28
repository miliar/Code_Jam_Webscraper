import sys
import math

def solveCase(words):
	N = int(words[0])
	D = int(words[1])
	G = int(words[2])
	Pd = float(words[1]) / 100
	Pg = float(words[2]) / 100
	
	if (D == 0 and G == 0):
		return "Possible"
	if (D == 100 and G == 100):
		return "Possible"
	if D > 0 and G == 0:
		return "Broken"
	if D < 100 and G == 100:
		return "Broken"
	
	for i in range(1, N + 1):
		games = Pd * i
		if games == math.floor(games):
			if float(100/G) == math.floor(float(100/G)) or float(games/G) == math.floor(float(games/G)):
				return "Possible"
				
	return "Broken"
	
		
if (len(sys.argv) > 1):
	out = ((len(sys.argv) > 2) and sys.argv[2]) or "test.out"
	
	fileIn = open(sys.argv[1], "r")
	fileOut = open(out, "w")
	
	fileIn.readline()
	line1 = fileIn.readline().strip()
	caseNum = 0
	while line1 != "":
		caseNum += 1
		
		answer = solveCase(line1.split(" "))
		
		outstr = "Case #" + str(caseNum) + ": " + answer
		fileOut.write(outstr + "\n")
		
		line1 = fileIn.readline()
	
	fileIn.close()
	fileOut.close()
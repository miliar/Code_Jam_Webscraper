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

	CPS = 2.0
	C, F, X = map(float, getLine().strip().split())
	
	totalTime = 0.0
	
	while True:
		timeToFarm = C / CPS
		timeToEnd = X / CPS
		timeToEndWithFarmPurchase = (X / (CPS + F)) + timeToFarm
		
		if timeToEnd < timeToFarm or timeToEndWithFarmPurchase > timeToEnd:
			totalTime += timeToEnd
			break
			
		CPS += F
		totalTime += timeToFarm
		
	fw.write("Case #%d: %.7f\n" % (curTest+1, totalTime))
	curTest += 1
					
fr.close()
fw.close()
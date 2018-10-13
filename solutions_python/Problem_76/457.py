import sys

def solveCase(words):
	xor = 0
	minVal = None
	sum = 0
	for i in words:
		val = int(i)
		xor ^= val
		sum += val
		if minVal == None or val < minVal:
			minVal = val
	
	if xor == 0:
		return str(sum - minVal)
	else:
		return "NO"
		
if (len(sys.argv) > 1):
	out = (len(sys.argv) > 2) and sys.argv[2] or "google.out"
	
	fileIn = open(sys.argv[1], "r")
	fileOut = open(out, "w")
	
	fileIn.readline()
	line1 = fileIn.readline()
	caseNum = 0
	while line1 != "":
		line2 = fileIn.readline().strip()
		caseNum += 1
		
		answer = solveCase(line2.split(" "))
		
		outstr = "Case #" + str(caseNum) + ": " + answer
		fileOut.write(outstr + "\n")
		
		line1 = fileIn.readline()
	
	fileIn.close()
	fileOut.close()
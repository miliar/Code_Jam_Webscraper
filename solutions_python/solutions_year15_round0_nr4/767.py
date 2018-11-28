#!/usr/bin/python

if __name__ == "__main__":
	outputFile = open("D.out", "w") 
	data = [[int(numStr) for numStr in line.split()] for line in open("D.in", "r")]
	numOfCase = data[0][0]
	dataIndex = 1
	for caseIndex in range(numOfCase):
		X = data[caseIndex + 1][0]
		R = data[caseIndex + 1][1]
		C = data[caseIndex + 1][2]
		MIN = min(R, C)
		
		if X >= 7 or (R*C)%X != 0 or MIN < (X+1)/2:
			result = 'RICHARD'
		elif (MIN == 2 and X == 4) or (MIN == 3 and X == 6):
			result = 'RICHARD'
		else:
			result = 'GABRIEL'

		outputLine = "Case #%d: %s\n" % (caseIndex + 1, result)
		outputFile.write(outputLine)
	outputFile.close()

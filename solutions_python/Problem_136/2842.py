def run_cookie_cutter():
	fileName = 'B-large'
	resultString = ""
	with open(fileName + ".in") as f:
		numCases = int(f.readline()) + 1
		for case in range(1, numCases):
			inputNums = f.readline().split()
			C = float(inputNums[0])
			F = float(inputNums[1])
			X = float(inputNums[2])
			resultString += "Case #" + str(case) + ": " + str(getMinTime(C, F, X)) + "\n"

	outputFile = open(fileName + ".out", "w")
	outputFile.write(resultString)
	outputFile.close()

def getMinTime(C, F, X):
	rate = 2.0
	fastestTime = X / rate
	currentTime = 0
	shouldContinue = True
	while shouldContinue:
		currentTime += (C / rate)
		rate += F
		restOfTime = X / rate
		totalToTest = currentTime + restOfTime
		if totalToTest < fastestTime:
			fastestTime = totalToTest
		else:
			shouldContinue = False
	return fastestTime

if __name__ == '__main__': 
	import sys
	run_cookie_cutter()
#!/usr/bin/python

def solveCookies(initialRate, farmCost, farmRateBoost, target):
	totalTime = 0.0
	currentRate = initialRate
	while(True):
		# how long does it take if we just wait
		waitTime = target/currentRate
		
		# how long does it take if buy one more farm
		nextFarmTime = farmCost/currentRate
		buyTime = nextFarmTime + target/(currentRate+farmRateBoost)
		
		if (waitTime < buyTime):
			totalTime += waitTime
			break
		else:
			totalTime += nextFarmTime
			currentRate += farmRateBoost

	return totalTime
	

f = open("input.txt")
numTests = int(f.readline())
output = ""
for i in range(numTests):
	[constC, constF, constX] = f.readline().split(' ')
	constC = float (constC)
	constF = float (constF)
	constX = float (constX)

	time = solveCookies(2.0, constC, constF, constX)
	output +=  "Case #" + str(i+1) + ": " + str(time) + '\n'

fout = open("output.txt", "w")
fout.write(output)


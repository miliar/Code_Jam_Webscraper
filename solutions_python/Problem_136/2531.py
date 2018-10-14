#! python3

from os import system

import sys
sys.stdout = open("B-large-output.txt", "w")

f = open("B-large.in", "r")
input = f.read().strip()
input = input.split('\n')
del input[0]

for lineKey, line in enumerate(input):
	caseArray = line.split()
	cookiesPerSecond = 2
	tentativeTime = float(caseArray[2]) / cookiesPerSecond
	totalFarmTime = 0
	acceptedTime = tentativeTime + 1
	while tentativeTime < acceptedTime:	
		acceptedTime = tentativeTime
		totalFarmTime += float(caseArray[0]) / cookiesPerSecond
		cookiesPerSecond += float(caseArray[1])
		manualClicking = float(caseArray[2]) / cookiesPerSecond
		tentativeTime = totalFarmTime + manualClicking
	print("Case #" + str(lineKey + 1) + ": " + "{0:.7f}".format(acceptedTime))
		
system("pause")
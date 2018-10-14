#!/usr/bin/python3
inputFile = "2_large.in"

def processTestCase(number):
	while number > 0:
		if isTidy(number):
			return number
		number -= getMinSub(number)

def isTidy(number):
	strnum = str(number)
	for i in range(len(strnum) - 1):
		if strnum[i] > strnum[i+1]:
			return 0
	return 1

def getMinSub(number):
	strnum = str(number)
	for i in range(len(strnum) - 1):
		if strnum[i] > strnum[i+1]:
			return int(strnum[i+1:]) + 1

with open(inputFile) as f:
	content = f.read().split("\n")[1:-1]
	i = 1
	for line in content:
		print("Case #%d: %d" % (i, processTestCase(int(line))))
		i += 1


#!/usr/bin/python

def allEnginesUsed(eng):
	for key in eng.keys():
		if eng[key] == False:
			return False
	return True

def resetEngines(eng):
	for key in eng.keys():
		eng[key]= False

def findRemainingEngine(eng):
	for key in eng.keys():
		if eng[key] == False:
			return key
	return "ERROR"
	

input = open("A-large.in", "r")
out = open("output.txt", "w")

numTestCases = int(input.readline())
for tcNum in range(numTestCases):
	print("--------------")
	numSearchEngines = int(input.readline())
	engineUsage = {}
	switchCount = 0
	for i in range(numSearchEngines):
		engineName = input.readline().strip()
		print engineName
		engineUsage[engineName] = False
	print("--")

	numQueries = int(input.readline())
	for i in range(numQueries):
		thisQuery = input.readline().strip()
		engineUsage[thisQuery] = True
		if allEnginesUsed(engineUsage):
			print("* Switch from " + thisQuery)
			resetEngines(engineUsage)
			switchCount = switchCount + 1
			engineUsage[thisQuery] = True
		print(thisQuery)
	
	out.write("Case #" + str(tcNum + 1) + ": " + str(switchCount) + "\n")
	print("* Finish with " + findRemainingEngine(engineUsage))
	print("* Case #" + str(tcNum) + ": " + str(switchCount) + "\n")

out.close()
input.close()

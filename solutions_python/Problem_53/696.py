#	Project:	Google Code Jam
#	Problem:	Snapper Chain
#	File:		snapperchain.py
#	Date:		8 May 2010
#	Author:		Christopher Busby

input = "A-small-attempt0.in"
output = input.replace(".in", ".out")

fileInput = open(input, "r")
fileOutput = open(output, "w+")

testCases = int(fileInput.readline())

def snap(snappers):
	index = 0
	while(index < len(snappers) and snappers[index] != 0):
		index += 1
	for i in range(0, index + 1):
		if(i + 1 > len(snappers)):
			continue
		snappers[i] += 1
		snappers[i] %= 2
	return snappers

for i in range(0, testCases):
	info = fileInput.readline().split(" ")
	for j in range(0, len(info)):
		info[j] = int(info[j])
	
	snappers = []
	for j in range(0, info[0]):
		snappers.append(0)
	
	for j in range(0, info[1]):
		snappers = snap(snappers)
	
	result = "ON"
	if 0 in snappers:
		result = "OFF"
	
	fileOutput.write("Case #" + str(i + 1) + ": " + result + "\n")
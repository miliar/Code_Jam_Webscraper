#	Project:	Google Code Jam
#	Problem:	Picking Up Chicks
#	File:		pickingupchicks.py
#	Date:		22 May 2010
#	Author:		Christopher Busby

input = "B-large.in"
output = input.replace(".in", ".out")

fileInput = open(input, "r")
fileOutput = open(output, "w+")

testCases = int(fileInput.readline())

def findSwaps(chickens, environ):
	swaps = 0
	count = 0
		
	j = len(chickens) - 1
	while(count < environ[1]):
		if(j < 0):
			return -1
		chicken = chickens[j]
		distance = (environ[2] - chicken[0])
		#print chicken
		if(distance <= environ[3] * chicken[1]):
			swaps += (len(chickens) - 1) - j
			count += 1
			chickens.remove(chicken)
		j -= 1
		
	return swaps

for i in range(0, testCases):
	environ = fileInput.readline().split(" ")
	for j in range(0, len(environ)):
		environ[j] = int(environ[j])
	pos = fileInput.readline().split(" ")
	for j in range(0, len(pos)):
		pos[j] = int(pos[j])
	vel = fileInput.readline().split(" ")
	for j in range(0, len(vel)):
		vel[j] = int(vel[j])
		
	chickens = []
	for j in range(0, len(pos)):
		chickens.append([pos[j], vel[j]])
	swaps = findSwaps(chickens, environ)
	if(swaps < 0):
		swaps = "IMPOSSIBLE"
		
	fileOutput.write("Case #" + str(i + 1) + ": " + str(swaps) + "\n")

fileOutput.close()
fileInput.close()
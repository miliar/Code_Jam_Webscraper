#	Project:	Google Code Jam
#	Problem:	Theme Park
#	File:		themepark.py
#	Date:		8 May 2010
#	Author:		Christopher Busby

input = "C-large.in"
output = input.replace(".in", ".out")

fileInput = open(input, "r")
fileOutput = open(output, "w+")

testCases = int(fileInput.readline())

def calculateEuros(r, k, groups):
	seen = []
	totals = []
	
	euros = 0
	index = 0
	while(True):
		start = index
		if(start in seen):
			break
		total = 0
		while(True):
			if(total + groups[index] > k):
				break
			total += groups[index]
			index += 1
			index %= len(groups)
			if(index == start):
				break
		seen.append(start)
		totals.append(total)

	ridePattern = seen.index(start)
	rides = len(seen) - ridePattern
	
	total = 0
	for i in range(ridePattern, len(seen)):
		total += totals[i]
	
	for i in range(0, ridePattern):
		euros += totals[i]
		r -= 1
	
	euros += (r / rides) * total
	
	ridesLeft = (r % rides)
	for i in range(ridePattern, ridePattern + ridesLeft):
		euros += totals[i]
		
	return euros

for i in range(0, testCases):
	info = fileInput.readline().split(" ")
	for j in range(0, len(info)):
		info[j] = int(info[j])
	groups = fileInput.readline().split(" ")
	for j in range(0, len(groups)):
		groups[j] = int(groups[j])
	
	euros = calculateEuros(info[0], info[1], groups)
	
	fileOutput.write("Case #" + str(i + 1) + ": " + str(euros) + "\n")
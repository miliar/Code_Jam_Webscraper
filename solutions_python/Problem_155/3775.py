inFile = open("testCases.txt", "r")
outfile = open("output.txt", "w")

testCases = int(inFile.readline())

for j in range(testCases - 1):
	maxShyness = inFile.readline().split()
	shynesses = maxShyness[1]
	maxShyness = int(maxShyness[0])
	numberStanding = 0
	friendsNeeded = 0
	i = 0
	while i <= maxShyness:
		if int(shynesses[i]) > 0:
			if numberStanding >= i:
				numberStanding += int(shynesses[i])
			else:
				friendsNeeded += (i - numberStanding)
				numberStanding += (friendsNeeded + int(shynesses[i]))
		i += 1	
	outfile.write("Case #" + str(j + 1) + ": " + str(friendsNeeded) + "\n")
maxShyness = inFile.readline().split()
shynesses = maxShyness[1]
maxShyness = int(maxShyness[0])
numberStanding = 0
friendsNeeded = 0
i = 0
while i <= maxShyness:
	if int(shynesses[i]) > 0:
		if numberStanding >= i:
			numberStanding += int(shynesses[i])
		else:
			friendsNeeded += (i - numberStanding)
			numberStanding = i + 1
	i += 1	
outfile.write("Case #" + str(testCases) + ": " + str(friendsNeeded))
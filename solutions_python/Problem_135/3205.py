file = open("A-small-attempt2.in", 'r')
sol = open ("smallOutput.txt", "w")

cases = int(file.readline())
for case in range (0, cases):
	#do the thing for every sample
	
	#read the data
	pick1 = int(file.readline())
	original = []
	for i in range (0, 4):
		temp = file.readline()
		temp = temp.split()
		temp = map (int, temp)
		original += [temp]
	pick2 = int(file.readline())
	shuffled = []
	for i in range (0, 4):
		temp = file.readline()
		temp = temp.split()
		temp = map (int, temp)
		shuffled += [temp]
	
	selectedRow1 = original[pick1-1]
	selectedRow2 = shuffled[pick2-1]
	validPicks = 0
	thecard = -1
	for card in selectedRow1:
		if card in selectedRow2:
			validPicks +=1
			thecard = card
	if validPicks == 1:
		print "Case #%d: %d" %(case+1, thecard)
		sol.write("Case #%d: %d\n" %(case+1, thecard))
	elif (validPicks > 1):
		print "Case #%d: Bad magician!" %(case+1)
		sol.write("Case #%d: Bad magician!\n" %(case+1))
	else:
		print "Case #%d: Volunteer cheated!" %(case+1)
		sol.write("Case #%d: Volunteer cheated!\n" %(case+1))

sol.close()
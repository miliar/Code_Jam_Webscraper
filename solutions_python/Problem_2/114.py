# Turns a string of departure and arrival times into a list
def generateTimingList(timingString):
	if (len(timingString.strip()) == 0): # No trips in that direction
		return []
	
	l = []
	
	for line in timingString.strip().split('\n'):
		hours = line.strip().split()
		#print "TEST", line, hours
		
		dep = hours[0].split(":")
		ar = hours[1].split(":")
		
		#print dep, ar
		
		# I decided to store all times as minutes since midnight, because it's most convienient.
		depTime = int(dep[0])*60+int(dep[1])
		arTime = int(ar[0])*60+int(ar[1])
		
		tup = (depTime, arTime)
		
		#print tup
		
		l.append(tup)
	
	#print l
	return l

# Checks if any trains are departing/arriving at the specified time	
def checkMinute(AB, BA, time, trainsAtA, trainsAtB, trainsNeeded, turn):
	# Have to seperate them out so that trains arrive and then depart, otherwise it doesn't work
	
	for tup in AB:
		if (tup[1]+turn == time):
			# Train arriving at B now ready
			trainsAtB += 1
	for tup in BA:
		if (tup[1]+turn == time):
			# Train arriving at A now ready
			trainsAtA += 1
	
	for tup in AB:					
		if (tup[0] == time):
			# Train departing from A
			if (trainsAtA > 0):
				trainsAtA-=1
			else:
				trainsNeeded[0]+=1

	for tup in BA:		
		if (tup[0] == time):
			# Train departing from B
			if (trainsAtB > 0):
				trainsAtB-=1
			else:
				trainsNeeded[1]+=1
			
	return trainsAtA, trainsAtB, trainsNeeded

in_file = open("B-large.in", "r")
out_file = open("output.txt", "w")
minutesInDay = 1440
case_num = 1

num_cases = int(in_file.readline())

#print num_cases

for i in range(num_cases):
	ABTripsS = ""
	BATripsS = ""

	turnaround = int(in_file.readline())
	
	NAB = in_file.readline().split()
	
	NA = int(NAB[0])
	
	NB = int(NAB[1])
	
	#print "NAB", NAB, NA, NB
	
	for v in range(NA):
		ABTripsS += in_file.readline()
	
	for v in range(NB):
		BATripsS += in_file.readline()
		
	#print "AB", ABTripsS, "BA", BATripsS

	ABTrips = generateTimingList(ABTripsS)
	BATrips = generateTimingList(BATripsS)
	
	# Status tracks the trains at A, trains at B, and trains needed (a nested list with [0] being at A and [1] being at B
	status = [0, 0, [0, 0]]

	for minute in range(minutesInDay):
		status = checkMinute(ABTrips, BATrips, minute, status[0], status[1], status[2], turnaround)
		
	print status[2]

	out_file.write("Case #" + str(case_num) + ": " + str(status[2][0]) + " " + str(status[2][1]) + "\n")
	
	case_num +=1

in_file.close()
out_file.close()
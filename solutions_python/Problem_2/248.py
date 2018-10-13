ARRIVE_A = 1
ARRIVE_B = 2
LEAVE_A = 3
LEAVE_B = 4

def parseTime(str, startIdx):
	n = (int(str[startIdx+0]) * 10 + int(str[startIdx+1])) * 60 + (int(str[startIdx+3]) * 10 + int(str[startIdx+4]))
	return n
	
def mySort(x, y):
	timeCmp = cmp(x[0], y[0])
	if timeCmp == 0:
		return cmp(x[1], y[1])
	return timeCmp

def doCase(fi, fo, caseIdx):
	turnaroundTime = int(fi.readline())
	
	strNumEntries = fi.readline()
	numABroutes = int(strNumEntries[:strNumEntries.index(' ')])
	numBAroutes = int(strNumEntries[strNumEntries.index(' '):])
	#print numABroutes, numBAroutes
	events = []
	for i in range(numABroutes):
		line = fi.readline()
		leaveTime = parseTime(line, 0)
		arriveTime = parseTime(line, 6) + turnaroundTime
		events.append([leaveTime, LEAVE_A])
		events.append([arriveTime, ARRIVE_B])
		
		#print leaveTime/60, ':', leaveTime%60, ' ', arriveTime/60, ':', arriveTime%60
		#print leaveTime, arriveTime		
		
	for j in range(numBAroutes):
		line = fi.readline()
		leaveTime = parseTime(line, 0)
		arriveTime = parseTime(line, 6) + turnaroundTime
		events.append([leaveTime, LEAVE_B])
		events.append([arriveTime, ARRIVE_A])
	
	events.sort(mySort)
	#print events
	
	startingA = 0
	startingB = 0
	currentA = 0
	currentB = 0
	
	for evt in events:
		code = evt[1]
		if code == ARRIVE_A:
			currentA = currentA + 1
		elif code == ARRIVE_B:
			currentB = currentB + 1
		elif code == LEAVE_A:
			if currentA == 0:
				startingA = startingA + 1
			else:
				currentA = currentA - 1
		elif code == LEAVE_B:
			if currentB == 0:
				startingB = startingB + 1
			else:
				currentB = currentB - 1
				
	fo.write("Case #%d: %d %d\n" % (caseIdx, startingA, startingB))

fi = open("B-large.in", "r")
fo = open("B-large.out", "w")

numCases = int(fi.readline())
for i in range(numCases):
	doCase(fi, fo, i+1)

fi.close()
fo.close()

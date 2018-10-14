def convertTomaxs(s):
	return int(s[0:2])*60 + int(s[3:5]) ,int(s[6:8])*60 + int(s[9:11])
	
input = file("B-large.in")
totalNumber = int(input.readline())
for n in range(totalNumber):
	turnAroundTime = int(input.readline())
	tripsToA ,tripsToB =  map(int,input.readline().split())
	arriveAtA = []
	leaveA = []
	arriveAtB = []
	leaveB = []
	for trips in range(tripsToA):
		a,b = convertTomaxs(input.readline())
		leaveA += [a]
		arriveAtB += [b+turnAroundTime]
	for trips in range(tripsToB):
		b,a = convertTomaxs(input.readline())
		leaveB += [b]
		arriveAtA += [a+turnAroundTime]
	
	arriveAtA.sort()
	leaveA.sort()
	arriveAtB.sort()
	leaveB.sort()
	atA = 0
	atB = 0
	maxAtA = 0
	maxAtB = 0
	for time in range(60*24):
		atA -= arriveAtA.count(time)
		atB -= arriveAtB.count(time)
		atA += leaveA.count(time)
		atB += leaveB.count(time)
		maxAtA = max(atA,maxAtA)
		maxAtB = max(atB,maxAtB)
	print 'Case #%i: %i %i' %(n+1,maxAtA,maxAtB)
			

import sys

input = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

totalTrials = int(input.readline())
trialsCompleted = 0

def compareTimes(t1, t2):
	t1h,t1m = map(int, t1.split(":"))
	t2h,t2m = map(int, t2.split(":"))
	if t1h < t2h:
		return -60
	elif t1h > t2h:
		return 60
	else:
		return t1m-t2m

def canReuseTrain(arrival, departure, turnaround):
	return (compareTimes(departure, arrival) >= turnaround)

def cmpByStartTime(train1, train2):
	t1start,t1end = train1
	t2start,t2end = train2
	return compareTimes(t1start,t2start)

def cmpByEndTime(train1, train2):
	t1start,t1end = train1
	t2start,t2end = train2
	return compareTimes(t1end,t2end)

def getOneWayReq(turnaroundTime, going, coming):
	numGoing = len(going)
	numComing = len(coming)
	trainUsed = [False]*numComing
	needed = 0
	for depart, arrive in going:
		n = 0
		accountedFor = False
		while n < numComing:
			comeDepart, comeArrive = coming[n]
			if not canReuseTrain(comeArrive, depart, turnaroundTime):
				needed += 1
				accountedFor = True
				break
			else:
				if not trainUsed[n]:
					trainUsed[n] = True
					accountedFor = True
					break
			n += 1
		if not accountedFor:
			needed += 1
	return needed

def findTrainRequirements(turnaroundTime, ab, ba):
	abNeeded = 0
	baNeeded = 0
	numAtrains = len(ab)
	numBtrains = len(ba)
	ab.sort(cmpByStartTime)
	ba.sort(cmpByEndTime)
	abNeeded = getOneWayReq(turnaroundTime, ab, ba)

	ab.sort(cmpByEndTime)
	ba.sort(cmpByStartTime)
	baNeeded = getOneWayReq(turnaroundTime, ba, ab)

	return (abNeeded, baNeeded)

while trialsCompleted < totalTrials:
	trialsCompleted += 1
	turnaroundTime = int(input.readline())
	NA,NB = map(int, input.readline().split())
	n = 0
	aToB = []
	while n < NA:
		aToB.append(input.readline().split())
		n += 1
	bToA = []
	n = 0
	while n < NB:
		bToA.append(input.readline().split())
		n += 1

	out,back = findTrainRequirements(turnaroundTime, aToB, bToA)
	output.write("Case #%s: %d %d\n" % (trialsCompleted, out, back))

input.close()
output.close()


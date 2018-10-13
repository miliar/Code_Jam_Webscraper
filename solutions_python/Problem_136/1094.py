import sys
f = open('B-Large.in', 'r')
numTest = int(f.readline())


fAns = open('ansQ2.txt', 'w')
cookieSec = 2.
def findBestTime(numCookie, C, F, X, time, cookieSec, timeLimit):
	if time > timeLimit:
		return time
	if numCookie >= X:
		return time
	timeList = []
	#buy C
	if (X - numCookie) / cookieSec < C / cookieSec:
		timeList.append(findBestTime(X, C, F, X, time + (X - numCookie) / cookieSec, cookieSec, timeLimit))
	else:
		timeList.append(findBestTime(X, C, F, X, time + (X - numCookie) / cookieSec, cookieSec, timeLimit) )
		timeList.append(findBestTime(numCookie - C, C, F, X, time + C / cookieSec, cookieSec + F, timeLimit))
	#not buy C how many second away from X
	
	

	timeList = sorted(timeList)
	return timeList[0]

	#return the only best time...

def findBestTime1(numCookie, C, F, X, time, cookieSec, timeLimit):
	
	newTimeLimit = sorted(timeLimit)
	
	if time > newTimeLimit[0]:
		return newTimeLimit[0]
	#print time + (X - numCookie) / cookieSec
	
	timeLimit.append(time + (X - numCookie) / cookieSec)
	#print cookieSec, timeLimit
	return findBestTime1(0, C, F, X, time + C / cookieSec, cookieSec + F, timeLimit)
	
def findBestTime2(numCookie, C, F, X, time, cookieSec):
	firstTime = time + X / cookieSec
	while True:
		secondTime = time + C / cookieSec + X / (cookieSec + F)
		#print firstTime, secondTime
		if firstTime < secondTime:
			return firstTime
		#update time
		firstTime = secondTime
		time = time + C / cookieSec
		cookieSec += F
	#update cookieSec
for i in range(numTest):
	
	line = f.readline().strip().split()
	C = float(line[0])
	F = float(line[1])
	X = float(line[2])

	

	#fAns.write('Case #'+str(i + 1) + ': ' + str(findBestTime(0, C, F, X, 0, cookieSec, X / cookieSec)) + '\n')
	#fAns.write('Case #'+str(i + 1) + ': ' + str(findBestTime1(0, C, F, X, 0, cookieSec, [X / cookieSec])) + '\n')
	fAns.write('Case #'+str(i + 1) + ': ' + str(findBestTime2(0, C, F, X, 0, cookieSec)) + '\n')

fAns.close()
f.close()
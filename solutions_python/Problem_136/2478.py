import sys

fileRead = open(sys.argv[1]).readlines()
C = []
F = []
X = []
cookieCount = 0
timeCount = 0
ResultTime = {}
farmCount = 0

numberOfTestCases = int(fileRead[0].replace("\n",""))

for i in range(1,len(fileRead)):
	C.append(float(fileRead[i].replace("\n","").split(" ")[0]))
	F.append(float(fileRead[i].replace("\n","").split(" ")[1]))
	X.append(float(fileRead[i].replace("\n","").split(" ")[2]))

#print X
for test in range(len(C)):
	timeCount = 0
	farmCount = 0
	if C[test] > X[test]:
		timeCount = X[test]/2
	else:
		while(True):
			if farmCount == 0:
				inc = 2
				cookieCount +=2
			else:
				inc = 2 + F[test]*farmCount
				cookieCount += inc
			
			if (X[test]/inc) > ((C[test]/inc) + (X[test]/(inc + F[test]))):
				farmCount += 1
				timeCount += C[test]/inc
			else:
				timeCount += X[test]/inc
				break
	ResultTime[test] = timeCount

#print ResultTime
for i in ResultTime.keys():
	print "Case #" + str(i+1) + ": " + "%.7f" % ResultTime[i]


	
			

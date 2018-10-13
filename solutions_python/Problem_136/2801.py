# cookieclicker.py
#
# Nate Beatty
# http://natebeatty.com
# April 12, 2014
#
# Google Code Jam | Qualification Round
# Problem B. Cookie Clicker Alpha
#

# import

def toFloat(array):
	return map(float, array)

def readInput():
	filePath = 'B-large.in.txt'
	f = open(filePath)
	lines = [line.strip().split(' ') for line in f]
	lines = map(toFloat, lines)
	f.close()
	return lines

# returns whether buying another farm would be worthwhile
def shouldBuyFarm(C, F, X, n):
	collectionRate = 2 + (n * F)
	timeToReachGoal = X / collectionRate
	nextCollectionRate = 2 + ((n + 1) * F)
	timeToBuyFarm = C / collectionRate
	if (timeToReachGoal < (timeToBuyFarm + (X / nextCollectionRate))): return False
	return True

def optimalFarmCount(C, F, X):
	n = 0
	while shouldBuyFarm(C, F, X, n):
		n += 1
	return n

def timeToBuyFarms(C, F, n):
	t = 0
	for i in range(n):
		t += (C / ((i * F) + 2))
		# print 'Adding time ' + str(t)
	return t

def timeToGoal(F, X, n):
	return X / ((F * n) + 2)

def calculateMinimumTime(C, F, X):
	n = optimalFarmCount(C, F, X)
	return timeToBuyFarms(C, F, n) + timeToGoal(F, X, n)

# print shouldBuyFarm(500.0, 4.0, 2000.0, 0)
# print shouldBuyFarm(500.0, 4.0, 2000.0, 1)
# print shouldBuyFarm(500.0, 4.0, 2000.0, 2)
# print shouldBuyFarm(500.0, 4.0, 2000.0, 3)
# print shouldBuyFarm(500.0, 4.0, 2000.0, 4)

# print optimalFarmCount(500.0, 4.0, 2000.0)

# print timeToGoal(4.0, 2000.0, 3)

txtinput = readInput()
cases = txtinput[0][0]

for i in range(int(cases)):
	case = txtinput[i+1]
	print 'Case #' + str(i+1) + ': ' + str(calculateMinimumTime(case[0], case[1], case[2]))

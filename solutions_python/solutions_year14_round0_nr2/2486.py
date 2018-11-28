import math

farmCost         = 0
farmExtraCookies = 0
goalCookies      = 0

def getint ():
	return int(raw_input())

def getAs (t):
	return t(raw_input())

def toFloat(s):
	return float(s)

def printCase(c, s):
	print "Case #" + str(c) + ": " + str(s)

def timeToGoal (cookies, rate, goalCookies):
	return (goalCookies - cookies) / rate

def timeToNextFarm (cookies, rate, farmCost):
	return (farmCost - cookies) / rate

# just buy farm if it would decreae your distance to the goal
def solve ():
	curRate = 2
	curCookies = 0
	curTime = 0
	while (True):
		curTime += timeToNextFarm(curCookies, curRate, farmCost)
		curCookies += (curCookies + timeToNextFarm(curCookies, curRate, farmCost) * curRate)
		#can buy farm
		if timeToGoal(0, curRate + farmExtraCookies, goalCookies) < timeToGoal(curCookies, curRate, goalCookies):
			curRate    += farmExtraCookies
			curCookies = 0
		else:
			return curTime + timeToGoal(curCookies, curRate, goalCookies)



for i in range(getint()):
	inp = raw_input().split(" ");

	farmCost         = toFloat(inp[0])
	farmExtraCookies = toFloat(inp[1])
	goalCookies      = toFloat(inp[2])

	printCase(i + 1, solve())


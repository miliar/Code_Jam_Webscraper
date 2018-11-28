dbg = 0

def printDbg(*args):
	if dbg: print("".join(args)) 

def getFarm(cookiesLeft, cost, currentRevenue, extraRevenue):
	secondsWOFarm = cookiesLeft/currentRevenue
	secondsWithFarm = (cookiesLeft+cost)/(currentRevenue+extraRevenue)
	return secondsWithFarm < secondsWOFarm
	
def solve(line):
	(C,F,X) = map(lambda v:float(v),line.split(" "))
	printDbg (str(C) + " , " + str(F) + " , " + str(X))
	numCookies = 0
	currentRevenue = 2
	seconds = 0
	while numCookies < X:
		if (numCookies >= C):
			if getFarm(X-numCookies,C,currentRevenue,F):
				printDbg("\tinvesting in a cookie farm")
				numCookies -= C
				currentRevenue +=F
			else:
				seconds += (X-numCookies)/currentRevenue
				numCookies = X
		else:
			step = C if C < X else X
			seconds += (step-numCookies)/currentRevenue
			numCookies = step
		printDbg ("\tcurrent cookie revenue: " + str(currentRevenue) + ", number of cookies: " + str(numCookies) + ", seconds: " + str(seconds)+"\n")
	return seconds

with open('B-large.in') as f:
    input = f.read().splitlines()
numCases = input.pop(0)

f = open('B-large.out', 'w')
for i in range(0,int(numCases)):
	f.write("Case #"+str(i+1)+": " + str(solve(input.pop(0))) + "\n")
	

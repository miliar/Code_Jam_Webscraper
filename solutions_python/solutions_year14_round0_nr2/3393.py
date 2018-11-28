def calculateFarmedTime(currentCookiePerSec, farmcost, farmsToBuy, bonusCookiesPerSec, target):
	farmBuyLength = 0
	for i in range(0, farmsToBuy):
		farmBuyLength += farmcost / (currentCookiePerSec + (bonusCookiesPerSec * i))
		
	finishTime = target / (currentCookiePerSec + (bonusCookiesPerSec * farmsToBuy))
		
	return farmBuyLength + finishTime
	

f = open('B-small-attempt0.in', 'r')
w = open('cookiecutterresults.txt', 'w+')

cases = int(f.readline())

firstlist = []
secondlist = []

for j in range(0, cases):

	cfxlist = f.readline().split()
	
	currentCookiePerSec = 2
	
	farmcost = float(cfxlist[0])
	bonusCookiesPerSec = float(cfxlist[1])
	targetCookies = float(cfxlist[2])
	
	currentTimeLen = -1
	nextTimeLen = -2
	
	i = 0
	while currentTimeLen > nextTimeLen:
	
		currentTimeLen = calculateFarmedTime(2, farmcost, i, bonusCookiesPerSec, targetCookies)
	
		nextTimeLen = calculateFarmedTime(2, farmcost, i+1, bonusCookiesPerSec, targetCookies)
		
		i += 1
		
		currentCookiePerSec += bonusCookiesPerSec


	print "Case #" + str(j+1) + ": " + str(currentTimeLen)
	
	w.write("Case #" + str(j+1) + ": " + str(currentTimeLen) + "\n")
	
w.close()
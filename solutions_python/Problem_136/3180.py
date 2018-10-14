import sys, os

t = int(sys.stdin.readline())

for i in xrange(t):
	c, f, x = map(float, sys.stdin.readline().strip().split())
	cookies = 0
	cookiesPerSecond = 2
	timeSoFar = 0

	while cookies < x:

		timeRemainingWithoutFarm = ((x - cookies)/cookiesPerSecond)
		timeRemainingWithFarm = ((c - cookies)/cookiesPerSecond) + ((x - cookies)/(cookiesPerSecond + f))
		if  timeRemainingWithoutFarm > timeRemainingWithFarm : 
			#buy farm

			timeToBuyFarm = c/cookiesPerSecond
			#cookies -= c
			timeSoFar += timeToBuyFarm
			cookiesPerSecond += f 
			#print "cookies, cookiesPerSecond, timeSofar", cookies, cookiesPerSecond, timeSoFar
			#print "Buy", timeToBuyFarm
		else:
			#do not buy farm
			timeSoFar += timeRemainingWithoutFarm
			cookies = x
			#print "cookies, cookiesPerSecond, timeSofar", cookies, cookiesPerSecond, timeSoFar
			#print "No buy", timeRemainingWithoutFarm
	print "Case #{0}: {1}".format ((i+1), "%.7f" % timeSoFar)

#c cookies needed to get farm
#f extra cookies per second because of farm
#x goal cookies







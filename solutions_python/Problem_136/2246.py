from __future__ import division

T = int(raw_input())

for i in range(0,T):
	[cost, farmSpeed, goal] = [float(x) for x in raw_input().split()]
	seconds = 0
	currentCookies = 0
	rate = 2

	while True:
		gainedForDecision = cost - currentCookies

		if (currentCookies + gainedForDecision >= goal):
			seconds += (goal - currentCookies) / rate
			break
		else:
			currentCookies += gainedForDecision
			seconds += gainedForDecision / rate

			timeWithBuy = (((goal - (currentCookies - cost)) / (rate + farmSpeed))) + seconds
			timeWithoutBuy = ((goal - currentCookies) / rate) + seconds

			if timeWithBuy < timeWithoutBuy:
				currentCookies -= cost
				rate += farmSpeed
			else:
				seconds += (goal - currentCookies) / rate
				break

	print "Case #%d: %.7f" %((i + 1), round(seconds, 7))
from __future__ import division

infile = """INPUT"""

def bestTime(line):
	factoryprice, factoryrate, goal = [float(v) for v in line.split(' ')]
	cookies, elapsed, productionrate = 0, 0, 2

	while True:
		# If we have reached our goal, yay!
		if cookies > goal:
			elapsed -= (cookies-goal)/productionrate
			return elapsed

		# Determine how long until something interesting can happen, then
		# "fast forward" to that point in time by adding cookies
		timeToFactory = (factoryprice/productionrate)
		cookies += productionrate*timeToFactory
		elapsed += timeToFactory

		# How long to win without buying a factory
		withoutPurchase = goal/productionrate

		# How long to win if we buy a factory (note that we have to include
		# the amount of time until we can buy a factory in this calculathon)
		withPurchase = timeToFactory + (goal/(factoryrate+productionrate))

		# If buying a factory is better, buy it!
		if withPurchase < withoutPurchase:
			productionrate += factoryrate
			cookies -= factoryprice

casenum = 0
for line in infile.split('\n'):
	casenum += 1
	print 'Case #{}: {}'.format(casenum,'{0:.7f}'.format(bestTime(line)))
	

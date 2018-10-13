from collections import deque

noRides = int(raw_input())
for iter in xrange(noRides):
	moneyMade = 0
	noTurns, noAllowed, noGroups = [long(x) for x in raw_input().strip().split()]
	groups = deque([long(x) for x in raw_input().strip().split()])
	for turn in xrange(noTurns):
		noRiding = 0
		noGRiding = 0
		while noRiding + groups[0] <= noAllowed and noGRiding < len(groups):
			noRiding += groups[0]
			noGRiding += 1
			groups.rotate(-1)
		moneyMade += noRiding
	print "Case #%i: %i" % ((iter + 1), moneyMade)

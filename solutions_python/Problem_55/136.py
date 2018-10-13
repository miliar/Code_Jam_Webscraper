import sys
sys.setrecursionlimit(5000)
class RideInfo:
	rideSum = None
	nextRide = None
	prevRide = None
	cycleSum = 0
	cycleNumRides = 0
	cycleComplete = False
	# constructor
	def __init__(self, rideSum, nextRide, prevRide):
		self.rideSum = rideSum
		self.nextRide = nextRide
		self.prevRide = prevRide
	
	# update cycle sum
	def addToCycleSum(self, x):
		if self.cycleComplete:
			return
		self.cycleSum += x
		self.cycleNumRides += 1
		if self.prevRide is not None:
			self.prevRide.addToCycleSum(x)
#

def long_list():
	return map(lambda x: long(x), raw_input().split(' '))

T = int(raw_input())
for t in range(0, T):
	#print "start case", (t+1)
	(R, k, N) = long_list()
	heads = {}
	spos = 0
	groups = long_list()
	gsum = reduce(lambda x,y: x+y, groups)
	if gsum <= k:
		answer = gsum * R
	else:
		answer = 0
		caller = None
		r = 0
		while r < R:
			if spos in heads:
				head = heads[spos]
				# cycle is complete
				head.cycleComplete = True
				# take as many copies of this cycle that can fit
				remainingRides = R - r # including current ride
				#print "hit cycle, remainingRides=", remainingRides
				numCycleCopies = remainingRides / head.cycleNumRides
				answer += head.cycleSum * numCycleCopies
				r += head.cycleNumRides * numCycleCopies
				#print "hit cycle, cycleNumRides=", head.cycleNumRides, "remainingRides=", remainingRides, "numCycleCopies=", numCycleCopies
				# finish up remaining rides
				if r < R:
					spos = head.nextRide
					answer += head.rideSum
					r += 1
					# i am the caller
					caller = head
				#spos = heads[spos][1]
				#print >> sys.stderr, "got a hit on", spos
				continue
			# take as many as possible
			curK = 0
			orig_spos = spos
			while (curK+groups[spos]) <= k:
				curK += groups[spos]
				spos = (spos + 1) % N
			answer += curK
			# store info and update caller
			caller = heads[orig_spos] = RideInfo(curK, spos, caller)
			caller.addToCycleSum(curK)
			r += 1
			
	print "Case #%d: %d" % (t+1, answer)

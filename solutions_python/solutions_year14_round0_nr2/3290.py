#!/usr/bin/env python

def cookies(farmcost,farmoutput,goal):
	t = 0.0
	cookies = 0.0
	rate = 2.0
	while True:
		assert cookies == 0
		timetogoal = goal / rate
		timetonextfarm = farmcost/rate
		if timetogoal <= timetonextfarm:
			t += timetogoal
			return t
		timetogoalwithfarm = timetonextfarm +  goal/(rate+farmoutput)
		if timetogoal <= timetogoalwithfarm:
			t += timetogoal
			return t
		t+= timetonextfarm
		rate += farmoutput
	return 0

if __name__ == "__main__":
	import sys
	testcases = int(sys.stdin.readline())
	for casenum in range(testcases):
		print "Case #%s:" % (casenum+1,),cookies(*map(float,sys.stdin.readline().split()))

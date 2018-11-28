#!/usr/bin/env python
"""
  Apologies for the Latham-style variable names. I lost the ability to code
  when doing this one...
"""
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	T = int(sys.stdin.readline())
	for t in xrange(T):
		cost, bonus, target = map(float, sys.stdin.readline().split(" "))
		rate = 2.0
		nextFarmTime = 0.0
		totalTime = 0.0
		timeToTarget = target / rate
		done = False
		
		while not done:
		  # Buy next farm.
		  nextFarmTime = cost / rate
		  rate = rate + bonus
		  nextTimeToTarget = target / rate
		  
		  # Is it worth it?
		  if timeToTarget > (nextTimeToTarget + nextFarmTime):
		    timeToTarget = nextTimeToTarget
		    totalTime += nextFarmTime
		  else:
		    totalTime += timeToTarget
		    done = True
		
		print "Case #%d: %0.7f" % (t + 1, totalTime)

if __name__ == "__main__":
	sys.exit(main())


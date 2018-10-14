#! /usr/bin/env python

def getSlowestTime(D, horses):
	times = list(map( lambda horse: (D - horse['K'])/horse['S'], horses ))
	return max(times)
#.......................................
	
#.......................................
	
#.......................................
	
#.......................................

def cruise_control(D, horses):
	T = getSlowestTime(D, horses)
	return D/T

#.......................................

def getHorse():
	horse_l = inputInts()
	return {'K':horse_l[0], 'S':horse_l[1]}
#.......................................

def inputInts():
	return list( map(lambda i: int(i), input().split()) )

#===========>MAIN FUNCTION<================

if __name__ == "__main__":
	
	# Initialize
	from collections import deque
	n_cases = int( input() )
	cases = []
	
	# Read cases
	for i in range(n_cases):
		# Read D and N
		D,N=inputInts()
		horses = []
		# Read the N lines with K_i and S_i
		for h in range(N):
			horse = getHorse()
			horses.append(horse)
		# Add case to queue
		cases.append([D, horses])
			
	# Print cases
	cases = deque(cases)
	for i in range(n_cases):
		case = cases.popleft()
		print("Case #%d: " % (i+1), cruise_control(*case)) 
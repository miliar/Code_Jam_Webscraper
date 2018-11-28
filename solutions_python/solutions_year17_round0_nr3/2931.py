# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math 

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
	stalls, users = [int(s) for s in input().split(" ")]  
	
	lhs = 0
	rhs = 0
	unassigned = users
	
	if users == stalls:
		unassigned = 0
		
	
	leftlimit = 0
	rightlimit = stalls + 1
	
	# Build the map of toilet cubicles
	occupied = []
	occupied.append(leftlimit)
	occupied.append(rightlimit)
		
	while unassigned > 0:
		score = 0
		if unassigned == users:
			currentpos = math.floor(leftlimit + rightlimit / 2)
			lhs = currentpos - leftlimit - 1 
			rhs = rightlimit - currentpos - 1	
			occupied.append(currentpos)
			unassigned = unassigned - 1
			occupied.sort()
		else:
			for j in range(len(occupied) - 1):
				leftlimit = occupied[j]
				rightlimit = occupied[j+1]
				currentpos = math.floor((leftlimit + rightlimit) / 2)
				lhs = currentpos - leftlimit
				rhs = rightlimit - currentpos
				
				if (max(lhs,rhs) > score):
					score = min(lhs,rhs)
					finalpos = currentpos
				
			occupied.append(finalpos)
			unassigned = unassigned - 1
				
			occupied.sort()
			leftlimit = occupied[occupied.index(finalpos) - 1]
			rightlimit = occupied[occupied.index(finalpos) + 1]
			lhs = finalpos - leftlimit - 1
			rhs = rightlimit - finalpos - 1 
		
	maxdist = max(lhs, rhs)
	mindist = min(lhs, rhs) 
	
	print("Case #{}: {} {}".format(i, maxdist, mindist))
	# check out .format's specification for more formatting options
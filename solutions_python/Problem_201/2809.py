#! /usr/bin/env python

def maxPos(gaps):
	max_pos=0
	for i in range(len(gaps)):
		if gaps[i] >gaps[max_pos]:
			max_pos=i
	return max_pos
#.......................................

def listInsert(gaps,p,items):
	del gaps[p]
	for i in range(len(items)):
		gaps.insert(p+i, items[i])
	return gaps
#.......................................

def addPerson(gaps):
	gap_pos = maxPos(gaps)
	gap = gaps[gap_pos]
	if gap%2==0:
		if gap ==2:
			gaps = listInsert(gaps,gap_pos,[gap//2])
			return 0,gap//2,gaps
		else:
			gaps = listInsert(gaps,gap_pos,[gap//2-1,gap//2])
			return gap//2-1,gap//2,gaps
	else:
		if gap//2 == 0:
			gaps = listInsert(gaps,gap_pos,[])
			return 0,0,gaps
		else:
			gaps = listInsert(gaps,gap_pos,[gap//2,gap//2])
			return gap//2,gap//2, gaps
#.......................................

def bathroomStalls(n, k):
	gaps = [n]
	for i in range(k):
		min, max, gaps = addPerson(gaps)
	return max, min
#.......................................

#===========>MAIN FUNCTION<================

if __name__ == "__main__":
	
	# Initialize
	from collections import deque
	n_cases = int( input() )
	cases = []
	
	# Read cases
	for i in range(n_cases):
		raw_n, raw_k = input().split(' ')
		n,k=[int(raw_n), int(raw_k)]
		cases.append( [n,k] )
	
	# Print cases
	cases = deque(cases)
	for i in range(n_cases):
		max, min = bathroomStalls(*cases.popleft())
		print("Case #%d: %d %d" % (i+1, max, min))
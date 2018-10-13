#!/usr/bin/python
from math import pow 
from string import atoi
from math import floor

data = open('input')
n = atoi(data.readline())
out = open('out', 'w')
for n in range(n):
	case = data.readline()
	R, k, N = case.rsplit()
	strgroups = data.readline().rsplit()
	groups = []
	totalgsize = 0
	for g in strgroups:
		g = atoi(g)
		groups.append(g)
		totalgsize+=g
	groups.reverse()

	dollars = 0
	k = atoi(k)
	R = atoi(R)

	line = []	
	run = 0	
	capacity = 0
	if totalgsize <= k:
		dollars += totalgsize * R
	else:
		while run < R:
			if groups == []:
				groups = line
				groups.reverse()
				line = []
			g = groups.pop()
			if capacity + g == k:
				capacity = 0
				dollars += k
				run += 1
				line.append(g)
			elif capacity + g < k:
				capacity += g 
				line.append(g)
			elif capacity + g > k:
				dollars += capacity 
				capacity = 0
				groups.append(g)
				run += 1

	out.write("Case #%d: %d\n"%(n+1,dollars))


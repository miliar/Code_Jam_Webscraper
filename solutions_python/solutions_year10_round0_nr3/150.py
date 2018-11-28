#!/usr/bin/env python

import math

f = open('C-large.in', 'r')
#f = open('in.random', 'r')

T = int(f.readline())
count = 0
for case in range(0,T):
	euros = 0
	line = f.readline()
	R,k,N =  line.split()
	R, k, N = int(R), int(k), int(N)
	gi = f.readline()
	gi = gi.split()
	for i in range(0,N):
		gi[i] = int(gi[i])

	rails = []
	for i in range(0,N):
		seats_free = k
		groups = 0
		next_group = i
		value = 0
		while (seats_free > 0) and (groups < N):
			if gi[next_group] > seats_free:
				break
			seats_free -= gi[next_group]
			value += gi[next_group]
			groups += 1
			next_group = (next_group + 1)%N
		rails.append({'value':value, 'next': next_group})

	visited = []
	this_group = 0
	for i in range(0,N):
		visited.append(this_group)
		this_group = rails[this_group]['next']
		if this_group in visited:
			start = visited.index(this_group)
			stop = len(visited)-1
			#print "Stop in ", this_group, " (position ",visited.index(this_group),")"
			#print visited
			break

	repeat_len = stop-start+1
	start_value,repeat_value,end_value = 0,0,0
	repeats = int(math.floor((R-start)/repeat_len))
	ending = (R-start)%repeat_len

	for i in range(0,start):
		start_value += rails[visited[i]]['value']

	for i in range(start,len(visited)):
		repeat_value += rails[visited[i]]['value']

	for i in range(start, start+ending):
		end_value += rails[visited[i]]['value']


	euros = start_value + repeats*repeat_value + end_value

	if R <= stop:
		euros = 0
		this_group = 0
		for i in range(0,R):
			euros += rails[this_group]['value']
			this_group = rails[this_group]['next']



	print 'Case #' + str(case+1) + ': '+ str(euros)

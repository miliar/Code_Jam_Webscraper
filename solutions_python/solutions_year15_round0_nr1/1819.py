#!/usr/bin/python

T = int(raw_input())

for t in xrange(T):
	sMax, Ss = raw_input().split()
	
	# Number of people who have already stood up to clap
	up = 0
	# Minimum number of friends you must invite
	friends = 0
	
	for sVal, people in enumerate(Ss):
		if sVal > up:
			friends += sVal - up
			up += sVal - up
		up += int(people)
	
	print "Case #%d: %d" % (t+1, friends)

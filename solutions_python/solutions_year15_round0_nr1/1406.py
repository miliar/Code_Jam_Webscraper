#!/usr/bin/env python
#coding=utf8
tests = input()
for test in range(0, tests):
	line = raw_input()
	sall = line.split()[1]
	friend = 0
	audience = 0
	for s, c in enumerate(sall): 
		if int(c)>0 and int(s) > audience + friend:
			friend += int(s) - audience - friend
		audience += int(c)

	print "Case #" + str(test+1) + ": " + str(friend)


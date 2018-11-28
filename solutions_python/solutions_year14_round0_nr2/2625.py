#!/usr/bin/python
# -*- coding:utf8 -*-

def testCase():
	C,F,X = map(float,raw_input().split(' '))

	r = 2.0 # cookies gained per second
	t = 0.0 # total time required to gain X cookies

	newfarm_needed = True # no 'do: while()' in python
	while newfarm_needed: # makes Jack a dull boy.

		# Does a new farm help us?
		without_newfarm = X/r
		with_newfarm = C/r+X/(r+F)
		if without_newfarm<=with_newfarm:
			newfarm_needed=False # no. Goto trivial ending.
		else:
			t += C/r # yes. Restart from 0 cookies.
			r += F

	# Trivial end with current number of farms
	t += X/r
	return t

T = int(raw_input())
for i in xrange(1,T+1):
	print('Case #%d: %.7f'%(i,testCase()))

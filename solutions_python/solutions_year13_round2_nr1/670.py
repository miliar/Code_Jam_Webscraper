#! /usr/bin/env python2

# I'm sending the output to file on OS!

from __future__ import division
import sys, math
from collections import deque


def solve(input):
	f = open(input)
	n = int(f.readline())
	i = 0
	while i < n:
		mote = int(f.readline().split()[0])
		others = deque(sorted([int(j) for j in f.readline().split()]))
		#print mote
		#print others
		print "Case #"+str(i+1)+": "+str(osmos(mote,others))
		i += 1

def calcMax(mote, n):
	i = 0
	while i < n:
		mote += (mote-1)
		i +=1
	return mote

def osmos(mote, others):
	#others.sort()
	res = 0
	possible = []
	while len(others) != 0:
		if mote > others[0]:
			mote += others.popleft()

		elif calcMax(mote,len(others)) > others[0]:
			possible.append(res + len(others))
			while mote <= others[0]:
				res +=1
				mote += (mote-1)
		else:
			res += len(others)
			break
	if len(possible)>0:
		return min(res, min(possible))
	else:
		return res
		
solve(sys.argv[1])

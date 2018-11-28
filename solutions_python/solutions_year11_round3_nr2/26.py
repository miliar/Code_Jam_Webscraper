#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def doit(line):
	'''
	>>> doit('2 20 8 2 3 5')
	54

	# 4 .5 8 1 8 .5
	>>> doit('1 4 2 2 10 4')
	20
	
	'''
	
	l = map(int, line.strip().split())
	
	boosters = l[0]
	hrs_to_build = l[1]
	dest = l[2]
	C = l[3]
	
	def trip_len(n):
		return l[4:][n % C]

	trips = [trip_len(n) for n in range(dest)]

	b4_booster = 0
	timer = 0
	stub_half = 0
	for trip in trips:
		b4_booster += 1
		if timer + trip * 2 < hrs_to_build:
			timer += trip * 2
		else: 
			stub_half = trip - ((hrs_to_build - timer) * 0.5)
			timer = hrs_to_build
			break		
			
	remaining_trips = trips[b4_booster:]
	remaining_trips.append(stub_half)
	remaining_trips.sort()
	remaining_trips.reverse()

	for n, trip in enumerate(remaining_trips):
		if n < boosters:
			timer += trip
		else:
			timer += trip * 2
			
	return int(timer)

	
def test():
	import doctest, b
	doctest.testmod(b)

def cl():
	f = sys.stdin
	f2 = None
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)
			f2 = open(fn.replace('in','out'), 'w')
			
	cases = int(f.readline())
	l = []
	for n in range(cases):		
		l.append('Case #%d: %s' % (n+1, doit(f.readline())))
			
	if f2:
		f2.write('\n'.join(l))
		f2.close()
	
	if f:
		f.close()

if __name__ == "__main__":
#	test()
	cl()

#!/usr/bin/env python
# encoding: utf-8
"""
Denis Sokolov
Google Code Jam 2010
"""

def solve(rounds, capacity, groups):
	revenue = 0
	for r in xrange(rounds):
		ride = []
		rideSize = 0
		while groups:
			if rideSize + groups[0] > capacity:
				break
			rideSize += groups[0]
			ride.append(groups.pop(0))
		revenue += rideSize
		groups.extend(ride)
	return revenue

def main():
	with open('C-small-attempt0.in') as f:
		t = int(f.readline())
		for case in xrange(t):
			rounds, capacity, groupsCount = map(int, f.readline().split(' '))
			groups = map(int, f.readline().split(' '))
			print 'Case #%d: %s' % (case + 1, solve(rounds, capacity, groups))

if __name__ == '__main__':
	main()

#!/usr/bin/env python

import sys

def parseTime(timeStr):
	hours, minutes = ( int(s) for s in timeStr.split(':') )
	return hours * 60 + minutes

def parseTrips(numTrips):
	departures = []
	arrivals = []
	for _ in range(numTrips):
		depart, arrive = ( parseTime(s) for s in sys.stdin.readline().split() )
		departures.append(depart)
		arrivals.append(arrive)
	return departures, arrivals

def simulate(departures, arrivals, turnaround):
	events = [ ( departure,  1 ) for departure in departures ] \
		+ [ ( arrival + turnaround, -1 ) for arrival in arrivals ]
	# Note: Sorting on second coordinate is important too.
	events.sort()
	trains = 0
	worstShortage = 0
	for time, delta in events:
		trains -= delta
		if trains < worstShortage:
			worstShortage = trains
	return -worstShortage

def solve():
	turnaround = int(sys.stdin.readline())
	tripsA, tripsB = ( int(s) for s in sys.stdin.readline().split() )
	departuresA, arrivalsB = parseTrips(tripsA)
	departuresB, arrivalsA = parseTrips(tripsB)
	return '%s %s' % (
		simulate(departuresA, arrivalsA, turnaround),
		simulate(departuresB, arrivalsB, turnaround)
		)

cases = int(sys.stdin.readline())
for case in range(cases):
	print 'Case #%d: %s' % (case + 1, solve())

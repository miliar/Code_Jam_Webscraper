#!/usr/bin/env python

import sys

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    R, k, N = map(long, inputfile.readline().strip().split())
    g = map(long, inputfile.readline().strip().split())

    y = 0
    first_ride = [None] * N
    ride_groups = [None] * N
    ride_seats = [None] * N
    ride = 0
    start = 0
    while ride < R:
	if first_ride[start] is not None:
	    break
	ridestart = start
	seats = 0
	groups = 0
	while seats + g[start] <= k and groups < N:
	    seats += g[start]
	    groups += 1
	    start += 1
	    if start >= N:
		start = 0
	    if start == ridestart:
		break
	first_ride[ridestart] = ride
	ride_groups[ridestart] = groups
	ride_seats[ridestart] = seats
	ride += 1
	y += seats

    if ride < R:
	cyclelen = ride - first_ride[start]
	if R - ride >= cyclelen:
	    cycles = (R - ride) / cyclelen
	    cycle_euros = 0
	    cycle_start = start
	    while True:
		cycle_euros += ride_seats[start]
		start = (start + ride_groups[start]) % N
		ride += 1
		if start == cycle_start:
		    break
	    y += cycle_euros * cycles
	    ride += (cycles - 1) * cyclelen

	while ride < R:
	    y += ride_seats[start]
	    start = (start + ride_groups[start]) % N
	    ride += 1

    print "Case #%d: %d" % (case, y)

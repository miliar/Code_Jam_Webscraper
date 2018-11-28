#!/usr/bin/python

from sys import argv
from datetime import timedelta as delta
input = file( argv[1] )

# define problem vars
n = input.next().strip()	# Number of test cases

# helper functions
def run_test( input ):
	t = delta( minutes=int( input.next() ) )	# Turnaround time
	na, nb = input.next().strip().split(' ')
	na, nb = int( na ), int( nb )
	nt = na + nb
	a_starts, b_starts = 0, 0

	# gather route data
	routes = []
	for route in input:
		start, stop = route.strip().split(' ')
		start_h, start_m = start.split(':')
		stop_h, stop_m = stop.split(':')
		route_type = len( routes ) < na
		routes.append( 
			( delta( hours=int( start_h ), minutes=int( start_m ) ),
			  delta( hours=int( stop_h ), minutes=int( stop_m ) ), route_type ) )
		if len( routes ) == nt: break

	# make sure we don't jump around
	routes.sort()
	
	# follow each train down their route
	while len( routes ):
		train = routes[0]
		routes.remove( train )
		start, end, a_route = train
		
		if a_route: a_starts += 1
		else: b_starts += 1

		# determine what other stops this train can make
		while True:
			start = end + t
			a_route = not a_route
			try:
				for route in routes:
					if start <= route[0] and route[2] == a_route:
						train = route
						start, end, a_route = train
						routes.remove( route )
						raise Exception
			except: continue
			break
	
	return a_starts, b_starts

# run tests
for i in range( 1, int(n) + 1 ): 
	start_a, start_b = run_test( input )
	print "Case #%s: %s %s" % ( i, start_a, start_b )


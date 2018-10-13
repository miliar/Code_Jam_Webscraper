#!/usr/bin/env python

import sys

def main():
	if len( sys.argv ) == 1:
		print 'Usage: trains inputfile'
		sys.exit(1)
	
	f = open( sys.argv[1], 'r' )
	lines = f.read().split('\n')[:-1]
	f.close()

	cases = int( lines[0] )
	del lines[0]
	
	for i in xrange( cases ):
		turnaround = int( lines[0] )
		del lines[0]
		trips = lines[0].split(' ')
		del lines[0]
		NA = int( trips[0] )
		NB = int( trips[1] )
		tripsA = lines[:NA]
		del lines[:NA]
		tripsB = lines[:NB]
		del lines[:NB]

		print 'Case #%d: %s' % ( i+1, trainsRequired( turnaround, tripsA, tripsB ) )


def trainsRequired( turnaround, tripsA, tripsB, trainsA = 0, trainsB = 0, check = True ):
	(departuresA, arrivalsB) = parseSchedule( tripsA )
	(departuresB, arrivalsA) = parseSchedule( tripsB )

	debug = False

	if debug: print '\tTurnaround time: %d' % turnaround

	requiredA = 0
	requiredB = 0
	for i in xrange( 2400 ):
		if arrivalsA.get(i-turnaround) != None:
			trainsA += arrivalsA[i-turnaround]
			if debug:
				for j in range( arrivalsA[i-turnaround] ):
					print '\tTrain arrived in A at %d (%d)' % (i-turnaround, trainsA)
		if arrivalsB.get(i-turnaround) != None:
			trainsB += arrivalsB[i-turnaround]
			if debug:
				for j in range( arrivalsB[i-turnaround] ):
					print '\tTrain arrived in B at %d (%d)' % (i-turnaround, trainsB)
		if departuresA.get(i) != None:
			trainsA -= departuresA[i]
			if debug:
				for j in range( departuresA[i] ):
					print '\tTrain departs A at %d (%d)' % (i, trainsA)
		if departuresB.get(i) != None:
			trainsB -= departuresB[i]
			if debug:
				for j in range( departuresB[i] ):
					print '\tTrain departs B at %d (%d)' % (i, trainsB)
		
		if trainsA < 0:
			requiredA += abs(trainsA)
			trainsA = 0
		if trainsB < 0:
			requiredB += abs(trainsB)
			trainsB = 0
	
	output = '%d %d' % ( requiredA, requiredB )

	if check:
		if not trainsRequired( turnaround, tripsA, tripsB, requiredA, requiredB, False ) == '0 0':
			output += ' (failed!)'

	return output


def parseSchedule( trips ):
	departures = {}
	arrivals = {}

	for trip in trips:
		times = trip.split(' ')
		depart = int( times[0][:2] + times[0][3:] )
		arrive = int( times[1][:2] + times[1][3:] )
		if departures.get( depart ) == None:
			departures[depart] = 1
		else:
			departures[depart] += 1
		if arrivals.get( arrive ) == None:
			arrivals[arrive] = 1
		else:
			arrivals[arrive] += 1

	return (departures, arrivals)
		



if __name__ == '__main__':
	main()


#! /usr/bin/python
import datetime

f = open( "atest" , "r" )
o = open( "atest_output", "w" )

def isGreaterThan( t1, t2 ):
	if t1 > t2:
		return 1
	elif t1 < t2:
		return -1
	else:
		return 0

def isGreaterThanBegin( t1, t2 ):
	return isGreaterThan( t1[0][0], t2[0][0] )

def isGreaterThanEnd( t1, t2 ):
	return isGreaterThan( t1[0][1], t2[0][1] )

def addTimes( t1, t2 ):
	newMinutes = t1.minute + t2.minute
	newHours = t1.hour + t2.hour
	while newMinutes > 59:
		newHours += 1
		newMinutes -= 60
	if newHours > 23:
		newHours = 23
		newMinutes = 59
	return datetime.time( newHours, newMinutes )

for case in range( int( f.readline() ) ):
	
	htime = 0
	time = int( f.readline() )
	while time > 59:
		htime += 1
		time -= 60

        turnaroundTime = datetime.time( htime, time )
	tripsAB, tripsBA = map( int, f.readline().split() )
	tripsFromA = []
	tripsFromB = []
	
	for t in range( tripsAB ):
		times = f.readline().strip().split()
		timea = times[0].split(':')
		times[0] = datetime.time( int( timea[0] ), int( timea[1] ) )
                timea = times[1].split(':')
                times[1] = datetime.time( int( timea[0] ), int( timea[1] ) )
		tripsFromA.append( [times, True] ) 

        for t in range( tripsBA ):
                times = f.readline().strip().split()
                timea = times[0].split(':')
                times[0] = datetime.time( int( timea[0] ), int( timea[1] ) )
                timea = times[1].split(':')
                times[1] = datetime.time( int( timea[0] ), int( timea[1] ) )
                tripsFromB.append( [times, True] )

	tripsFromA.sort( isGreaterThanEnd )
	tripsFromB.sort( isGreaterThanBegin ) 

	for trainA in tripsFromA[:]:
		for trainB in tripsFromB[:]:
			if trainB[1] == True and addTimes( trainA[0][1], turnaroundTime ) <= trainB[0][0]:
				trainB[1] = False
				tripsBA -= 1
				break

        tripsFromA.sort( isGreaterThanBegin )
        tripsFromB.sort( isGreaterThanEnd )

#	print tripsFromA
#	print tripsFromB
	
        for trainB in tripsFromB[:]:
		for trainA in tripsFromA[:]:
        		if trainA[1] == True and addTimes( trainB[0][1], turnaroundTime ) <= trainA[0][0]:
				trainA[1] = False
                               	tripsAB -= 1
				break

	#print tripsFromA
	
	o.write( "Case #" + str( case + 1 ) + ": " + str( tripsAB ) + " " + str( tripsBA ) + "\n" )

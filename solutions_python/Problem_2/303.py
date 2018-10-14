#!/usr/bin/python

import sys

def getMins(timeStr):
	parts = timeStr.split(':')
	return (int(parts[0]) * 60) + int(parts[1])

def getTrips(file, howMany):
	result = []
	for i in range(howMany):
		st = file.readline().strip()
		print st
		times = st.split()
		d = getMins(times[0])
		a = getMins(times[1])
		result.append([d, a])
	return result

def getSortedItems(trips, place):
	arrivals = map(lambda x: x[place], trips)
	arrivals.sort()
	return arrivals

def getSortedArrivals(trips):
	return getSortedItems(trips, 1)

def getSortedDepartures(trips):
	return getSortedItems(trips, 0)

def intToTimeStr(total):
	hours = total / 60
	minutes = total % 60
	return "%d:%02d" % (hours, minutes)

def computeNumTrains(arrivals, departures, turn):
	trainsNeeded = 0
	arrivalIndex = 0
	for time in departures:
		if (arrivalIndex < len(arrivals)) and ( \
				arrivals[arrivalIndex] + turn <= time):
			print("train at " + intToTimeStr(time) + \
				" can use train arriving at " + intToTimeStr(\
				arrivals[arrivalIndex]))
			arrivalIndex = arrivalIndex + 1
		else:
			print("need train for train departing at " + intToTimeStr(time))
			trainsNeeded = trainsNeeded + 1

	return trainsNeeded

input = open(sys.argv[1])
out = open("output.txt", "w")

numTestCases = int(input.readline())
for tcNum in range(numTestCases):
	turnaroundTime = int(input.readline())
	print "turnaround: %d" % turnaroundTime
	tripsString = input.readline()
	numAB = int(tripsString.split()[0])
	numBA = int(tripsString.split()[1])
	print "A to B trips"
	abTrips = getTrips(input, numAB)
	print "B to A trips"
	baTrips = getTrips(input, numBA)

	arrivalsAtA = getSortedArrivals(baTrips)
	departuresFromA = getSortedDepartures(abTrips)
	print("Station A:")
	aStart = computeNumTrains(arrivalsAtA, departuresFromA, turnaroundTime)
	
	arrivalsAtB = getSortedArrivals(abTrips)
	departuresFromB = getSortedDepartures(baTrips)
	print("Station B:")
	bStart = computeNumTrains(arrivalsAtB, departuresFromB, turnaroundTime)

	print("Case #" + str(tcNum + 1) + ": " + str(aStart) + " " + \
		str(bStart) + "\n")
	out.write("Case #" + str(tcNum + 1) + ": " + str(aStart) + " " + \
		str(bStart) + "\n")

out.close()
input.close()

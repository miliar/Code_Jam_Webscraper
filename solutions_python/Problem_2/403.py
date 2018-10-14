def parseTime(t):
	times = t.split(':')
	return (int(times[0]), int(times[1]))

def addTime(time, minutes):
	newMinutes = time[1] + minutes
	extraHours = newMinutes/60
	newMinutes = newMinutes % 60
	return (time[0] + extraHours, newMinutes)

def maxLessThan(l, x):
	max = (-1,0)
	for y in l:
		if y <= x and y > max:
			max = y
	return max

def handleCase(turnaround):
	Atrains = 0
	Btrains = 0
	Adepartures = []
	Bdepartures = []
	Aarrivals = []
	Barrivals = []
	trips = raw_input().split()
	Ac = int(trips[0])
	Bc = int(trips[1])
	for i in range(0, Ac):
		trip = tuple([parseTime(x) for x in raw_input().split()])
		Adepartures += [trip[0]]
		Barrivals += [addTime(trip[1], turnaround)]
	for j in range(0, Bc):
		trip = tuple([parseTime(x) for x in raw_input().split()])
		Bdepartures += [trip[0]]
		Aarrivals += [addTime(trip[1], turnaround)]
	Aarrivals.sort()
	Barrivals.sort()
	for departure in Adepartures:
		arrival = maxLessThan(Aarrivals, departure)
		if arrival == (-1,0):
			Atrains += 1
		else:
			Aarrivals.remove(arrival)
	for departure in Bdepartures:
		arrival = maxLessThan(Barrivals, departure)
		if arrival == (-1,0):
			Btrains += 1
		else:
			Barrivals.remove(arrival)
	return (Atrains, Btrains)

cases = input()
for i in range(1, cases+1):
	trains = handleCase(input())
	print "Case #%d: %d %d" % (i, trains[0], trains[1])

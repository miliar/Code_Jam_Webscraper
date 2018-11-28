#!/usr/bin/env python
from sys import argv
mktime = lambda s: tuple(map(lambda x: int(x), s.split(':')))
mintotime = lambda m: (m / 60, m % 60)
timetomin = lambda (x,y): 60*x + y
arrivals = lambda X: map(lambda i: i[1], X)
departures = lambda X: map(lambda i: i[0], X)
opp = lambda s: s == 'B' and 'A' or 'B'
fmttime = lambda m: ':'.join(map(lambda x: str(x), mintotime(m)))

f = open(argv[1])
N = int(f.readline())

def possible(L, dtime, journey):

	arriving = filter(lambda x: x[2] == opp(journey[2]), L)
	zz = filter(lambda i: i[0] >= dtime, arriving)
	if zz == []: return zz
	jj = zz[departures(zz).index(min(departures(zz)))]
	return jj
	

for i in range(N):
	T = int(f.readline()) # turnaround time (minutes)
	NA, NB = map(lambda x: int(x), f.readline().split(' '))
	L = []
	for j in range(NA):
		departure, arrival = f.readline()[:-1].split(' ')
		L.append((timetomin(mktime(departure)), timetomin(mktime(arrival)), 'A'))
	for j in range(NB):
		departure, arrival = f.readline()[:-1].split(' ')
		L.append((timetomin(mktime(departure)), timetomin(mktime(arrival)), 'B'))
	t = {}
	t['A'] = t['B'] = 0
	while len(L) > 0:
		minimum = min(departures(L))
		journey = L[departures(L).index(minimum)]
		dtime = journey[1] + T
		t[journey[2]] += 1
		L.remove(journey)
		while possible(L, dtime, journey):
			old_journey = journey[:]
			journey = possible(L, dtime, journey)
			dtime = journey[1] + T
			L.remove(journey)
	print "Case #%d: %d %d" % (i+1, t['A'], t['B'])
	

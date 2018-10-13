# coding: utf8
# rozwiązanie ?
import sys
from heapq import heappush, heappop

def simulate(ab, ba, T):
	events	= []
	for d, a in ab:
		heappush(events, (d, "d", "A"))
		heappush(events, (a, "a", "B"))
	for d, a in ba:
		heappush(events, (d, "d", "B"))
		heappush(events, (a, "a", "A"))

	locos	= dict(
		A	= 0,
		B	= 0,
	)
	L	= dict(
		A	= 0,
		B	= 0,
	)
	while events:
		time, action, place = heappop(events)
#		print time, action, place
		if action == "d":	# departure
			if locos[place] == 0:
				L[place] += 1
			else:
				locos[place] -= 1
		elif action == "a":
			heappush(events, (time + T, "_", place))	# manouvering
		elif action == "_":
			locos[place] += 1
	return L["A"], L["B"]

def time_parse(time):
	h, m = [int(x) for x in time.split(":")]
	return h * 100 + m

if len(sys.argv) > 1:
	f_name = sys.argv[1]
else:
	f_name = "tt.in"

f = open(f_name)
N = int(f.readline())

for i in xrange(N):
	T	= int(f.readline())
	NA, NB	= [int(x) for x in f.readline().split()]
	ab	= []
	for j in xrange(NA):
		dt, at	= [time_parse(x) for x in f.readline().split()]
		ab.append((dt, at))

	ba	= []
	for j in xrange(NB):
		dt, at	= [time_parse(x) for x in f.readline().split()]
		ba.append((dt, at))

	LA, LB = simulate(ab, ba, T)
	print "Case #%d: %d %d" % (i + 1, LA, LB)


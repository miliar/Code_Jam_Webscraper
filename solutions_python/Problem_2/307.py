#!/usr/bin/env python

#!/usr/bin/env python

import sys;

def solve (li, T):
	# sort departure time (ordered events)
	li.sort(lambda x, y: cmp(x[0],y[0]));

	(no, que) = ([0, 0], [[], []]);
	for trip in li:
		(dep, ari, sta) = trip;
		train = 0;
		if que[sta] and que[sta][0] <= dep:
			train = 1;
			que[sta] = que[sta][1:];
		if 0 == train:
			# NA, buy one :)
			no[sta] += 1;
		# available now, move it
		staNew = 1 & (sta + 1);
		que[staNew].append(ari + T);
		que[staNew].sort();

	return no;

def toMin (str):
	(HH, MM) = str.split(':');
	return int(HH) * 60 + int(MM);

####

#sys.stdin = open("B-small-attempt0.in");
(STATION_A, STATION_B) = (0, 1);
lines = sys.stdin.readlines();
it = iter(lines);

cmax = int(it.next().rstrip());
cidx = 1;
while cidx <= cmax:
	T = int(it.next().rstrip());
	(NA, NB) = [int(a) for a in it.next().rstrip().split()];
	li = [];
	while NA:
		NA -= 1;
		trip = it.next().rstrip().split();
		trip.append(STATION_A);
		li.append(trip);
	while NB:
		NB -= 1;
		trip = it.next().rstrip().split();
		trip.append(STATION_B);
		li.append(trip);
	# convert HH:MM to int(MMMM)
	for t in li:
		t[0] = toMin(t[0]);
		t[1] = toMin(t[1]);

	(ano, bno) = solve(li, T);
	print "Case #%d: %d %d" % (cidx, ano, bno);
	cidx += 1;

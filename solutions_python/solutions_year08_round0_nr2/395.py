#!/usr/bin/env python
import sys

def solve(t, na, nb, trains):
	e = []
	for i in range(na + nb):
		trip = trains[i]
		s = i >= na
		e.append((int(s), False, int(trip[0:2]) * 60 + int(trip[3:5])))
		e.append((int(not s), True, int(trip[6:8]) * 60 + int(trip[9:11]) + t))
	
	key = lambda x: int(x[1])
	e.sort(key=key, reverse=True)
	key = lambda x: x[2]
	e.sort(key=key)
	nt = [0, 0]
	ct = [0, 0]
	for sta, arr, time in e:
		if not arr and ct[sta] == 0:
			nt[sta] += 1
			ct[sta] += 1
		if arr:
			ct[sta] += 1
		else:
			ct[sta] -= 1
	return "%i %i" % (nt[0], nt[1])

def main():
	f = sys.stdin

	n = int(f.readline().strip())
	for i in range(n):
		t = int(f.readline().strip())
		na, nb = [int(x) for x in f.readline().strip().split(" ")]
		trains = []
		for j in (na, nb):
			for k in range(j):
				trains.append(f.readline().strip())
		print "Case #%i: %s" % (i + 1, solve(t, na, nb, trains))

if __name__ == "__main__":
	main()

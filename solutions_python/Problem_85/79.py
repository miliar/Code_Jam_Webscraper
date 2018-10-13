#!/usr/bin/python

T = int(raw_input())
for test in xrange(T):
	line = raw_input().split()
	L, t, n, c = map(int, line[:4])
	a = map(int, line[4:])
	d = a * (n / c  + 1)
	d = d[:n]
	ans = 10**9
	for i in xrange(n):
		time = 0
		boost = 0 
		second = None
		for j in xrange(n):
			win = 0
			if j == i:
				if time > t:
					win = d[i]
				else:
					win = max([0, (time + 2*d[i] - t)/2])
				if (time - t) % 2 == 1:
					print "DUCK"

			pwin = 0
			if time > t:
				pwin = d[j]
			else:
				pwin = max([0, (time + 2*d[j] - t)/2])
				if (time - t) % 2 == 1:
					print "DUCK"

			if j > i and pwin > boost:
				boost = pwin
				second = j

			if L < 1:
				win = 0

			time += 2*d[j] - win

		if L < 2:
			boost = 0
		ans = min([ans, time - boost])
		#print i, second, time - boost

	print "Case #%d: %d" % (test + 1, ans)

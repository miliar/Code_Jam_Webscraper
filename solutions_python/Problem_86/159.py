# Python 2.7

import sys

for i in xrange(0, int(sys.stdin.readline())):
	[players, lowest, highest] = list(map(int, sys.stdin.readline().split(" ")))
	f = list(map(int, sys.stdin.readline().split(" ")))
	t = True
	for j in xrange(lowest, highest + 1):
		t = True
		for k in f:
			if k % j and j % k:
				t = False
		if t:
			print "Case #" + str(i + 1) + ": " + str(j)
			break
	if not t:
		print "Case #" + str(i + 1) + ": NO"

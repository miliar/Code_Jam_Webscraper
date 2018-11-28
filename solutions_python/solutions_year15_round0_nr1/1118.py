#!/usr/bin/env python


for i in range(int(raw_input())):
	print 'Case #{}:'.format(i + 1),
	smax, S = raw_input().split()
	smax = int(smax)
	additional = 0
	total = 0
	for i, si in enumerate(S):
		si = int(si)
		ds = i - total
		if ds > 0:
			additional += ds
			total += ds
		total += si
	print additional
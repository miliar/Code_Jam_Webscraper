#!/usr/bin/env python

def ans(line):
	target = 'welcome to code jam'
	tracks = [0 for i in xrange(len(target))]

	for c in line:
		for i in xrange(1, len(target)):
			if target[i] == c:
				tracks[i] += tracks[i-1]

		if target.startswith(c):
			tracks[0] += 1

	return tracks[-1]

with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		N = int(fin.readline().strip())
		for case in xrange(N):
			line = fin.readline().strip()
			print >>fout, 'Case #%d: %s' % (case+1, str(ans(line)+10000)[-4:])

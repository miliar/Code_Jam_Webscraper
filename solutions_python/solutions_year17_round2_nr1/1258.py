#!/usr/bin/env python

def CruiseCtrl(d, horses):
	slowest_time = max(map(lambda ps: (d - ps[0])/ps[1], horses))
	return d/slowest_time

fileOut = open('file.out.txt', 'w')

with open('file.in.txt', 'r') as fileIn:
	for i in xrange(int(fileIn.readline())):
		d, n = map(int, fileIn.readline().strip().split())
		horses = []
		for j in xrange(n):
			horses += map(float, fileIn.readline().strip().split()),
		fileOut.write('Case #{:d}: {:.6f}\n'.format(i + 1, CruiseCtrl(d, horses)))

fileIn.close()
fileOut.close()

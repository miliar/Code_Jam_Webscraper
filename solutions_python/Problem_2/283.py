#!/usr/bin/env python

def time_compare((x1, x2), (y1, y2)):
	if x1 > y1:
		return 1
	elif x1 == y1:
		if x2 > y2:
			return 1
		elif x2 == y2:
			return 0
		else: #x2<y2
			return -1
	else: #x1<y1
		return -1

def time_add((x1, x2), t):
	y2 = x2 + t
	ov = y2 / 60
	y1 = x1 + ov
	y2 = y2 % 60
	return (y1, y2)

import sys

if len(sys.argv) < 2:
	print 'Need Input!'
	sys.exit()

f=open(sys.argv[1],'r')
numcases = int(f.readline())
for i in range(1, numcases+1):
	print "Case #" + str(i) + ": ",
	turnaroundtime = int(f.readline())
	line = f.readline()
	line = line.rstrip()
	line = line.split()
	na = int(line[0])
	nb = int(line[1])
	trains = []
	times = []
	for j in range(0, na+nb):
		line = f.readline()
		line = line.rstrip()
		line = line.split()
		dep = line[0].split(':')
		arr = line[1].split(':')
		d0 = int(dep[0])
		d1 = int(dep[1])
		a0 = int(arr[0])
		a1 = int(arr[1])
		trains.append(((j<na), (d0, d1), time_add((a0, a1), turnaroundtime)))
		times.append((d0, d1))
		times.append(time_add((a0, a1), turnaroundtime))
	d = {}
	for x in times:
		d[x] = x
	times = d.values()

	times.sort(time_compare)

	ta = 0 #Trains starting at A
	tb = 0 #Trains starting at B
	na = 0 #Number of trains currently at A
	nb = 0 #Number of trains currently at B
	for x in times:
		for (atob, d, a) in trains:
			if x == a and atob:
				nb = nb + 1
			if x == a and (not atob):
				na = na + 1
			if x == d and atob:
				na = na - 1
			if x == d and (not atob):
				nb = nb - 1
		#Check if we ran out of trains
		if na < 0:
			ta = ta - na
			na = 0
		if nb < 0:
			tb = tb - nb
			nb = 0
	print str(ta), str(tb)
			

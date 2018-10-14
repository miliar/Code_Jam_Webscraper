#!/usr/bin/env python

import datetime
import sys

import psyco
psyco.full()

def solve():
	file = open(sys.argv[1])
	N = int(file.readline())
	for n in range(N):
		T = int(file.readline())
		tmp = file.readline().strip().split(' ')
		NA = int(tmp[0])
		NB = int(tmp[1])

		nas = read(file, NA)
		nbs = read(file, NB)
			
		nas_initial_count = 0
		nbs_initial_count = 0

		nas_count = 0
		nbs_count = 0
		
		for a in range(60 * 24):
			t = datetime.time(a // 60, a % 60)

			for na in nas:
				if na[0] == t:
					nas_count -= 1

				if addtime(na[1], datetime.time(0, T)) == t:
					nbs_count += 1
			
			for nb in nbs:
				if nb[0] == t:
					nbs_count -= 1

				if addtime(nb[1], datetime.time(0, T)) == t:
					nas_count += 1
					
			if nas_count < 0:
				nas_initial_count += -nas_count
				nas_count = 0

			if nbs_count < 0:
				nbs_initial_count += -nbs_count
				nbs_count = 0

		
		print("Case #%i: %i %i" % (n + 1, nas_initial_count, nbs_initial_count))

def read(file, count):
	r = [ ]

	for c in range(count):
		tmp = file.readline().strip().split(' ')
		tmp1 = tmp[0].split(':')
		tmp2 = tmp[1].split(':')
		r.append((datetime.time(int(tmp1[0]), int(tmp1[1])), datetime.time(int(tmp2[0]), int(tmp2[1]))))

	return r

def addtime(time1, time2):
	resminute = time1.minute + time2.minute
	reshour = time1.hour + time2.hour
	
	if resminute >= 60:
		reshour += 1
	
	return datetime.time(reshour, resminute % 60)


solve()
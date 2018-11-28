#!/usr/bin/python

import sys

def readdata():
	def rl():
		return sys.stdin.readline().strip().split(' ')
	def hm2m(str):
		h,m = (int(x) for x in str.split(':'))
		return h*60+m
	n = int(rl()[0])
	cases = []
	for i in range(n):
		t = int(rl()[0])
		na, nb = (int(x) for x in rl())
		sa = []
		for j in range(na):
			sa.append([hm2m(x) for x in rl()])
		sb = []
		for j in range(nb):
			sb.append([hm2m(x) for x in rl()])
		case = (t,sa,sb)
		cases.append(case)
	return cases

case_number = 1
for case in readdata():
	turnaround = case[0]
	needed = [0,0]
	trains = [[],[]]
	all_trains = []
	for train in case[1]:
		all_trains.append((0,train[0],train[1]))
	for train in case[2]:
		all_trains.append((1,train[0],train[1]))
	all_trains.sort(key=lambda t: t[1])
	for schedule in all_trains:
		from_station = schedule[0]
		found = False
		for t in trains[from_station]:
			if t <= schedule[1]:
				trains[from_station].remove(t)
				found = True
				break
		if not found:
			needed[from_station] += 1
		trains[1-from_station].append(schedule[2] + turnaround)
	print 'Case #' + str(case_number) + ':',needed[0],needed[1]
	case_number += 1

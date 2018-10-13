#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys


def calcRideGroups(k, g):
	ridegroups = 0
	tmpk = k
	for group in g:
		tmpk-=group
		ridegroups+=1
		if tmpk < 0:
			return ridegroups - 1
	return ridegroups


def calcRideMoney(g, gnum):
	money = 0
	for gidx in range(gnum):
		money += g[gidx]
	return money

def calcMoney(R, k, N, g):
	money = 0
	for round in range(R):
		gnum = calcRideGroups(k, g)
		money += calcRideMoney(g, gnum)
		g = g + g[:gnum]
		del g[:gnum]
	return money


casenum = int(sys.stdin.readline().rstrip())

for i in range(casenum):
	line1 = sys.stdin.readline()
	linedata = line1.rstrip().split()
	R = int(linedata[0])
	k = int(linedata[1])
	N = int(linedata[2])
	line2 = sys.stdin.readline()
	linedata2 = line2.rstrip().split()
	g = []
	for mem in linedata2:
		g.append(int(mem))
	print "Case #" + str(i+1) + ": " + str(calcMoney(R, k, N, g))


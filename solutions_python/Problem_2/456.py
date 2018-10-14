#! /usr/bin/env python
# -*- coding: utf8 -*-

def timetoint(num):
	num = str(num)
	lenght = len(num)
	if int(num[-2:]) == 60:
		return int(str(int(num[:-2])+1)+"00")
	elif int(num[-2:]) > 60:
		if (int(num[-2:]) - 60) < 10:
			return int(str(int(num[:-2])+1) + "0" + str(int(num[-2:])-60))
		else:
			return int(str(int(num[:-2])+1)+str(int(num[-2:])-60))
	else:
		return int(num)

N = int(raw_input())
i = 0

while i < N:
	T = int(raw_input())

	NAB = raw_input()
	NAB = NAB.split(" ")
	NA, NB = int(NAB[0]), int(NAB[1])
	
	departureA = []
	arrivalA = []
	j = 0
	while j < NA:
		x = raw_input()
		x = x.split(" ")
		x[0] = x[0].split(":")
		x[1] = x[1].split(":")
		
		departureA.append((int(x[0][0] + x[0][1])))
		arrivalA.append((int(x[1][0] + x[1][1])))
		
		j = j + 1
		
	departureB = []
	arrivalB = []
	j = 0
	while j < NB:
		x = raw_input()
		x = x.split(" ")
		x[0] = x[0].split(":")
		x[1] = x[1].split(":")
		
		departureB.append((int(x[0][0] + x[0][1])))
		arrivalB.append((int(x[1][0] + x[1][1])))
		
		j = j + 1
		
	departureA.sort()
	departureB.sort()
	arrivalA.sort()
	arrivalB.sort()
	
	stationA = 0 # number of trains starting in A 
	stationB = 0 # number of trains starting in B
	
	for dep in departureA:
		if len(arrivalB) != 0 and timetoint(arrivalB[0] + T) <= dep:
			arrivalB.remove(arrivalB[0])
		else:
			stationA += 1
			
	for dep in departureB:
		if len(arrivalA) != 0 and timetoint(arrivalA[0] + T) <= dep:
			arrivalA.remove(arrivalA[0])
		else:
			stationB += 1

	print "Case #" + str(i+1) + ": " + str(stationA) + " " + str(stationB)

	i = i + 1

#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputf = open('C-small-attempt0.in','r')
outputf = open('C-small-attempt0.out','w')
lineNumber = inputf.readline()

for i in range(int(lineNumber)):
	coasterData = inputf.readline().split(' ')
	popleQueue = inputf.readline().split(' ')
	if(int(coasterData[2]) != len(popleQueue)):
		print 'inputDataError'
		break;
	proceeds = 0
	for j in range(int(coasterData[0])):
		seatBalance = int(coasterData[1])
		waitNum = len(popleQueue)
		for k in range(waitNum):
			room = int(popleQueue[0])
			if (seatBalance < room):
				break;
			popleQueue.pop(0)
			proceeds = proceeds + room
			seatBalance = seatBalance - room
			popleQueue.append(room)
	outputf.write('Case #%d: %d\n'%(i+1,proceeds))

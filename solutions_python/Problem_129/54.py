#! /Library/Frameworks/Python.framework/Versions/Current/bin/python

from collections import deque

modN = 1000002013

T = int(raw_input())

for t in range(1,T+1):

	realCost = 0

	inpArr = raw_input().split()
	N = int(inpArr[0])
	M = int(inpArr[1])

	eventList = []

	for m in range(M):
		inpArr = raw_input().split()
		o = int(inpArr[0])
		e = int(inpArr[1])
		p = int(inpArr[2])
		d = e - o

		realCost += p*(2*N + 1 - d)*d/2
		eventList += [[o,0,p],[e,1,p]]

	sEventList = sorted(eventList)

	cardQueue = deque([])
	optCost = 0

	for evt in sEventList:
		if evt[1] == 0:
			cardQueue.append([evt[0],evt[2]])
		else:
			toPop = evt[2]
			e = evt[0]
			while toPop > 0:
				lastEntry = cardQueue.pop()
				d = e - lastEntry[0]
				if toPop < lastEntry[1]:
					optCost += toPop*(2*N + 1 - d)*d/2
					cardQueue.append([lastEntry[0],lastEntry[1] - toPop])
					toPop = 0
				else:
					optCost += lastEntry[1]*(2*N + 1 - d)*d/2
					toPop -= lastEntry[1]

	print 'Case #'+str(t)+': '+str(realCost - optCost)
#!/usr/bin/python
# dirty and inefficient solution, this is a rush
import sys
T = int(sys.stdin.readline().strip())
for t in range(1, T + 1):
	cost, gain, goal = (float(x) for x in sys.stdin.readline().strip().split())
	
	CpS = 2.0
	lastTime = goal / CpS	
	nbFarms = 0
	calcTime = lastTime
	costFarm = cost / CpS
	farmsTotalCost = 0
	while calcTime <= lastTime:
		lastTime = calcTime
		nbFarms += 1
		farmsTotalCost += costFarm
		CpS += gain		
		costFarm = cost / CpS
		calcTime = farmsTotalCost + goal / CpS
		
	resp = lastTime
	print "Case #{t}: {resp:.7f}".format(t=t, resp=resp)
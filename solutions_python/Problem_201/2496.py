#!/usr/bin/python

import sys
import array
import queue

f = open(sys.argv[1],'r')
t = int(f.readline())

def getLR(number):
	if (number % 2 == 0):
		half = number/2
		return half, half-1
	half = (number-1)/2
	return half, half

for case in range(t):
	n, k = f.readline().split()
	n = int(n)
	k = int(k)
	stalls = queue.PriorityQueue()
	stalls.put(-n)
	L, R = 0, 0
	for i in range(k):
		block = stalls.get()
		L, R = getLR(-block)
		stalls.put(-L)
		stalls.put(-R)	
	print ("Case #" + str(case+1) + ": " + str(int(L)) + " " + str(int(R)))
	







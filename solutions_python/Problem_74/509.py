#!/usr/bin/python

import sys

f = open("bot.in","rb")
t = int(f.readline())

def index(s):
	if (s == "O"):
		return 0;
	else:
		return 1;

for i in range(t):
	
	pos = [1,1]
	wait = [0,0]
	time = 0
	s = f.readline().split()
	n = int(s.pop(0))
	while (len(s)>0):
		rob = index(s.pop(0))
		but = int(s.pop(0))
		travel = abs(but - pos[rob])
		if (travel <= wait[rob]):
			plus = 0
		else:
			plus = travel - wait[rob]
		time = time + plus + 1
		wait[rob] = 0
		wait[1-rob] = wait[1-rob]+plus+1
		pos[rob] = but
	print "Case #{0:d}: {1:d}".format(i+1,time)

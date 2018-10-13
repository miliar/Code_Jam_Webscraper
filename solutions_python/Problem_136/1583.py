#!/usr/bin/env python3
import sys
argc = len(sys.argv)
filename = sys.argv[1]
if argc > 2:
	casenumbers = list(map(int, sys.argv[2:]))
file = open(filename)
T = int(file.readline().rstrip())
for case in range(1,T+1):
	C, F, X = map(float, file.readline().rstrip().split())
	if argc > 2 and not(case in casenumbers):
		continue
	time = 0
	cookiespersecond = 2
	while True:
		wait = time + (X / cookiespersecond)
		farm = time + (C / cookiespersecond) + (X / (cookiespersecond + F))
		if farm < wait:
			time += (C / cookiespersecond)
			cookiespersecond += F
		else:
			time = wait
			break
	print ("Case #", case, ": ", sep="", end="")
	print("{:.7f}".format(time))

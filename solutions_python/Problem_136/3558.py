#!/usr/bin/env python

import os, sys, getopt

sys.setrecursionlimit(5000)
minimum = 999999999999
C = 0
F = 0
X = 0
def recursion(time, persec, farms):
	global minimum
	time_to_next = C/persec
	time_to_win = X/persec
	if minimum > time_to_win + time:
	        minimum = time_to_win + time
	goon = 999999999999
	if farms >= X:
		return time_to_win + time
	if time + time_to_next < minimum:
		goon = recursion(time+time_to_next, persec+F,farms+1)		
	if goon < time + time_to_win:
		if minimum > goon:
			minimum = goon
		return goon
	else:
                return time_to_win + time        	

if __name__ == '__main__': #if we run the program from command line

	file = open('in.in')

	string = file.readline()
	total_number = int(string)
	for i in range(0, total_number):
		info = file.readline().strip().split(" ")
		C = float(info[0])
		F = float(info[1])
		X = float(info[2])
		minimum = 9999999999
		#for 
		#time_to_win = X/persec
	        #if minimum > time_to_win + time:
        	 #       minimum = time_to_win + time
		

		print "Case #%d: %.7f" % (i+1,recursion(0,2,0))


#!/usr/bin/python

#
# Google CodeJam 2011
# Qualification Round
# Problem A: Bot Trust
# Author: dvolgyes
#

import sys
import os

CASES=int(sys.stdin.readline())
for case in range(0,CASES):
	input=sys.stdin.readline().strip()
	vect=list(input.split(" "))
	pos={"O":1,"B":1}
	time={"O":0,"B":0}
	full=0
	for j in range(0,(len(vect)-1)/2):
			curPos=int(vect[j*2+2])
			curRobot=vect[j*2+1]
			delta=abs(curPos-pos[curRobot])
			if (delta>full-time[curRobot]):
				full=full+(delta)-(full-time[curRobot])
			full=full+1
			pos[curRobot]=curPos
			time[curRobot]=full
	print("Case #%s: %s" % (case+1,full))

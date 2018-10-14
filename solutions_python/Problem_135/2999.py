#!/bin/bash
import numpy as np

T = int(raw_input())

for i in xrange(T):
	gr1 = int(raw_input())-1 # guess row 1
	t1 = [[int(c) for c in raw_input().split(" ")] for r in xrange(4)]
	gr2 = int(raw_input())-1 # guess row 2
	t2 = [[int(c) for c in raw_input().split(" ")] for r in xrange(4)]
	intersection = list(np.intersect1d(t1[gr1],t2[gr2]))
	if len(intersection) < 1:
		intersection = [None]
	print("Case #%d: %s" % (i+1, 
		{
			True:str(intersection[0]),
			False:{
				True:"Bad magician!",
				False:"Volunteer cheated!"
			}[len(intersection)>1]
		}[intersection[0] != None and len(intersection) == 1]
		))

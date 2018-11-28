#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sys.stdout.flush()
		n = int(input())
		mushrooms = [m for m in map(int, input().split(' '))]

		first = 0
		second_speed = 0
		for i in range(1, len(mushrooms)):
			first = first + max(0, mushrooms[i-1]-mushrooms[i])
			second_speed = max(second_speed, max(0, mushrooms[i-1]-mushrooms[i]))
		second = 0
		for i in range(0, len(mushrooms)-1):
			second = second + min(second_speed, mushrooms[i])

		print("Case #%d: %d %d" % (caseIdx, first, second))

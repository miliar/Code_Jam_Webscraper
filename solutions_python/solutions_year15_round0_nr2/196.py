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
		d = int(input())
		pancakes = [p for p in map(int, input().split(' '))]

		ans = max(pancakes)
		for i in range(1, max(pancakes)+1):
			if i > ans:
				break
			accu_minutes = i
			for p in pancakes:
				accu_minutes = accu_minutes + math.ceil(p/i)-1
			ans = min(ans, accu_minutes)
		print("Case #%d: %d" % (caseIdx, ans))

#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

T = int(raw_input())

for caseNo in range(T):
	(C,F,X) = map(float, raw_input().split(" "))
	CPS = 2
	currentTime = 0
	currentCookie = 0

	minTime = X / CPS

	while(True):
		currentTime += C / CPS
		CPS += F
		reachTime = currentTime + X / CPS
		if(reachTime < minTime):
			minTime = reachTime
		else:
			break

	print("Case #" + str(caseNo + 1) + ": " + str(minTime))

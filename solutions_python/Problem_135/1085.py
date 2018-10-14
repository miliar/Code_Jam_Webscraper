#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

T = int(raw_input())

for caseNo in range(T):
	firstChoice = int(raw_input()) - 1
	firstRows = {}
	for i in range(4):
		firstRows[i] = map(int, raw_input().split(" "))
	secondChoice = int(raw_input()) - 1
	secondRows = {}
	for i in range(4):
		secondRows[i] = map(int, raw_input().split(" "))
	
	candidate = []
	for x in firstRows[firstChoice]:
		if(x in secondRows[secondChoice]):
			candidate.append(x)

	if(len(candidate) == 0):
		ansStr = "Volunteer cheated!"
	elif(len(candidate) == 1):
		ansStr = str(candidate[0])
	else:
		ansStr = "Bad magician!"

	print("Case #" + str(caseNo + 1) + ": " + ansStr)

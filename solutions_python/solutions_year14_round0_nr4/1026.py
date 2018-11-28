#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from copy import deepcopy

T = int(raw_input())

for caseNo in range(T):
	N = int(raw_input())
	w = []
	w.append(map(float, raw_input().split(" ")))
	w.append(map(float, raw_input().split(" ")))
	wall = w[0][:]; wall.extend(w[1])
	wall.sort()
	wall.reverse()
	widx = [[0 for i in range(N)] for j in range(2)]
	for x in range(2):
		for y in range(N):
			widx[x][y] = wall.index(w[x][y])
	widx[0].sort()
	widx[1].sort()

	# smaller index is stronger!

	dwarpoint = 0
	widxbk = deepcopy(widx)
	while(len(widx[0]) != 0):
		c = 0
		# using weakest
		while(len(widx[0]) != 0):
			Nweakest = widx[0][-1]
			Kweakest = widx[1][-1]
			if(Nweakest > Kweakest):
				c = 1
				del widx[0][-1]
				del widx[1][0]
			else:
				break
		# kill if possible
		while(len(widx[0])!= 0):
			Kstrongest = widx[1][0]
			for Ncand in reversed(widx[0]):
				if(Ncand < Kstrongest):
					c = 1
					dwarpoint += 1
					del widx[0][widx[0].index(Ncand)]
					del widx[1][0]
					continue
			break
		if(len(widx[0]) != 0 and c == 0):
			Nweakest = widx[0][-1]
			Kweakest = widx[1][-1]
			if(Nweakest < Kweakest):
				del widx[0][-1]
				del widx[1][0]

			
			

	widx = widxbk
	
	warpoint = -1
	while(warpoint == -1):
		N = widx[0].pop()
		K = -1
		for Kcand in reversed(widx[1]):
			if(Kcand < N):
				K = Kcand
				break
		if(K == -1):
			# cannot konquer!
			warpoint = len(widx[0]) + 1
		else:
			del widx[1][widx[1].index(K)]
			if(len(widx[0]) == 0):
				warpoint = 0
				break

	print("Case #" + str(caseNo + 1) + ": " + str(dwarpoint) + " " + str(warpoint))



# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/env python
import sys
import random
import numpy as np
from time import time
import math


def color(x):
	if x == 0:
		return "R"
	if x == 1:
		return "O"
	if x == 2:
		return "Y"
	if x == 3:
		return "G"
	if x == 4:
		return "B"
	if x == 5:
		return "V"

def repair(colors,N):
	if colors[0] != colors[N-1]:
		return colors
	tofix = list(colors)
	temp = tofix[N-2]
	tofix[N-2] = tofix[N-1]
	tofix[N-1] = temp
	currIndex = N-2
	while currIndex > 1 and tofix[currIndex] == tofix[currIndex-1]:
		temp = tofix[currIndex-2]
		tofix[currIndex-2] = tofix[currIndex-1]
		tofix[currIndex-1] = temp
		currIndex = currIndex-2
	fixedFlag = True
	for i in range(N-1):
		if tofix[i] == tofix[i+1]:
			fixedFlag = False
	if tofix[0] == tofix[N-1]:
		fixedFlag = False
	if fixedFlag == True:
		return(''.join(tofix))
	else:
		return("IMPOSSIBLE")



T = int(raw_input().strip())
for n in range(T):
	case = list(map(int,raw_input().strip().split(' ')))
	N = case[0]
	toPlace = case[1:]
	prevColor = -1
	output = ""
	badFlag = False
	for i in range(6):
		if toPlace[i] > N/2:
			badFlag = True
	if badFlag == False:
		for i in range(N):
			maxIndex = -1
			for k in range(6):
				if k != prevColor:
					if maxIndex < 0:
						maxIndex = k

					elif toPlace[k] > toPlace[maxIndex]:
						maxIndex = k
			output = output + color(maxIndex)
			toPlace[maxIndex] -= 1
			prevColor = maxIndex

		output = repair(str(output),N)
		print("Case #" + str(n+1) + ": " + str(output))
	else:
		print("Case #" + str(n+1) + ": IMPOSSIBLE")
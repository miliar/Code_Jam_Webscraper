#! python3

from os import system

import sys
sys.stdout = open("B-small-attempt0-output.txt", "w")

f = open("B-small-attempt0.in", "r")
input = f.read().strip()

input = input.split('\n')
del input[0]

for lineKey, line in enumerate(input):
	total = 0
	lineInfo = line.split(' ')
	for i in range(int(lineInfo[0])):
		for j in range(int(lineInfo[1])):
			if i & j < int(lineInfo[2]):
				total += 1
	print("Case #" + str(lineKey + 1) + ": " + str(total))
	
system("pause")

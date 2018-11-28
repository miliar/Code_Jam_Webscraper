#!/usr/bin/env python3

# Google Code Jam 2010
# Qualification Round
# C. Theme Park

# This is fairly simple, we have a pos variable, which is a pointer to the
# current position of the queue. There is a startpos variable, which we use
# to not have more groups in the rollercoaster than in the queue. Then we just
# check if the next group fits into the rollercoaster, and when they do, we
# increment the position and the income by appropriate ammount. At the end we
# print out the total income.

import sys

def solvecase(t):
	print("Case #" + str(t) + ": ", end="")
	# Read the firs line with R, k and N
	line = sys.stdin.readline().split()
	# The roller coaster will run R times in a day.
	R = int(line[0])
	# The roller coaster can hold k people at once.
	k = int(line[1])
	# N groups in line:
	N = int(line[2])
	# Read the second line with g[i], the size of the groups
	g = sys.stdin.readline().split()
	# Convert g[i] to integers from strings:
	for pos in range(0, N):
		g[pos] = int(g[pos])
	# Position in the queue, we start at the beginning:
	pos = 0
	# How much money is in the register:
	income = 0
	for r in range(1, R+1):
		# starting position in the queue:
		startpos = pos
		# seats taken:
		seats = 0
		while seats + g[pos] <= k:
			seats += g[pos]
			pos += 1
			if pos == N:
				# The position loops to 0
				pos = 0
			if pos == startpos:
				# All the groups are in the rollercoaster:
				break
		income += seats
	print(income)

# Number of cases
T = int(sys.stdin.readline())

for t in range(1, T+1):
	solvecase(t) 


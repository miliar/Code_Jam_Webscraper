#!/usr/bin/env python3

# qualification round, exercize 1
# 16 cards in square (4x4), 1 number per card (1 to 16)
# the number is shown
# pick a card and tell the row
# re-arrange in 4x4 square, the volunteer pick the row of its card
# the mage will get the right card. How?

# program gives two arrangements of the card and volunteer answer
# rows are given 1 to 4 from top to bottom
# The program should determine the card, if there are multiple choices or if
# the volunteer is not consistent

import sys

def readCase():
	A = int(sys.stdin.readline().strip()) - 1
	lines = []
	for l in range(4):
		lines.append([int(x) for x in sys.stdin.readline().strip().split()])
	return A, lines

# First line the number of test cases T
T = int(sys.stdin.readline())

for t in range(T):
	A1, L1 = readCase()
	A2, L2 = readCase()
	
	l1 = set(L1[A1])
	l2 = set(L2[A2])
	
	i = list(l1.intersection(l2))
	if len(i) == 1:
		print("Case #{}: {}".format(t + 1, i[0]))
	elif len(i) == 0:
		print("Case #{}: Volunteer cheated!".format(t + 1))
	elif len(i) > 1:
		print("Case #{}: Bad magician!".format(t + 1))

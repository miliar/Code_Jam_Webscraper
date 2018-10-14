#!/usr/bin/env python3

# These are my first programs in python, so please bear with me.
# We are going to do a recursive search on the flow path.
# We start at 0,0 (nort-westernmost corner), and ask what label should we give
# to this location. If the location doesn't have a label yet, then store the
# next available label.
# Next we calculate in which way the water would flow, and ask recursively
# what label should we give to that location, and set our label to be the same
# and we also return this label to our caller. If there is no way for the
# water to flow, we are a sink, so we set our label as the next available, and
# we also return the value to our caller.
# In the previous version I really messed up the x and y coordinates.

import sys

# An array to hold the available basins labels:
labels = []
for i in range(26):
	labels.append(chr(ord('a') + i))
# An array to hold the input elevation map:
input = []
# An array to put the results in:
label = []

def lower(x, y, lowest):
	if x>=0 and y>=0 and x<W and y<H and lowest > input[x][y]:
		return True
	else:
		return False

def findlowestneighbor(x,y):
	nx = None
	ny = None
	lowest = input[x][y]
	# North
	if lower(x, y-1, lowest):
		nx = x
		ny = y-1
		lowest = input[x][y-1]
	# West
	if lower(x-1, y, lowest):
		nx = x-1
		ny = y
		lowest = input[x-1][y]
	# East
	if lower(x+1, y, lowest):
		nx = x+1
		ny = y
		lowest = input[x+1][y]
	# South
	if lower(x,y+1, lowest):
		nx = x
		ny = y+1
		lowest = input[x][y+1]
	if nx == None:
		return None
	else:
		return [nx, ny]

def labelme(x, y, currlabel):
# If we already have a label, return it
	if label[x][y] != "":
		return label[x][y]
	#label[x][y] = labels[currlabel]
	flowdirection = findlowestneighbor(x,y)
	if flowdirection == None:
		# We are a sink
		label[x][y] = labels[currlabel]
	else:
		label[x][y] = labelme(flowdirection[0], flowdirection[1], currlabel)
	return label[x][y]

def solvecase(t):
	global input
	global label
	global H
	global W
	line = sys.stdin.readline().split()
	H=int(line[0])
	W=int(line[1])
	label = [ [ "" for y in range(H)] for x in range(W) ]
	currlabel = 0
	input = [ [ 0 for y in range(H)] for x in range(W) ]
	for y in range(H):
		line = sys.stdin.readline().split()
		for x in range(W):
			input[x][y] = line[x]

	for y in range(H):
		for x in range(W):
			if labelme(x, y, currlabel) == labels[currlabel]:
				currlabel+=1
	print("Case #" + str(t) + ":")
	for y in range(H):
		for x in range(W):
			print(label[x][y], end="")
			if x < W-1:
				print(" ", end="")
		print()

# Number of maps
T = sys.stdin.readline()

for t in range(1, int(T)+1):
	solvecase(t)


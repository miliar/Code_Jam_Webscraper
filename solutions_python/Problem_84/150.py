#!/usr/bin/env python

# Google Code Jam 2011
# Round 1C
# Jeremy Chin <rekless@gmail.com>
# A. Square Tiles


import math
import sys

# Simple stupid method

f = open(sys.argv[1])

def fill(graph, width):
	if '#' not in graph:
		return graph
	idx = graph.index('#')
	
	x = idx % width
	x1 = x + 1
	y = idx / width
	y1 = y + 1
	if x1 == width or y1 * width + x1 > len(graph):
		return False

	if graph[y * width + x + 1] != '#' or \
		graph[y1 * width + x] != '#' or \
		graph[y1 * width + x1] != '#':
			return False
	graph[y * width + x] = '/'
	graph[y * width + x1] = '\\'
	graph[y1 * width + x] = '\\'
	graph[y1 * width + x1] = '/'
	return fill(graph, width)

f.readline() # number of cases
# for line in f:
line = f.readline()
idx = 1
while line:
	parts = line.split()
	rows = int(parts[0])
	cols = int(parts[1])

	pic = []
	for x in range(0,rows):
		pic += f.readline().strip("\n")
	res = fill(list(pic), cols)
	print "Case #%s:" % idx
	if res == False:
		print "Impossible"
	else:
		for x in range(0, rows):
			print ''.join(res[(x*cols):((x+1)*cols)])

	line = f.readline()

	idx += 1

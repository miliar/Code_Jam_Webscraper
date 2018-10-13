#!/usr/bin/env python

# Tanner Grehawick
# Google Code Jam 2017 Qualification Round
# Problem 1: Oversized Pancake Flipper

from sys import stdin
from collections import deque
import re

data_p = re.compile(r'([\-\+]+)\s*([0-9]+)')

sample_count = stdin.readline().strip()
sample_count = int(sample_count)

# simple breadth first search of state graph
def search_states(istate, fsize):
	unvisited = deque()			# queue of unvisited states
	visited = set()				# set of visited states
	distance = {}					# map of states -> len of shortest path from istate
	unvisited.append(istate)
	distance[istate] = 0
	while len(unvisited) > 0:
		state = unvisited.popleft()
		d = distance[state]
		if state.find("-") == -1:	# if there are no blank pancakes, this is the correct state
			return d
		for n in neighbors(state, fsize):
			if n not in visited:
				distance[n] = d + 1
				visited.add(n)
				unvisited.append(n)
	return "IMPOSSIBLE"

flip_p = re.compile(r'.')
def flip_repl(m):
	if m.group(0) == "+":
		return "-"
	else:
		return "+"

def neighbors(state, fsize):
	for i in xrange((len(state) - fsize) + 1):
		flip = state[i:i+fsize]
		flip = flip_p.sub(flip_repl, flip)
		yield "{}{}{}".format(state[:i], flip, state[i+fsize:])

for s in xrange(sample_count):
	line = stdin.readline().strip()
	m = data_p.match(line)
	if m:
		istate = m.group(1)			# initial state of the pancakes
		fsize = int(m.group(2))		# size of the flipper
		print ("Case #{}: {}".format(s + 1, search_states(istate, fsize)))	
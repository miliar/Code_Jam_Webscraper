#!/usr/bin/env python
from sys import stdin

def reachable(current_pos, current_vine):
	if (current_pos, current_vine) in table:
		return table[(current_pos, current_vine)]
	
	radius = min(vines[current_vine][0] - current_pos, vines[current_vine][1])
	
	if vines[current_vine][0] + radius >= goal:
		table[(current_pos, current_vine)] = True
		return True
	
	for i in xrange(current_vine + 1, len(vines)):
		if vines[i][0] <= vines[current_vine][0] + radius:
			if reachable(vines[current_vine][0], i):
				table[(current_pos, current_vine)] = True
				return True
	
	table[(current_pos, current_vine)] = False
	return False

for T in xrange(1, int(stdin.readline()) + 1):
	n = int(stdin.readline())
	vines = []
	
	# (distance, length)
	for i in xrange(n):
		vines.append(
			tuple(int(x) for x in stdin.readline().strip().split())
		)
	
	goal = int(stdin.readline())
	table = dict()
	reach =  reachable(0, 0)
	
	if reach:
		print "Case #{}: YES".format(T)
	else:
		print "Case #{}: NO".format(T)
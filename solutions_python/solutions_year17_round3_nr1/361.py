import sys
import math
# import numpy as np 
# import networkx as nx
# import heapq
# import collections

INPUT_FILE = 'test.in'
OUTPUT_FILE = 'test.out'

def lv(data):
	return data.readline().rstrip('\n')

def ll(data):
	return lv(data).split(' ')

def lm(data, lines):
	src = []
	for i in range(lines):
		src.append(ll(data))
	return src

def import_file(file):
	with open(file) as data:
		T = int(lv(data))
		tests = []
		for i in range(T):
			(N, K) = [int(x) for x in ll(data)]
			pancakes = []
			for idx in range(N):
				(radii, height) = [float(x) for x in ll(data)]
				pancakes.append((radii, height))
			tests.append((N, K, pancakes))			   
		return (T, tests)

def eval_stack(stk):
	# Top to bottom
	area = 0.0
	previous_area = 0.0
	for pc in stk:
		(rad, hei) = pc
		area += hei * rad * 2 * math.pi 
		area += (rad * rad * math.pi - previous_area)
		previous_area = rad * rad * math.pi
	return area


def solution(T):
	(N, K, pancakes) = T
	height_sorted = sorted(pancakes, key=lambda m : m[0] * m[1])
	
	if K > 1:
		top = height_sorted[-1 * (K - 1):]
		biggest_radius = sorted(top, key = lambda m: m[0])[-1][0]
		bottom = height_sorted[:-1 * (K - 1)]
	else:
		top = []
		bottom = pancakes
		biggest_radius = 0.0

	biggest_bottom = sorted(bottom, key = lambda m: m[0])[-1][0]
	last_cake = sorted(bottom, key=lambda m: max(m[0] * m[0] - biggest_radius * biggest_radius, 0) + 2 * m[0] * m[1])[-1]
	top.append(last_cake)

	return eval_stack(sorted(top, key=lambda m: m[0]))

def solution2(T):
	(N, K, pancakes) = T
	cakes = sorted(pancakes, key=lambda k: k[0] * k[1])[-1 * K:]
	return eval_stack(sorted(cakes, key=lambda m: m[0]))

sys.stdout = open(OUTPUT_FILE, 'w')
(T, test_cases) = import_file(INPUT_FILE)
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ': '), 
	print(solution(test))
	print >> sys.stderr, 'Case #' + str(idx + 1) + ': completed'
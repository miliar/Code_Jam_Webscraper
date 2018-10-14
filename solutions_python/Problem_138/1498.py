#! /usr/bin/env python

from __future__ import print_function
from sys import stdin, stderr
import math


debug = True

def debug_print(s):
	if debug:
		print('    DEBUG: {}'.format(s), file=stderr)


def ken_choose(B_ken, chosen_naomi):
	try:
		chosen_ken = min(filter(lambda x: x > chosen_naomi, B_ken))
	except ValueError:
		chosen_ken = min(B_ken)
	B_ken.remove(chosen_ken)
	return chosen_ken


def solve_d_war(B_naomi, B_ken):
	B_naomi = set(B_naomi)
	B_ken = set(B_ken)
	score_naomi = 0

	while len(B_naomi) > 0:
		chosen_naomi = min(B_naomi)
		min_ken = min(B_ken)
		max_ken = max(B_ken)
		told_naomi = max_ken - 0.0000001 if chosen_naomi < min_ken else max_ken + 0.0000001
		chosen_ken = ken_choose(B_ken, told_naomi)
		B_naomi.remove(chosen_naomi)
		if chosen_naomi > chosen_ken:
			score_naomi += 1

	return score_naomi


def solve_war(B_naomi, B_ken):
	B_naomi = set(B_naomi)
	B_ken = set(B_ken)
	score_naomi = 0

	while len(B_naomi) > 0:
		chosen_naomi = B_naomi.pop()
		chosen_ken = ken_choose(B_ken, chosen_naomi)
		if chosen_naomi > chosen_ken:
			score_naomi += 1

	return score_naomi


if __name__ == '__main__':
	num_cases = int(stdin.readline().strip())

	for case in range(1, num_cases + 1):
		N, = [int(x) for x in stdin.readline().strip().split()]
		B_naomi = [float(x) for x in stdin.readline().strip().split()]
		B_ken = [float(x) for x in stdin.readline().strip().split()]
		debug_print('N: {}, B_naomi: {}, B_ken: {}'.format(N, B_naomi, B_ken))

		y = solve_d_war(B_naomi, B_ken)
		z = solve_war(B_naomi, B_ken)
		print('Case #{}: {} {}'.format(case, y, z))


#!/usr/bin/env python3

from sys import stdin

def f(a, b):
	size_b = len(b)
	i_b = 0
	for chosen_a in a:
		while i_b < size_b and b[i_b] < chosen_a: i_b += 1
		if i_b < size_b: b[i_b] = None
		i_b += 1
	return len([x for x in b if x is not None])
		

cases = int(stdin.readline())

for case in range(1, cases+1):
	N = int(stdin.readline())
	naomi = [float(x) for x in stdin.readline().split()]
	ken = [float(x) for x in stdin.readline().split()]
	naomi.sort()
	ken.sort()
	score_w = f(list(naomi), list(ken))
	score_dw = N - f(list(ken), list(naomi))

	print('Case #%d: %d %d' % (case, score_dw, score_w))



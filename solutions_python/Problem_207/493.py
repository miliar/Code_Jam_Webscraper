#!/usr/bin/env python3

import sys

def check(N, sol):
	if N != len(sol):
		return False
	if sol[0] == sol[-1]:
		return False
	for i in range(N-1):
		if sol[i] == sol[i+1]:
			return False
	return True

def solve(line, t):
	N, R, O, Y, G, B, V = map(int, line.split(' '))
	colors = [[R, 'R'], [Y, 'Y'], [B, 'B']]
	colors.sort()
	#print(colors)
	sol = ""
	
	diff = colors[2][0] - colors[1][0]
	while colors[1][0] > 0:
		sol += colors[2][1] + colors[1][1]
		colors[2][0] -= 1
		colors[1][0] -= 1

	turn = 2 if colors[2][0] > 0 else 0
	while colors[turn][0] > 0:
		sol += colors[turn][1]
		colors[turn][0] -= 1
		turn = 2 - turn

	if colors[2][0] > 0:
		print("Case #%d: IMPOSSIBLE" % (t))
		return

	i = 1
	while colors[0][0] > 0:
		sol = sol[:i] + colors[0][1] + sol[i:]
		i += 2
		colors[0][0] -= 1

	assert(colors[0][0] == 0)
	assert(colors[1][0] == 0)
	assert(colors[2][0] == 0)

	#print("sol: %s" % sol)
	if not check(N, sol):
		print("Case #%d: IMPOSSIBLE" % (t))
		return
	
	print("Case #%d: %s" % (t, str(sol)))


lines = [ l.strip() for l in sys.stdin.readlines() ]

T = int(lines[0])

for i in range(T):
	solve(lines[i+1], i+1)

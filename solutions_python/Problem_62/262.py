#!/usr/bin/env python3

t = int(input())
for x in range(t):
	y = 0
	n = int(input())
	wires = []
	for i in range(n):
		wires.append(tuple(map(int, input().split())))
	wires.sort()
	for i, wire in enumerate(wires):
		a, b = wire
		for j in range(i):
			if wires[j][1] > b:
				y += 1
	print('Case #%d: %d' % (x + 1, y))

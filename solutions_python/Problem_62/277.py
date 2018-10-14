#!/usr/bin/python

T = int(raw_input())
for t in range(0, T):
	N = int(raw_input())
	wires = {}
	cnt = 0
	for n in range(0, N):
		ab = raw_input().split(' ')
		(a, b) = (int(ab[0]), int(ab[1]))
		wires[a] = b
	for key_i in wires.keys():
		for key_j in wires.keys():
			if key_i != key_j and wires[key_i] != wires[key_j]: 
				"""
				if key_i <= key_j and wires[key_i] >= key_j and key_i <= wires[key_j] and wires[key_i] >= wires[key_j]:
					cnt = cnt + 1
				"""
				if key_i > key_j and wires[key_i] < wires[key_j]:
					cnt = cnt + 1
				elif key_i < key_j and wires[key_i] > wires[key_j]:
					cnt = cnt + 1
	print "Case #" + str(t+1) + ": " + str(cnt/2)

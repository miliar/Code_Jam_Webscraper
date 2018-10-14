#!/usr/bin/python
import sys

t = int(sys.stdin.readline())
for c in xrange(1, t+1):
	row = int(sys.stdin.readline())
	for i in range(4):
		inp = [int(x) for x in sys.stdin.readline().split()]
		if i == row-1:
			mem_1 = inp

	row = int(sys.stdin.readline())
	for i in range(4):
		inp = [int(x) for x in sys.stdin.readline().split()]
		if i == row-1:
			mem_2 = inp

	inter = list(set(mem_1) & set(mem_2))

	if len(inter) == 1:
		print "Case #{}: {}".format(c, inter[0])
	elif len(inter) > 1:
		print "Case #{}: {}".format(c, "Bad magician!")
	elif len(inter) == 0:
		print "Case #{}: {}".format(c, "Volunteer cheated!")
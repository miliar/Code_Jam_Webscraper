#! /usr/bin/python

import sys

trials = int(sys.stdin.readline())

for rnd in range(trials):
	ans1 = int(sys.stdin.readline())
	grid1 = []
	for x in range(4):
		line = sys.stdin.readline()
		tmp = [ int(x) for x in line.split(" ") ]
		grid1.append(tmp)
	ans2 = int(sys.stdin.readline())
	grid2 = []
	for x in range(4):
		line = sys.stdin.readline()
		tmp = [ int(x) for x in line.split(" ") ]
		grid2.append(tmp)
	set1 = set(grid1[ans1-1])
	set2 = set(grid2[ans2-1])
	diff = set1.intersection(set2)
	if len(diff) == 1:
		ans = str(diff.pop())
	elif len(diff) == 0:
		ans = "Volunteer cheated!"
	else:
		ans = "Bad magician!"
	print "Case #" + str(rnd + 1) + ": " + str(ans)

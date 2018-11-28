#!/usr/bin/env python

import io

f = open("input.txt")

cases = int(f.readline())

for c in range(cases):
	answer_one = int(f.readline())
	line_one = []
	for i in range(4):
		if (i + 1) == answer_one:
			line_one = [int(n) for n in (f.readline().strip()).split(' ')]
		else:
			f.readline()
	answer_two = int(f.readline())
	line_two = []
	for i in range(4):
		if (i + 1) == answer_two:
			line_two = [int(n) for n in (f.readline().strip()).split(' ')]
		else:
			f.readline()

	set_one = set(line_one)
	set_two = set(line_two)
	inters = set_one.intersection(set_two)	
	
	print "Case #%d:" % (c + 1),
	if (len(inters) == 0):
		print "Volunteer cheated!"
	elif (len(inters) == 1):
		print "%d" % inters.pop()
	else:
		print "Bad magician!"

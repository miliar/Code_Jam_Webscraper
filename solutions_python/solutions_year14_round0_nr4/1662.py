#!/usr/bin/env python


import sys


if sys.stdin.isatty():
	print "No input detected!"
	sys.exit(1)
T = int(sys.stdin.readline())

for case in range(1, T+1):
	N = int(sys.stdin.readline())
	blocks_naomi = sys.stdin.readline().split()
	blocks_ken   = sys.stdin.readline().split()
	blocks_naomi = [float(block) for block in blocks_naomi]
	blocks_ken   = [float(block) for block in blocks_ken]

#	print blocks_naomi
#	print blocks_ken

	blocks_naomi.sort()
	blocks_ken.sort()

	
	dblocks_naomi = blocks_naomi[:]
	dblocks_ken   = blocks_ken[:]
#	print blocks_naomi
#	print blocks_ken

	point_naomi = 0
	point_ken   = 0

	# War
	while len(blocks_naomi):
		chosen_naomi = blocks_naomi.pop()
		chosen_ken   = blocks_ken[0]
		for block in blocks_ken:
			if block > chosen_naomi:
				point_ken +=1
				chosen_ken = block
				blocks_ken.remove(block)
				break
		if chosen_ken < chosen_naomi:
			point_naomi += 1	
			blocks_ken.remove(chosen_ken)


	# Deceitful War
	dpoint_naomi = 0
	dpoint_ken   = 0
	while len(dblocks_naomi):
		got_point = False
		for block in dblocks_naomi:
			if block > dblocks_ken[0]:
				dpoint_naomi += 1
				dblocks_ken.pop(0)
				dblocks_naomi.remove(block)
				got_point = True
				break

		if not got_point:
#			if dblocks_naomi[0] < dblocks_ken[len(dblocks_ken)-1]:
			dpoint_ken += 1
			dblocks_ken.pop()
			dblocks_naomi.pop(0)
		

	print "Case #%d: %d %d" % (case, dpoint_naomi, point_naomi)

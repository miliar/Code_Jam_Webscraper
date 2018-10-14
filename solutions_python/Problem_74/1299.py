#!/usr/bin/python

import sys

numberOfCases = int(sys.stdin.readline()[:-1])

for case in range(numberOfCases):
        list = sys.stdin.readline()[:-1].split(" ")

	seq = {}
	seq['O'] = []
	seq['B'] = []

	order = []
	for i in range(1, len(list), 2):
		item = []
		item.append(list[i])
		item.append(list[i+1])
		order.append(item)
	index = {}
	index['O'] = 1
	index['B'] = 1
	for action in order:
		curr = action[0]
		targetButton = int(action[1])
		if curr == 'O': 
			theOther = 'B'
		else:
			theOther = 'O'

		# move to target button	
		currActions = []
		begin = index[curr]
		if targetButton < begin:
			r_from = begin
			r_to = targetButton-1
			step = -1
		else:
			r_from = begin
			r_to = targetButton+1
			step = 1
		for x in range(r_from, r_to, step):
			if (index[curr] != x):
				currActions.append("%s move %d" % (curr, x))
		currActions.append("%s push %d" % (curr, x))
		index[curr] = x
	
		moveCount = len(currActions) - 1
		buffer = len(seq[theOther]) - len(seq[curr])
		base = moveCount - buffer

		if buffer == 0:
			seq[curr].extend(currActions)
		else:
			if base < 0:
				count = len(seq[theOther]) - len(seq[curr])
				for tmp in range(count):
					seq[curr].extend(".")

				seq[curr].extend(currActions[moveCount:])
			elif base > 0:
				count = len(seq[theOther]) - len(seq[curr])
				for tmp in range(count):
					seq[curr].extend(".")

				if buffer < 0:
					seq[curr].extend(currActions)
				else:
					seq[curr].extend(currActions[buffer:])
			else:
				seq[curr].extend(currActions)

	lenO = len(seq['O'])
	lenB = len(seq['B'])
	if lenO > lenB:
		max = lenO
	else:
		max = lenB	

	print "Case #%d: %d" % (case+1, max)
			



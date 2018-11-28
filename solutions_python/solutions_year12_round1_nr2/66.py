#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())
for case_no in xrange(1, cases + 1):
	levels = int(sys.stdin.readline())
	others = []
	doable = []
	for i in xrange(levels):
		costA, costB = [int(val) for val in sys.stdin.readline().strip().split()]
		if costA == 0 or costB == 0:
			doable.append((costB, costA, 0))
		else:
			others.append((costB, costA, 0))
	cur = 0
	ans = 0
	while len(doable) + len(others) > 0:
		if len(doable) == 0:
			break
		changed = False
		do = []
		ndoable = []
		for case in doable:
			if case[0] <= cur:
				do.append(case)
			else:
				ndoable.append(case)
		if len(do) > 0:
			doable = ndoable
			for case in do:
				cur += 2 - case[2]
				ans += 1
				changed = True
		else:
			next_best = None
			for case in doable:
				if case[2] != 1:
					if case[1] <= cur and (next_best is None or case[0] > next_best[0]):
						next_best = case
			if next_best is not None:
				doable.remove(next_best)
				doable.append((next_best[0], next_best[1], 1))
				cur += 1
				ans += 1
				changed = True
			else:
				break
		todo = []
		nothers = []
		for case in others:
			if case[0] <= cur or case[1] <= cur:
				todo.append(case)
			else:
				nothers.append(case)
		if len(todo) > 0:
			others = nothers
			for case in todo:
				doable.append(case)

	if len(others) + len(doable) > 0:
		print "Case #%d: Too Bad" % case_no
	else:
		print "Case #%d: %d" % (case_no, ans)
	case_no += 1

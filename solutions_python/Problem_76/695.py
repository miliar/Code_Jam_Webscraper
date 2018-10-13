#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())
for case in xrange(1, cases + 1):
	print "Case #%d:" % case,
	sys.stdin.readline()
	nums = [int(n) for n in sys.stdin.readline().strip().split()]
	nums.sort()
	cur_scores = {(0, 0): (0, 0)}
# 	print
	for num in nums:
		next_scores = {}
		for key in cur_scores:
			k_mine = key[0]
			v_mine = cur_scores[key][0]
			k_theirs = key[1]
			v_theirs = cur_scores[key][1]
			# consider giving it to me
			nkey = (k_mine ^ num, k_theirs)
			if nkey in next_scores:
				if v_mine + num > next_scores[nkey][0]:
					next_scores[nkey] = (v_mine + num, v_theirs)
			else:
				next_scores[nkey] = (v_mine + num, v_theirs)
			# consider giving it to them
			nkey = (k_mine, k_theirs ^ num)
			if nkey in next_scores:
				if v_mine > next_scores[nkey][0]:
					next_scores[nkey] = (v_mine, v_theirs + num)
			else:
				next_scores[nkey] = (v_mine, v_theirs + num)
		cur_scores = next_scores
# 		print num
# 		for key in cur_scores:
# 			print key, cur_scores[key]
	max_score = -1
	for key in cur_scores:
# 		print key, cur_scores[key]
		if key[0] == key[1]:
			if max_score < cur_scores[key][0]:
				if cur_scores[key][1] > 0:
					max_score = cur_scores[key][0]
	if max_score < 0:
		print 'NO'
	else:
		print max_score
	case += 1


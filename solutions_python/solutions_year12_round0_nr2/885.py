# -*- coding: utf-8 -*-
# Google Code Jam 2012 - Qualification Round
# http://code.google.com/codejam/contest/1460488/dashboard#s=p1
# Copyright © 2012 Aluísio Augusto Silva Gonçalves
# This module is free software, licensed under the terms of the Artistic License 2.0


"""
   Dancing With the Googlers
"""


# Imports {{{1
##############

import CodeJam


# Functions {{{1
################

def is_valid (a, b, c):
	return abs(a - b) <= 2 and abs(b - c) <= 2 and abs(a - c) <= 2

def is_surprising (a, b, c):
	return abs(a - b) == 2 or abs(b - c) == 2 or abs(a - c) == 2

def next_score (points, max, check=None):
	return next(i for i in range(max, -1, -1) if i <= points and (check is None or abs(a - check) <= 2))

def find_scores (points, best, surprising=False):
	scores = filter(lambda e: sum(e) == points, SCORES)
	best_scores = filter(lambda e: any(x >= best for x in e), scores)
	best = False
	if best_scores:
		best = True
		scores = best_scores
	if surprising:
		scores = filter(lambda e: is_surprising(*e), scores)
	else:
		scores = filter(lambda e: not is_surprising(*e), scores)
	return (best, scores)

def best_score_set (target, surprises, *points_set):
	bests = 0
	# Handle single cases first
	next_round = []
	for points in points_set:
		u_is_best, u_score = find_scores(points, target)
		s_is_best, s_score = find_scores(points, target, True)
		if u_score and s_score:
			next_round.append((points, u_is_best, s_is_best))
			continue
		if s_score:
			if surprises == 0:
				# And then something happened, something I knew was impossible
				# but it happened anyway
				continue
			else:
				surprises -= 1
		if s_is_best or u_is_best:
			bests += 1
	# Now choose when to surprise
	for points, u_is_best, s_is_best in next_round:
		if surprises == 0 or not s_is_best:
			# Leave it to someone else
			if u_is_best:
				bests += 1
		else:
			surprises -= 1
			if s_is_best:
				bests += 1
	# Now we're done
	return bests


# Data {{{1
###########

# Generate all possible triplets of scores
score_range = xrange(0, 11)
SCORES = ((a, b, c) for a in xrange(0, 11) for b in xrange(0, 11) for c in xrange(0, 11))
SCORES = filter(lambda e: is_valid(*e), SCORES)


# Entry point {{{1
##################

@CodeJam.ProblemSolver(__name__, 1)
def solve (input):
	in_ = [int(e) for e in input[0].split()]
	return best_score_set(in_[2], in_[1], *in_[3:])

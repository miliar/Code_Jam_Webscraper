#!/usr/bin/env python

import operator
import math
from pprint import pprint
from fractions import gcd

log = False


def RPI(WP, OWP, OOWP):
	return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

def solve(matrix):
	WP_vector = []
	OWP_vector = []
	OOWP_vector = []
	
	for team_row in matrix:
		team_row = filter(lambda b: b != NO_GAME, team_row)

		wins = sum(1 for game in team_row if game == WIN)
		WP = wins / float(len(team_row))
		WP_vector.append(WP)

	sum_WP_vector = sum(WP_vector)
	for i, team_row in enumerate(matrix):
		if log:
			print ''
			
		ops = set()
		for i2, r in enumerate(matrix):
			if r[i] != NO_GAME and i != i2:
				ops.add(i2)
		


		game = [m for m in matrix]
		game.pop(i)
		
		game = filter(lambda r: r[i] != NO_GAME, game)
		
		total_wins = 0
		counts = 0
		
		#print ''
		for o in ops:
			#print 'o ', o
			team_row2 = list(matrix[o])
			team_row2.pop(i)
			team_row2 = filter(lambda b: b != NO_GAME, team_row2)
			
			wins = sum(1 for b in team_row2 if b == WIN)
			counts += len(team_row2)
			total_wins += wins/ float(len(team_row2))
			
			#print wins/ len(team_row2)
			
		#print total_wins, float(len(ops))

		#~ for team_row2 in game:
			#~ team_row2 = list(team_row2)
			#~ team_row2.pop(i)
			#~ team_row2 = filter(lambda b: b != NO_GAME, team_row2)
			#~ 
			#~ wins = sum(1 for b in team_row2 if b == WIN)
			#~ counts += len(team_row2)
			#~ total_wins += wins
			
			
		OWP_vector.append(total_wins / float(len(ops)))
	
	sum_OWP_vector = sum(OWP_vector)
	for i, team_row in enumerate(matrix):
		game = [m for m in OWP_vector]
		
		ops = set()
		for i2, r in enumerate(matrix):
			if r[i] != NO_GAME and i != i2:
				ops.add(i2)
				
		OOWP = 0
		for o in ops:
			OOWP += OWP_vector[o]
			
		OOWP_vector.append(OOWP/float(len(ops)))
		
	#~ pprint(WP_vector)
	#~ pprint(OWP_vector)
	#~ pprint(OOWP_vector)
	
	return [RPI(WP, OWP, OOWP) for WP, OWP, OOWP in zip(WP_vector, OWP_vector, OOWP_vector)]
					
NO_GAME = '.'
WIN = '1'
LOSE = '0'

				
if __name__ == '__main__':    
	with open('A-large-0.in') as f:
		lines = f.readlines()

	problems = []

	line_num = 0
	
	num_problems = int(lines[line_num])
	line_num += 1
	
	for problem_lines in range(num_problems):
		N = int(lines[line_num])
		line_num += 1
		matrix = []
		for team_line in range(N):
			matrix.append(lines[line_num].strip())
			line_num += 1

		problems.append(matrix)

	#~ if log:
		#~ pprint(problems)

	for problem_num, matrix in enumerate(problems):
		if log:
			print ''
			print '###'
			print matrix
		
		answer = solve(matrix)
		
		print 'Case #%d:' % (problem_num+1)
		for a in answer:
			print a





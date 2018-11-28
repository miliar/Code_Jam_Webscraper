#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#solve case function
def solve_case(sb, case_number):
	print "Case #" + str(case_number) + ":"
	matches = []
	wps = []
	owps = []
	oowps = []
	for ts in sb:
		wins = float(ts.count('1'))
		loses = float(ts.count('0'))
		wps.append([wins,(wins + loses)])
		matches.append(wins + loses)
	for ts,m in zip(sb, matches):
		tmp_owps = 0.0
		for t,w in zip(ts, wps):
			if t == '1':
				tmp_owps += w[0] / (w[1] - 1)
			elif t == '0':
				tmp_owps += (w[0] - 1) / (w[1] - 1)
		owps.append(tmp_owps / m)
	for ts,m in zip(sb, matches):
		tmp_oowps = 0.0
		for t,o in zip(ts, owps):
			if t == '1' or t == '0':
				tmp_oowps += o
		oowps.append(tmp_oowps / m)
	for w, o, oo in zip(wps, owps, oowps):
		print 0.25 * (w[0] / w[1]) + 0.50 * o + 0.25 * oo


#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	team_num = int(r.readline().strip())
	score_board = []
	for n in range(0, int(team_num)):
		score_board.append(list(r.readline().strip()))
	solve_case(score_board, case_number)


#!/usr/bin/python

import sys

def solve(cases):
	solution = []
	for case in cases:
		N = case[0]
		games = case[1]
		
		WP = []
		for team in games:
			wins = 0
			losses = 0
			for game in team:
				if game == '1':
					wins += 1
				elif game == '0':
					losses += 1
			if wins == 0 and losses == 0:
				WP.append(0.0)
			else:
				WP.append(float(wins) / float(wins + losses))

		OWP = []
		for i in range(N): # Going through teams
			acc = 0.0
			opp = 0
			for j in range(N): # Going through opponents
				wins = 0
				losses = 0
				if i != j and games[i][j] != '.':
					opp += 1
					for k in range(N): # Going through the games of opponents
						if k != i:
							if games[j][k] == '1':
								wins += 1
							elif games[j][k] == '0':
								losses += 1
					if not (wins == 0 and losses == 0):
						acc += float(wins) / float(wins + losses)
			acc /= float(opp)
			OWP.append(acc)

		OOWP = []
		for i in range(N):
			acc = 0.0
			opp = 0
			for j in range(N):
				if i != j and games[i][j] != '.':
					opp += 1
					acc += OWP[j]
			OOWP.append(acc / float(opp))

		csol = []
		for i in range(N):
			csol.append(0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i])
		
		solution.append(csol)

	return solution


f = open(sys.argv[1],'r')
caseCount = int(f.readline().strip('\n'))
cases = []
for i in range(caseCount):
	teamCount = int(f.readline().strip('\n'))
	case = []
	for i in range(teamCount):
		case.append(f.readline().strip('\n'))
	cases.append((teamCount,case))

solution = solve(cases)

for i in range(len(cases)):
	print "Case #" + str(i + 1) + ": "
	for sol in solution[i]:
		print sol

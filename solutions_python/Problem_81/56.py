#!/usr/bin/env python

def solve(matrix):
	teamWPfrac = [(line.count('1'),len(matrix) - line.count('.')) for line in matrix]
	teamWP = [a / float(b) for a,b in teamWPfrac]

	oppWP = []
	for team, line in enumerate(matrix):
		games = 0
		temp = 0.0
		for opp, symbol in enumerate(line):
			if symbol == '.':
				continue

			w,g = teamWPfrac[opp]
			temp += (w - (symbol == '0')) / float(g - 1)
			games += 1

		oppWP.append(temp / float(games))
	
	oppoppWP = []
	for team, line in enumerate(matrix):
		games = 0
		temp = 0.0
		for opp, symbol in enumerate(line):
			if symbol == '.':
				continue
			temp += oppWP[opp]
			games += 1
			
		oppoppWP.append(temp / float(games))

	print matrix
	print
	print teamWPfrac
	print oppWP
	print oppoppWP
	print
	print [teamWP[i] / 4 + oppWP[i] / 2 + oppoppWP[i] / 4 for i in xrange(len(matrix))]
	print
	print
	print


	return [teamWP[i] / 4 + oppWP[i] / 2 + oppoppWP[i] / 4 for i in xrange(len(matrix))]



def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for case in xrange(tests):
		numTeams = int(inFile.readline())
		matrix = [inFile.readline().strip() for team in xrange(numTeams)]
		outFile.write("Case #{0}:\n".format(case+1))
		for i in solve(matrix):
			outFile.write("{0}\n".format(i))

solveFile("example.in")
solveFile("A-small-attempt0.in")
solveFile("A-large.in")


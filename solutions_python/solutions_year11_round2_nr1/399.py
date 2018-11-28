#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

class Team:

	def __init__(self, number):
		self.number = number
		self.games = {}
		self.played = 0.0
		self.won = 0.0

	def calculateWP(self):
		#print "WP:", self.number, self.won, self.played
		self.wp = self.won / self.played

	def calculateOWP(self, teams):
		#print "OWP of", self.number
		owp = 0
		for team in teams:
			owp += team.calculateTeamWP(self.number)
			#print "--versus", team.number, "=", team.calculateTeamWP(self.number)
		self.owp = owp / self.played

	def calculateOOWP(self, teams):
		oowp = 0
		for team in teams:
			if team.number in self.games:
				oowp += team.owp
		self.oowp = oowp / self.played

	def calculateRPI(self):
		#print "Team", self.number, self.wp, self.owp, self.oowp
		return 0.25 * self.wp + 0.5 * self.owp + 0.25 * self.oowp

	def calculateTeamWP(self, team):
		if team == self.number or team not in self.games:
			return 0.0
		elif self.games[team] == "1":
			return (self.won - 1) / (self.played - 1)
		else:
			return self.won / (self.played - 1)

def readTestCases(inName):
	if inName.index(".in") > -1:
		outName = inName.replace(".in", ".out")
	else:
		outName = inName + ".out"

	with open(inName) as inFile:
		with open(outName, "w") as outFile:
			cases = int(inFile.readline())
			for i in xrange(cases):
				solveCase(i + 1, inFile, outFile)

def solveCase(case, inFile, outFile):
	n = int(inFile.readline())
	teams = []
	for i in xrange(n):
		team = Team(i)
		teams.append(team)
		for i, game in enumerate(inFile.readline()):
			#print i, game
			if game == "0":
				team.games[i] = game
				team.played += 1
			if game == "1":
				team.games[i] = game
				team.played += 1
				team.won += 1
		team.calculateWP()
	
	for team in teams:
		team.calculateOWP(teams)
	
	for team in teams:
		team.calculateOOWP(teams)
	
	
	outFile.write("Case #{0}:\n".format(case))
	for team in teams:
		outFile.write("{0}\n".format(team.calculateRPI()))

if __name__ == "__main__":
	readTestCases(sys.argv[1])

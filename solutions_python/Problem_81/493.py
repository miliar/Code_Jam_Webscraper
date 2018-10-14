#!/usr/bin/python
import sys

class Team:
	def __init__(self, number, line):
		line = line.rstrip("\r\n")
		self.number = number
		self.games = list(line)
		self.played = 0
		self.won = 0
		self.lost = 0
		self.rpi = 0
		self.owp = 0
		self.oowp = 0
		for game in self.games:
			if game != '.':
				self.played +=1
				if game=='1':
					self.won +=1
				else:
					self.lost +=1
		self.wp = float(self.won) / self.played
		
	def playedAgainst(self, team):
		if self.games[team] != '.':
			return True
		else:
			return False
			
	def calcOWP(self):
		answer = 0
		index = 0
		for x in self.games:
			if x!='.':
				answer += collection[index].WP2(self.number)
			index += 1
		self.owp = float(answer) / self.played
	
	def calcOOWP(self):
		answer = 0
		index = 0
		for x in self.games:
			if x!='.':
				answer += collection[index].owp
			index += 1
		self.oowp = float(answer) / self.played
	
	def WP2(self, team):
		index = 0
		won = 0
		played = 0
		for game in self.games:
			if game != '.' and index!=team:
				played +=1
				if game=='1':
					won +=1
			index += 1
		return float(won) / played
			
		
			
def asum(a):
	return a.label

data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	teams = int(data.pop(0))
	team = 0
	collection = []
	while (team < teams):
		collection.append(Team(team, data.pop(0)))
		team += 1
	
	for x in collection:
		x.calcOWP()
		
	for x in collection:
		x.calcOOWP()
		
	sys.stdout.write("Case #%d:\n" % case)
	for x in collection:
		sys.stdout.write("%f\n" % ((0.25 * x.wp) + (0.5 * x.owp) + (0.25 * x.oowp)))
	case += 1
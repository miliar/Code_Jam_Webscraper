from __future__ import division
import sys


class Team():
	def __init__(self,id_, matrix_, teams_):
		self.id = id_
		self.matrix = matrix_
		self.teams = teams_

		self.calc_wp()

	def calc_wp(self):
		self.num_games = 0
		self.num_won = 0
		self.opponents = []

		for i,match in enumerate(self.matrix[self.id]):
			if match == '1':
				self.num_games += 1
				self.num_won += 1
				self.opponents.append(i)
			elif match == '0':
				self.num_games += 1
				self.opponents.append(i)
			elif match == '.':
				pass
			else:
				print "Got weird match (%s) value in row %d" % (match, self.id)

		self.wp = self.num_won / self.num_games

	def calc_owp(self):
		wps = []
		for index in self.opponents:
			opponent = self.teams[index]
			their_win = opponent.num_won
			their_games = opponent.num_games - 1
			if self.matrix[self.id][index] == '0':
				their_win -= 1
			wps.append(their_win / their_games)

		self.owp = sum(wps) / len(wps)

	def calc_oowp(self):
		owps = []
		for index in self.opponents:
			opponent = self.teams[index]
			owps.append(opponent.owp)
		self.oowp = sum(owps) / len(owps)

	def calc_rpi(self):
		self.rpi = 0.25 * self.wp + 0.50 * self.owp + 0.25 * self.oowp

def do_line(num_teams, matrix):
	teams = []
	for i in range(num_teams):
		teams.append(Team(i, matrix, teams))
	for team in teams:
		team.calc_owp()
	for team in teams:
		team.calc_oowp()
	for team in teams:
		team.calc_rpi()
	return [team.rpi for team in teams]


in_, out_f= sys.argv[1], sys.argv[1]+".out"
out = open(out_f, 'w')
with open(in_, 'r') as file:
	num = 1
	num_cases = int(file.next().rstrip())
	for num in range(1, num_cases+1):

		num_teams = int(file.next().rstrip())
		matrix = [[None for i in range(num_teams)] for j in range(num_teams)]
		for j in range(num_teams):
			for i,result in enumerate(file.next().rstrip()):
				matrix[j][i] = result
#		print matrix
		ret = do_line(num_teams, matrix)
		out.write("Case #%d:\n" % (num))
		#print "Case #%d:\n" % (num),
		for rpi in ret:
			out.write("%0.7f\n" % (rpi))
		#	print "%0.7f\n" % (rpi),
		num += 1


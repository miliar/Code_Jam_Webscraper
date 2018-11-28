from sys import stdin

class Schedule(object):
	def __init__(self, in_file, teams):
		self.teams = []
		self._schedule = []
		for i in range(teams):
			self.teams.append(Team())
			self._schedule.append(in_file.next())

	def winner(self, a, b):
		outcome = self._schedule[a][b]
		if outcome == '1':
			return (self.teams[a],self.teams[b])
		elif outcome == '0':
			return (self.teams[b],self.teams[a])
		else:
			return None,None

	def RPI(self, team):
		return 0.25 * team.wp() + 0.50 * team.owp + 0.25 * team.oowp

	def scores(self):
		self.compute_wins()

		for i in self.teams:
			i.compute_owp()

		for i in self.teams:
			i.compute_oowp()
			yield self.RPI(i)

	def compute_wins(self):
		n = len(self.teams)
		for i in range(n):
			for j in range(n):
				# Only look at scores where i < j: the other half of the matrix is redundant
				if j == i: break

				outcome = self._schedule[i][j]
				if outcome == '1':
					w,l = (self.teams[i],self.teams[j])
				elif outcome == '0':
					w,l = (self.teams[j],self.teams[i])
				else:
					w,l = (None, None)

				if w:
					w.play(l, True)
					l.play(w, False)

class Team(object):
	def __init__(self):
		self.wins = []
		self.opponents = []
		self.owp = 0
		self.oowp = 0

	def wp(self, ignore=None):
		if not self.opponents:
			return 0

		if not ignore:
			return len(self.wins) / float(len(self.opponents))
		else:
			wins = [i for i in self.wins if i is not ignore]
			games = [i for i in self.opponents if i is not ignore]
			return len(wins) / float(len(games))

	def compute_owp(self):
		for i in self.opponents:
			self.owp += i.wp(ignore=self)
		if self.opponents:
			self.owp /= float(len(self.opponents))

	def compute_oowp(self):
		for i in self.opponents:
			self.oowp += i.owp

		if self.opponents:
			self.oowp /= float(len(self.opponents))

	def play(self, team, win=False):
		self.opponents.append(team)
		if win:
			self.wins.append(team)

def parse_input(in_file):
	in_file.next()

	while True:
		try:
			teams = int(in_file.next())
			s = Schedule(in_file, teams)
			yield s
		except StopIteration:
			break

for i, s in enumerate(parse_input(stdin)):
	print 'Case #%d:' % (i + 1)
	for rpi in s.scores():
		print rpi

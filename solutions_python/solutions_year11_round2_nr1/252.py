import sys,re

class Team:
	def __init__(self):
		self.wins = set()
		self.lost = set()
		self.opponents = set()
		self.wp = 0
		self.owp = 0

T = int(sys.stdin.readline())

for case in range(T):
	count = int(sys.stdin.readline())
	teams = [ Team() for x in range(count) ]
	for i in range(count):
		for j,char in enumerate(sys.stdin.readline().strip()):
			team = teams[i]
			if char == '1': team.wins.add(j); team.opponents.add(j); 
			elif char == '0': team.lost.add(j); team.opponents.add(j)
	print "Case #%d:"%(case+1)
	for team in teams:
		team.wp = float(len(team.wins))/float(len(team.wins)+len(team.lost))
		#print "wins",team.wins,"lost",team.lost,"wp", team.wp
	for i,team in enumerate(teams):
		opp_wp = []
		for opp in team.opponents:
			opponent = teams[opp]
			wins = len([ x for x in opponent.wins if x != i ])
			lost = len([ x for x in opponent.lost if x != i ])
			opp_wp.append( float(wins)/float(wins+lost) )
		team.owp = float(sum(opp_wp)) / len(opp_wp)
		#print "owp",team.owp	
	for team in teams:
		WP = team.wp
		OWP = team.owp
		owpsum = 0.0
		for op in team.opponents:
			owpsum+=teams[op].owp
		OOWP = float(sum([ teams[opp].owp for opp in team.opponents ])) / float(len(team.opponents))
		RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		print RPI
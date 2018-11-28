from __future__ import division
import sys

teams = [
	( [(1, 1), (2, 1)], (2,2) ),
	( [(0, 0), (2, 0), (3, 0)], (0,3) ),
	( [(0,0), (1, 1), (3, 1)], (2, 3) ),
	( [(1, 1), (2, 0)], (1,2) )
]

def wp((_, (wins, games)), w = None):
	if w is None:
		return wins/games
	else:
		return (wins - (1 - w))/(games - 1)

def avg(*nums):
	return sum(nums) / len(list(nums))

def owp((opponents, record), teams):
	return avg( *[wp(teams[team], w) for (team, w) in opponents] )

def oowp((opponents, record), teams):
	return avg( *[owp(teams[team], teams) for (team, _) in opponents] )

def rpi(teams, team):
	return .25 * wp(team) + .5 * owp(team, teams) + .25 * oowp(team, teams)

def all_rpi(teams):
	return "\n".join(map(lambda t: str(rpi(teams, t)), teams))


def run_trial(t, teams, out = sys.stdout):
	sol = all_rpi(teams)
	print >> out, "Case #%d: \n%s" % (t, sol)

lines = """2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
""".split('\n')

def main(args):
	global lines
	if len(args) > 1:
		lines = open(args[1]).readlines()
	lines.reverse()
	trials = int(lines.pop())
	for t in xrange(1, trials + 1):
		teams = []
		num_teams = int(lines.pop())
		for _ in xrange(num_teams):
			outcomes = lines.pop().rstrip()
			opponents = [ (team, int(outcome)) for team, outcome in enumerate(outcomes) if outcome != '.' ]
			record = ( sum( int(outcome) for outcome in outcomes if outcome != '.'), len([outcome for outcome in outcomes if outcome != '.'] ))
			teams.append( (opponents, record))
		run_trial(t, teams)

if __name__ == '__main__':
	main(sys.argv)
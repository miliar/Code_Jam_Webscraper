import sys

DEFAULT_MESSAGE = 'Game has not completed'
WILDCARD = 'T'
GAME_LENGTH = 4

global dot_count

class FoundWinner(Exception):
	def __init__(self, winner):
		self.val = "%s won" % winner
	def __str__(self):
		return self.val

class FoundDraw(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return "Draw"

def run_all_tests(game):
	global dot_count

	# run horizontal matches
	for horiz in game:
		run_match(horiz, 'O')
		run_match(horiz, 'X')

	# run column matches
	for i in range(0, GAME_LENGTH):
		culm = []
		for horiz in game:
			culm.append(horiz[i])
		run_match(culm, 'O')
		run_match(culm, 'X')

	# run diagonal matches
	diag_fwd = []
	diag_rev = []
	for i in range(0, GAME_LENGTH):
		diag_fwd.append(game[i][i])
		diag_rev.append(game[i][(GAME_LENGTH-1)-i])
	run_match(diag_fwd, 'O')
	run_match(diag_fwd, 'X')
	run_match(diag_rev, 'O')
	run_match(diag_rev, 'X')

	if dot_count == 0:
		raise FoundDraw()

def run_match(hrow, match):
	global dot_count
	if hrow.count(match) + hrow.count(WILDCARD) == GAME_LENGTH:
		raise FoundWinner(match)
	dot_count += hrow.count('.')

fname = sys.argv[1]
dot_count = 0
f = open(fname, 'r')

try:
	num_cases = int(f.readline())
	case_line = 0

	for cur_game in range(0, num_cases):
		dot_count = 0
		game = []
		for j in range(0, GAME_LENGTH):
			game.append(f.readline())
		f.readline()

		msg = DEFAULT_MESSAGE
		try:
			run_all_tests(game)
		except (FoundWinner, FoundDraw), e:
			msg = e.__str__()
		finally:
			print "Case #%d: %s" % (cur_game+1, msg)


except Exception, e:
	print e
finally:
	f.close()
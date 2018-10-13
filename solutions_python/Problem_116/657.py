def get_input():
	s = []
	for i in range(4):
		s.append(raw_input()[:4])
	raw_input()
	return s

def same(a, b):
	if a == '.' or b == '.':
		return False
	if a == 'T' or b == 'T' or a == b:
		return True
	else:
		return False

def solve(s, round):
	for i in range(4):
		winner = s[i][0]
		if (winner == 'T'):
				winner = s[i][1]

		if same(winner, s[i][0]) and same(winner, s[i][1]) and same(winner, s[i][2]) and same(winner, s[i][3]) :
			print 'Case #{0}: {1} won'.format(round, winner)
			return

	for i in range(4):
		winner = s[0][i]
		if (winner == 'T'):
			winner = s[1][i]
		if same(winner, s[0][i]) and same(winner, s[1][i]) and same(winner, s[2][i]) and same(winner, s[3][i]):
			print 'Case #{0}: {1} won'.format(round, winner)
			return

	winner = s[0][0]
	if (winner == 'T'):
		winner = s[1][1]
	if same(winner, s[0][0]) and same(winner, s[1][1]) and same(winner, s[2][2]) and same(winner, s[3][3]):
		print 'Case #{0}: {1} won'.format(round, winner)
		return

	winner = s[0][3]
	if (winner == 'T'):
		winner = s[1][2]
	if same(winner, s[0][3]) and same(winner, s[1][2]) and same(winner, s[2][1]) and same(winner, s[3][0]):
		print 'Case #{0}: {1} won'.format(round, winner)
		return
	else:
		for i in range(4):
			for j in range(4):
				if (s[i][j] == '.'):
					print 'Case #{0}: Game has not completed'.format(round)
					return
	print 'Case #{0}: Draw'.format(round)

T = int(raw_input())
for i in range(T):
	solve(get_input(), i+1)
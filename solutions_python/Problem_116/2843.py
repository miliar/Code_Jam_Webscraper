def verify(order):
	for player in ['X', 'O']:
		for o in range(4):
			winner = True

			for i in range(4):
				if order == 0:
					if moves[o][i] != player and moves[o][i] != 'T':
						winner = False
						break

				else:
					if moves[i][o] != player and moves[i][o] != 'T':
						winner = False
						break

			if winner:
				print 'Case #%i: %s won' % (case, player)
				return

		winner = True
		for o in range(4):
			if order == 0:
				if moves[o][o] != player and moves[o][o] != 'T':
					winner = False
					break

			else:
				if moves[-(o+1)][-(o+1)] != player and moves[-(o+1)][-(o+1)] != 'T':
					winner = False
					break

		if winner:
			print 'Case #%i: %s won' % (case, player)
			return

	if order == 0:
		verify(1)
	else:
		for m in moves:
			if '.' in m:
				print 'Case #%i: Game has not completed' % case
				return
			else:
				print 'Case #%i: Draw' % case
				return

a = open('small.in', 'r+')
lines = a.readlines()
a.close()

all_moves = []
moves = []
for l in lines:
	if l == '\n':
		all_moves.append(moves);
		moves = []
	else:
		moves.append(l[:-1])

case = 0
for a in all_moves:
	moves = a;
	case += 1
	verify(0)
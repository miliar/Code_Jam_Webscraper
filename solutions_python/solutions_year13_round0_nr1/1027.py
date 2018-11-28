from sys import stdin

def check_seq(seq, p):
	s = map(lambda c: c == p or c == 'T', seq)
	return all(s)

def check(m, p):
	seqs = m + zip(*m) + [ [m[i][i] for i in range(4)] ] + [ [m[i][3-i] for i in range(4)] ]
	won = lambda seq: check_seq(seq, p)

	res = map(won, seqs)
	return any(res)

def solve(m):
	if check(m, 'X'):
		return 'X won'
	if check(m, 'O'):
		return 'O won'
	
	s = ''.join(m)
	if s.count('.') == 0:
		return 'Draw'
	return 'Game has not completed'

T = int(stdin.readline())
for t in xrange(T):
	m = []
	for r in xrange(4):
		m.append(stdin.readline().strip())
	stdin.readline() # skip empty
	answer = solve(m)
	print 'Case #%d:' % (t + 1), answer
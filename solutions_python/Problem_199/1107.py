
def parse_input():
	tmp = raw_input()
	S, K = tmp.split()
	K = int(K)

	return S, K

def solve(S, K):
	def flip(S, start, length):
		for i in xrange(length):
			if S[start + i] == '-':
				S[start + i] = '+'
			else:
				S[start + i] = '-'

	S = list(S)
	flip_cnt = 0

	for i in xrange(len(S) - K + 1):
		if S[i] == '-':
			flip_cnt += 1
			flip(S, i, K)

	return S, flip_cnt

def verify(S):
	if '-' in S:
		return False

	return True

T = int(raw_input())

for i in xrange(T):
	S, K = parse_input()
	S, flip_cnt = solve(S, K)

	if verify(S):
		print "Case #%d: %d" % (i + 1, flip_cnt)
	else:
		print "Case #%d: IMPOSSIBLE" % (i + 1)


def imp(n):
	print "Case #%d: IMPOSSIBLE" % n
def case(n, i):
	print "Case #%d: %d" % (n, i)

def flip(S, K, i):
	start = S[:i]
	for t in range(i, i+K):
		if S[t] == '+':
			start += '-'
		else:
			start += '+'
	start += S[K + i:]

	return start

def all_p_Q(S):
	all_eq = True
	for i in xrange(1, len(S)):
		all_eq = all_eq and S[i] == '+' and (S[i] == S[i-1])
	return all_eq

T = input()
for n in xrange(1, T + 1):
	S, K = raw_input().split()
	L = len(S) # 2<=L<= 10|1000
	K = int(K) # 2<=K<=L

	p = 0

	for j in xrange(L):
		if S[j] == '-' and j+K - 1 < L:
			S = flip(S, K, j)
			p += 1

	if all_p_Q(S):
		case(n, p)
	else:
		imp(n)
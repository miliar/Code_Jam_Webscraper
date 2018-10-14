import sys

sys.setrecursionlimit(10000)

def inv(s):
	t = ''
	for x in s:
		t += ('+' if x == '-' else '-')
	return t

def solve(s, k):
	if len(s) <= k:
		if '-' not in s:
			return 0
		if s == ('-'*k):
			return 1
		return -1
	if s[0] == '+':
		return solve(s[1:], k)
	else:
		ret = solve(inv(s[1:k]) + s[k:], k)
		if ret < 0:
			return ret
		return 1 + ret

t = int(sys.stdin.readline())
for i in range(t):
	s, k = sys.stdin.readline().split()
	k = int(k)
	ans = solve(s, k)
	if ans >= 0:
		print('Case #%d: %d' % (i+1, ans))
	else:
		print('Case #%d: IMPOSSIBLE' % (i+1))

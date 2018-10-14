import itertools

MAX_INT = 999999999


def invert(s):
	out = ""
	for c in s:
		if c == '+':
			out += '-'
		else:
			out += '+'
	return out


def flip(s, k, flip_point):
	a = s[:flip_point]
	b = invert(S[flip_point:flip_point + k])
	c = S[flip_point+k:]
	return s[:flip_point] + invert(s[flip_point:flip_point + k]) + s[flip_point+k:]


def all_up(s):
	return s == '+' * len(s)


def solve(s, k):
	for step in range(10000):
		for flip_points in itertools.combinations(list(range(len(s) - k + 1)), step):
			out = '+' * len(s)
			for f in flip_points:
				out = flip(out, k, f)
			# print flip_points, out
			if out == s:
				return step


if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T+1):
		line = raw_input()
		S, K = line.split()
		K = int(K)
		ans = solve(S, K)
		if ans is None:
			ans = 'IMPOSSIBLE'
		print "Case #%s: %s" % (t, ans)

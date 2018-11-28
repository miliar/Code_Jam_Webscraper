
def parseCase():
	d, n = [x for x in input().split(" ")]
	d, n = int(d), int(n)
	h = []
	for _ in range(n):
		k, s = [x for x in input().split(" ")]
		k, s = int(k), int(s)
		h.append((k, s))
	return d, h


def solveCase(case):
	d, h = case
	last = max([(d - k) / s for (k, s) in h])
	return d / last


def flips(s, k):
	f = 0
	i = 0
	while i < (len(s) - k + 1):
		if s[i] == 0:
			s[i : i + k] = [1 - n for n in s[i : i + k]]
			f = f + 1
		i = i + 1
	return f if 0 not in s else 'IMPOSSIBLE'


if __name__ == '__main__':
	t = int(input())
	for i in range(1, t + 1):
		case = parseCase()
		sol = solveCase(case)
		print("Case #{0}: {1}".format(i, sol))

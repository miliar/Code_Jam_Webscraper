
def parseCase():
	s, k = [s for s in input().split(" ")]
	k = int(k)
	s = [int(ord(c) == ord('+')) for c in s]
	return (s, k)


def solveCase(case):
	s, k = case
	return flips(s, k)


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

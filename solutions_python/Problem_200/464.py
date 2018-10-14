inf = open("B-large.in", "r")
outf = open("B-large.out", "w")

input = inf.readline

def to_s(arr):
	return [str(i) for i in arr]

def sol():
	s = list(map(int, input().strip()))
	n = len(s)
	ans = [0 for i in range(n)]
	pref = 0
	for i in range(n):
		for j in range(9, pref - 1, -1):
			for t in range(i, n):
				ans[t] = j
			if (int("".join(to_s(ans))) <= int("".join(to_s(s)))):
				pref = j;
				break
	return int("".join(to_s(ans)))

for i in range(int(input())):
	print("Case #", i + 1, ": ", sol(), sep = "", file = outf)

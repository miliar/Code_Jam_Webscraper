inf = open("input.txt", "r")
outf = open("output.txt", "w")

input = inf.readline

def sol():
	s, a = map(str, input().split())
	n = len(s)
	s = [i for i in s]
	k = int(a)
	cnt = 0
	for i in range(n + 1 - k):
		if (s[i] == '-'):
			cnt += 1
			for j in range(k):
				if (s[j + i] == '-'):
					s[j + i] = '+'
				else:
					s[j + i] = '-'
	# print(s)
	s = "".join(s)
	if (s != '+' * n):
		return "IMPOSSIBLE"
	else:
		return cnt

for i in range(int(input())):
	print("Case #", i + 1, ": ", sol(), sep = "", file = outf)

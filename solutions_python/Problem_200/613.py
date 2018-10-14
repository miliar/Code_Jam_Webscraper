import sys

sys.setrecursionlimit(4000)

def isTidy(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			return i
	return len(l)

def solve(l):
	i = isTidy(l)
	if (i == len(l)):
		return l
	else:
		l[i] = l[i]-1
		for j in range(i+1, len(l)):
			l[j] = 9
		return solve(l)

T = int(raw_input())

for i in range(T):
	l = map(lambda s: int(s), list((raw_input())))
	res = solve(l)
	res = int("".join(map(lambda i: str(i), l)))
	print("Case #%d: %s"%(i+1, res))


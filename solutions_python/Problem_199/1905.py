def solve(s, k):
	l = len(s)
	flips_count = 0
	for i in range(l):
		if s[i] == '-':
			if i > (l - k):
				return -1
			for j in range(i, i+k):
				s[j] = '-' if s[j] == '+' else '+'
			flips_count += 1
	return flips_count

t = int(input())
for case in range(1, t+1):
	s, k = input().split()
	s = list(s)
	k = int(k)
	c = solve(s, k)
	res = str(c) if c != -1 else "IMPOSSIBLE"
	print("Case #%i: %s" % (case, res))

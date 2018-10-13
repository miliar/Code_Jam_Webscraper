#!/usr/bin/python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	s, k = raw_input().split(' ')
	s = [_ == '+' for _ in s]
	k = int(k)
	ls = len(s)

	i = 0
	ans = 0
	while i < ls - k + 1:
		if not s[i]:
			for j in range(i, i+k):
				s[j] = not s[j]
			ans += 1
		i += 1

	for j in range(ls-k, ls):
		if not s[j]:
			ans = 'IMPOSSIBLE'
			break

	print "Case #{}: {}".format(case, ans)
	# check out .format's specification for more formatting options

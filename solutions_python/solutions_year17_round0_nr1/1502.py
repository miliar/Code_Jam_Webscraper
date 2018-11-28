# -*- coding:utf-8 -*-
t = input()

def flip(s, i, j):
	ss = s[:i]
	for idx in xrange(i, j):
		if s[idx] == '+':
			ss += '-'
		else:
			ss += '+'
	ss += s[j:]
	return ss

def solve_exaustive(s, k):

	idx2 = 0
	for char in s:
		if char == "+":
			idx2 += 1
		else:
			break

	n = len(s)

	if s == "+"*n:
		return 0
	# print idx2
	if n - idx2 < k:
		# print "i get first"
		j = n-k
		cnt = 0
		s = flip(s, j, j+k)
		cnt += 1
		
		if s == "+"*n:
			return 1
		return "IMPOSSIBLE"
	else:
		# print "i get second"
		j = idx2
		cnt = 0
		while j <= n-k:
			if s[j] == "-":
				s = flip(s, j, j+k)
				print "after flipping s is " + s
				j += 1
				cnt += 1
			else:
				j += 1

		if s == "+"*n:
			return cnt
		return "IMPOSSIBLE"

for idx in xrange(1,t+1):
	s, k = raw_input().split()
	s = s.strip()
	k = int(k)
	ans = solve_exaustive(s, k)
	print "Case #{0}: {1}".format(idx, ans)
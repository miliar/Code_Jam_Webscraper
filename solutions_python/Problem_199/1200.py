#! /usr/bin/python3

def flip(s, i, k):
	return s[:i] + s[i:i+k].replace('+', 'a').replace('-', '+').replace('a', '-') + s[i+k:]

def f(s, k):
	i = s.find('-')
	c = 0
	n = len(s)
	while i >= 0:
		if i > n-k:
			return "IMPOSSIBLE"
		s = flip(s, i, k)
		c += 1
		i = s.find('-', i+1)
	return c

t = int(input())
for it in range(1, t+1):
	s, k = input().split()
	k = int(k)
	print("Case #%d:" % it, f(s, k))

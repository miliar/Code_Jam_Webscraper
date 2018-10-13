#!/usr/bin/python

dic = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

n = int(raw_input())
for i in range(0, n):
	line = raw_input()
	s = ""
	for j in line:
		if dic.has_key(j):
			s += dic[j]
		else:
			s += j
	print 'Case #%d: %s' % (i + 1, s)

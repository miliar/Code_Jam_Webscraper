# -*- coding: utf-8 -*-

import sys
from collections import deque
fin = sys.stdin
T = int(fin.readline())

for case in range(1,T+1):
	transpose = {}
	opose_let = {}

	game = deque(fin.readline().split())
	t = int(game.popleft())
	for i in range(t):
		r = game.popleft()
		transpose[r[0] + r[1]] = r[2]
		transpose[r[1] + r[0]] = r[2]

	o = int(game.popleft())
	for i in range(o):
		r = game.popleft()
		opose_let[r[1]] = r[0]
		opose_let[r[0]] = r[1]

	r = int(game.popleft())
	b = game.popleft()

	def check_transpose(s):
		if len(s) < 2:
			return (s, False)

		if s[-1] + s[-2] in transpose:
			return (s[:-2] + [transpose[s[-1] + s[-2]]], True)

		return (s, False)

	def check_opose(s):
		if len(s) < 2:
			return s

		if s[-1] in opose_let and opose_let[s[-1]] in s[:-1]:
			return []

		return s

	s = []
	for i in range(r):
		s.append(b[i])

		s, cont = check_transpose(s)
		
		if cont:
			continue

		s = check_opose(s)

	print "Case #%d: %s" % (case, str(s).replace("'", ''))
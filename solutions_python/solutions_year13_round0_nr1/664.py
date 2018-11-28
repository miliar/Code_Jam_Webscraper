#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys, re

fin = open("A.in", "r")
fout = open("A.out", "w")
count = int(fin.readline())

for t in xrange(1, count + 1):
	desk = []
	gsymbols = ["X", "O"]
	ends = set()

	def is_win(line):
		for g in gsymbols:
			if line.count(g) == 4 or (line.count(g) == 3 and line.count("T") == 1):
				ends.add(g)
		return False

	count_p = 0
	for i in range(0, 4):
		s = fin.readline()
		count_p += s.count(".")
		desk.append(s[:4])
	fin.readline()

	is_win(desk[0][0] + desk[1][1] + desk[2][2] + desk[3][3])
	is_win(desk[0][3] + desk[1][2] + desk[2][1] + desk[3][0])

	for row in desk:
		is_win(row)

	for j in xrange(0, 4):
		col = ""
		for i in xrange(0, 4):
			col += desk[i][j]
		is_win(col)

	ends = list(ends)

	if count_p == 0 and len(ends) == 0:
		ends = gsymbols

	fout.write("Case #{0}: ".format(t))
	if len(ends) == 2:
		fout.write("Draw\n")
	elif len(ends) == 1:
		fout.write("{0} won\n".format(ends[0]))
	else:
		fout.write("Game has not completed\n")
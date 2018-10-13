#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys, re

fin = open("B.in", "r")
fout = open("B.out", "w")
count = int(fin.readline())

for t in xrange(1, count + 1):
	n, m = [int(x) for x in fin.readline().split()]
	cells = []
	for x in range(0, 102):
		cells.append([])
	desk = []
	all_h = set()
	for i in xrange(0, n):
		s = [int(x) for x in fin.readline().split()]
		desk.append(s)
		for j in xrange(0, len(s)):
			all_h.add(s[j])
			cells[s[j]].append((i, j))

	answer = True
	urows = [False] * n
	ucols = [False] * m
	for x in reversed(sorted(list(all_h))):
		nurows = [False] * n
		nucols = [False] * m
		for cell in cells[x]:
			nurows[cell[0]] = True
			nucols[cell[1]] = True
			if urows[cell[0]] and ucols[cell[1]]:
				answer = False
				break
		if not answer:
			break
		urows = nurows
		ucols = nucols

	if answer:
		answer = "YES"
	else:
		answer = "NO"
	fout.write("Case #{0}: {1}\n".format(t, answer))
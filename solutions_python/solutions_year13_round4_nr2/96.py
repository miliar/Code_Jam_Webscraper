#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys, re, itertools

# fin = sys.stdin
# fout = sys.stdout

fin = open("B.in", "r")
fout = open("B.out", "w")

t = int(fin.readline())

for test in xrange(1, t + 1):
	n, p = [int(x) for x in fin.readline().split()]
	a1 = -1L
	a2 = -1L

	num = 0L
	pos =1L
	plus = 2L**(n - 1L)
	for i in xrange(1, n + 2):
		# print "i = {0}, p1 = {1}".format(num, pos)
		if pos <= p:
			a1 = max(num, a1)
		num = min(num + 2L ** i, 2L ** n - 1L)
		pos += plus
		plus /= 2L

	num = 0L
	pos =1L
	plus = 2L**(n - 1L)
	for i in xrange(0, n + 1):
		# print "i = {0}, p2 = {1}".format(num, pos)
		if pos <= p:
			a2 = max(num, a2)
		num += plus
		pos += 2L ** i
		plus /= 2L

	fout.write("Case #{0}: {1} {2}\n".format(test, a1, a2))
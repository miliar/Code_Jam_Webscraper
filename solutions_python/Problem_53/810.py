#!/usr/bin/python

import re

def solve(n, k, c):
	s = 2**n
	if k%s == s-1: return "Case #%d: ON\n" % c
	else: return "Case #%d: OFF\n" % c

f = open("large.in", "r")
w = open("large.out", "w")

cases = int(f.readline())

for i in range(1, cases+1):
	line = f.readline()
	l = line.split(" ")
	if l[0] != '\n':
		w.write(solve(int(l[0]), int(l[1]), i))


f.close()
w.close()

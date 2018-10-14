#!/usr/bin/env python
# encoding: utf-8

import sys, os, re

f = open('./input.txt')
o = open('./output.txt', 'w')
T = int(f.readline())
e = 1e-6

def war(n, naomi, ken):
	t = 0
	while n > 0:
		if n == 1:
			return t+1 if naomi[0] > ken[0] else t
		else:
			if naomi[-1] > ken[-1]:
				naomi = naomi[0:n-1]
				ken = ken[1:]
				t += 1
			else:
				naomi = naomi[0:n-1]
				ken = ken[0:n-1]

		n -= 1

def deceitful_war(n, naomi, ken):
	t = 0
	while n > 0:
		if n == 1:
			return t+1 if naomi[0] > ken[0] else t
		else:
			if naomi[0] < ken[0]:
				naomi = naomi[1:n]
				ken = ken[0:n-1]
			else:
				naomi = naomi[1:n]
				ken = ken[1:n]
				t += 1
		n -= 1

for case in range(1, T+1):
	n = int(f.readline())
	naomi = sorted(map(float, f.readline().split(' ')))
	ken = sorted(map(float, f.readline().split(' ')))

	o.write("Case #%s: %s %s\n" % (case, deceitful_war(n, naomi, ken), war(n, naomi, ken)))

f.close()
o.close()

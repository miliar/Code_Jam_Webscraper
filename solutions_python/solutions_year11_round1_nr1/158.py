#!/usr/bin/python

import sys

def gcd(a,b):
	while b>0:
		a,b = b,a%b
	return a

def do_case(case, l):
	possible = True
	dminplay = 100 / gcd(l[1], 100)
	if dminplay > l[0]:
		possible = False
	if l[1] < 100 and l[2] == 100:
		possible = False
	if l[1] > 0 and l[2] == 0:
		possible = False

	if possible:
		print 'Case #%d: Possible' % case
	else:
		print 'Case #%d: Broken' % case

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
	line_data = data_lines.pop().split(' ')
	do_case(case, [long(x) for x in line_data])
	case += 1

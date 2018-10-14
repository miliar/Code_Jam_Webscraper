#!/usr/bin/env python

import os, sys

def cnt(r):
	t = 0
	x = 0
	o = 0

	for i in r:
		if i == 'X':
			x += 1
		elif i == 'O':
			o += 1
		elif i == 'T':
			t += 1
		elif i == '.':
			pass
		else:
			print "error"

	return test(x,o,t)

def test(x,o,t):
	if x == 4:
		return "X won"
	if x == 3 and t == 1:
		return "X won"
	if o == 4:
		return "O won"
	if o == 3 and t == 1:
		return "O won"
	return None

def determine(a):
	for i in xrange(0,4):
		ret = cnt(a[i])
		if ret is not None:
			return ret
	
	for i in xrange(0,4):
		ret = cnt(a[0][i] + a[1][i] + a[2][i] + a[3][i])
		if ret is not None:
			return ret

	ret = cnt(a[0][0] + a[1][1] + a[2][2] + a[3][3])
	if ret is not None:
		return ret

	ret = cnt(a[0][3] + a[1][2] + a[2][1] + a[3][0])
	if ret is not None:
		return ret
	
	if ''.join(a).find('.') == -1:
		return "Draw"
	else:
		return "Game has not completed"

	return "Unknown"

def main():
	f = open(sys.argv[1], 'r')
	n_test = int(f.readline().strip())

	for i in xrange(1, n_test+1):
		a = []
		a.append(f.readline().strip())
		a.append(f.readline().strip())
		a.append(f.readline().strip())
		a.append(f.readline().strip())

		try:
			f.readline()
		except:
			pass

		print "Case #%d: %s" % (i, determine(a))

main()

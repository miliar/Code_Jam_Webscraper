#!/usr/bin/env python

import os, sys, math

def build(a, n, m):
	col = []
	row = []

	for i in xrange(0, n):
		row.append(max(a[i]))

	for i in xrange(0, m):
		b = []
		for j in xrange(0,n):
			b.append(a[j][i])
		col.append(max(b))

	return (col, row)

def determine(a, n, m):
	col, row = build(a, n, m)
	for i in xrange(0,n):
		for j in xrange(0,m):
			if row[i] > a[i][j] and col[j] > a[i][j]:
				return "NO"
	return "YES"

def main():
	f = open(sys.argv[1], 'r')
	n_test = int(f.readline().strip())

	for i in xrange(1, n_test+1):
		tmp = f.readline().strip().split(" ")
		n = int(tmp[0])
		m = int(tmp[1])

		a = []
		for j in xrange(0, n):
			a.append(f.readline().strip().split(" "))

		print "Case #%d: %s" % (i, determine(a, n, m))

main()

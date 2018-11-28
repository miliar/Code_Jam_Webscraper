from sys import stdin
from collections import defaultdict

for cs in xrange(1,1+int(stdin.readline().strip())):
	(n,m) = [int(z) for z in stdin.readline().split()]
	# print n,m

	rows = [[char for char in stdin.readline().split()] for nn in xrange(n)]

	minbyrow = [max(row) for row in rows]
	minbycol = [max(col) for col in map(list, zip(*rows))]
	# print minbyrow, minbycol

	sol = "YES"
	for r in xrange(n):
		for c in xrange(m):
			h=rows[r][c]
			if h<minbyrow[r] and h<minbycol[c]:
				sol = "NO"
				break
		if sol=="NO":
			break

	print "Case #" + str(cs) + ": " + sol





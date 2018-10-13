#!/usr/bin/python

from sys import stdin

nump = int(stdin.readline())

for case in xrange(1,nump+1):
	numt = int(stdin.readline())
	liststr = stdin.readline()
	parts = liststr.split()
	ilist = map(int,parts)
	ilist.sort()

	totalvalue = 0
	totalxor = 0

	for num in ilist:
		totalxor = totalxor ^ num
		totalvalue += num

	res = "NO"

	if totalxor == 0:
		res = str(totalvalue - ilist[0])

	print("Case #%d: %s" % (case, res))

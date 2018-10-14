#! /usr/bin/python

badtxt = "Bad magician!"
cheattxt = "Volunteer cheated!"

maxtests = int(raw_input())

for testnum in xrange(1,maxtests+1):
	rowpicks = []
	for g in [1,2]:
		picknum = int(raw_input())

		grid = []
		for x in xrange(1,5):
			thisrow = [int(f) for f in (raw_input()).split(' ')]
			grid.append(thisrow)
			if x == picknum:
				rowpicks.append(thisrow)
	
	magicnum = set(rowpicks[0]) & set(rowpicks[1])

	result = badtxt

	if not magicnum:
		result = cheattxt
	elif len(magicnum) == 1:
		result = str(magicnum.pop())

	print "Case #%d: %s" % (testnum, result)


#!/usr/bin/python

n = input()
for x in range(1, n+1):
	g1 = int(raw_input())

	grid = []

	for i in xrange(1, 5):
	    if i == g1:
	    	grid.extend([int(ii) for ii in raw_input().strip().split() ])
	    else:
	    	raw_input()

	#second guess
	g2 = int(raw_input())
	grid2 = []

	for i in xrange(1, 5):
	    if i == g2:
	    	grid2.extend([int(ii) for ii in raw_input().strip().split() ])
	    else:
	    	raw_input()

	g =filter(set(grid).__contains__, grid2)
	len_g = len(g)
	if (len_g == 1):
		print "Case #%d: %d" % (x, g[0])
	elif len_g == 0:
		print "Case #%d: Volunteer cheated!" % (x,)
	else:
		print "Case #%d: Bad magician!" % (x, )


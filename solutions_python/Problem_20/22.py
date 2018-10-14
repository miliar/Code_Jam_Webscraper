#!/usr/bin/python

cases = int(raw_input())

for c in xrange(1, cases + 1):
	H, W, R = map(int, raw_input().split())
	
	rocks = []
	squares = []
	for i in xrange(W+1):
		vector = (H+1)*[0]
		rocks.append(vector)
		vector = (H+1)*[0]
		squares.append(vector)
	#print "Pre-rocks:"
	#print rocks
	for i in xrange(R):
		y,x = map(int, raw_input().split())
		rocks[x][y] = 1
		#print "Rock at x %d y %d" % (x, y)
	
	# Now loop main thing
	squares[1][1] = 1
	
	looping = True
	
	levels = [0]
	foo = 1
	done = False
	for i in xrange(1,101):
		levels.append(foo)
		if foo % 2 == 1 and done == False:
			done = True
		else:
			foo += 1
			done = False
	#print "Rocks:"
	#print rocks
	#print levels
	#print "Max is %d" % max(H,W)
	#print "max level is %d" % levels[max(H,W)]
	for level in xrange(2, levels[max(H,W)]+1):
		for x,y in zip(xrange(level, 2*level),xrange(2*level-1, level-1, -1)):
			#print "Doing squares level %d x %d y %d" % (level, x, y)
			if x <= W and y <= H:
				if rocks[x][y] == 1:
					continue
					#print "Skipping due to being a rock"
			if level == 2:
				squares[x][y] = 1
			if x+2 <= W and y+1 <= H:
				#print "Adding 1"
				if rocks[x+2][y+1] == 0:
					squares[x+2][y+1] += squares[x][y]
				#	print "Adding one to x %d y %d" % (x+2, y+1)
			if x+1 <= W and y+2 <= H:
				#print "Adding 2"
				if rocks[x+1][y+2] == 0:
					squares[x+1][y+2] += squares[x][y]
				#	print "Adding one to x %d y %d" % (x+1, y+2)
	
	print "Case #%d: %d" % (c, squares[W][H] % 10007)

# Lawnmower
# Conjecture: for every element suffices to test if we can "go all the way through" in one direction

import math
import sys
import itertools

with open(sys.argv[1], 'r') as f:
	n = int(f.readline().strip())
	for i in range(n):
		l = f.readline().strip().split()
		rows = int(l[0])
		cols = int(l[1])

		R = []
		for j in range(rows):
			R.append([int(x) for x in f.readline().strip().split()])
		C = zip(*R)

		# Now for each elem test "go through" ability
		failed = False
		for x in xrange(cols):
			for y in xrange(rows):
				thisval = R[y][x]
				# Is anyone bigger than me in my row?
				for v in R[y]:
					if v > thisval:
						# Is anyone bigger than me in my col?
						for v2 in C[x]:
							if v2 > thisval:
								failed = True
								break
						if failed:
							break
				if failed:
					break
			if failed:
				break

		if failed:
			print "Case #%d: NO" % (i+1)
		else:
			print "Case #%d: YES" % (i+1)


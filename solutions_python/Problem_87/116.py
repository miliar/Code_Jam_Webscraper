#!/usr/bin/python


def iread(fd):
    return [ int(x) for x in fd.readline().split() ]


class Path():
	def __init__(self, d, V):
		self.dist = float(d)
		self.speed = V

	def __cmp__(self, other):
		if self.speed<other.speed:
			return -1
		elif self.speed>other.speed:
			return 1
		else:
			if self.dist>other.dist:
				return -1
			elif self.dist<other.dist:
				return 1
			else:
				return 0


def solve(fd):

	X, S, R, t, N = iread(fd)
	WalkWays = [None]*N
	for i in xrange(N):
		WalkWays[i] = iread(fd)

	# Convert it in a collection of d,V
	pos = 0
	Way = []
	i = 0
	while pos<X:
		if i>=N:
			# No more walkways
			Way.append(Path(X-pos, S))
			pos = X
		else:
			# Get the next walkway
			B, E, w = WalkWays[i]
			i = i+1
			# Go from current position
			if pos<B:
				Way.append(Path(B-pos, S))
			# Follow the Ww
			Way.append(Path(E-B, S+w))
			pos = E
	# Now Apply the t seconds to the slower blocks
	Way.sort()

	i = 0
	while (t>0) and (i<len(Way)):
		w = Way[i].speed-S+R
		drun = w*t
		if Way[i].dist<=drun:
			Way[i].speed = w
			t -= Way[i].dist/w
		else:
			# Correct just the distance
			Way[i].dist -= t*(R-S)
			t = 0
		i += 1

	# Just integrate....
	Time = 0.0
	for p in Way:
		Time += p.dist/p.speed

	return Time


import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = iread(fd)[0]

for i in xrange(T):
    Time = solve(fd)
    print("Case #%d: %10.8f" % (i+1, Time))
    
fd.close()


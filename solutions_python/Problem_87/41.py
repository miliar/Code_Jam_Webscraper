#!/usr/bin/env python

def solve(X,S,R,T,N, Wraw):
	# run during the slowest parts of the journey

	assert S > 0
	assert R > 0

	Wraw.sort()

	#find the distance between walkways run at least those
	noWalkway = 0
	lastEnd = 0
	for start, end, speed in Wraw:
		noWalkway += start - lastEnd
		lastEnd = end
	noWalkway += X-lastEnd

	time = 0

	if (T * R) <= noWalkway:
		# run as much as possible
		time = T + (noWalkway - (T * R)) / float(S)
		T = 0
	else:
		# run all of it
		time = noWalkway / float(R)
		T -= (noWalkway / float(R))
		assert T >= 0

	assert time >= 0

	Ws = sorted([(s, Start, End) for Start, End, s in Wraw])

	for ws, Start, End in Ws:
		diff = End - Start

		assert diff >= 0
		assert ws >= 0

		if T == 0:
			time += diff / float(ws + S)
		elif diff > ((ws + R) * T):
			notRunning = diff - ((ws + R) * T)
			assert notRunning >= 0
			time += T + notRunning / float(ws + S) 
			T = 0	# used all run
		else:
			time += diff / float(ws + R)
			T -= diff / float(ws + R)
			assert T >= 0

		assert time >= 0


	return time

def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for test in xrange(tests):
		X, S, R, T, N = map(int, inFile.readline().strip().split())
		Ws = [map(int, inFile.readline().strip().split()) for w in xrange(N)]

		outFile.write("Case #{0}: {1}\n".format(test+1, solve(X,S,R,T,N,Ws)))

#solveFile("example.in")
#solveFile("A-small-attempt1.in")
solveFile("A-large.in")

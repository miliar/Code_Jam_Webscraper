

from sys import stdin


def readline(): return stdin.readline().strip('\n')

def readint(): return int(readline())


T = readint()

for t in range(1, T+1):
	C, F, X = [float(x) for x in readline().split(' ')]
	time = 0.0
	per_sec = 2.0
	while (C/per_sec + X/(per_sec + F)) < X/per_sec:
		time += C/per_sec
		per_sec += F
	
	time += X/per_sec
	print 'Case #' + str(t) + ': ' + str(time)


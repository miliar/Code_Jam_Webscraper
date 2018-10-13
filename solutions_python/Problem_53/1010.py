import os, sys, math

infile = open(sys.argv[1], "r")

T = int(infile.readline().rstrip())

for t in range(0, T):
	list = map(int, infile.readline().rstrip().split())
	N = list[0]
	K = list[1]
	plugs = [0 for x in range(0, N)]
	for k in range(0, K):
		for x in range(0, N):
			if plugs[x] == 0:
				plugs[x] = 1
				break
			plugs[x] = 0
				

	print "Case #%d: %s" % (t+1, "ON" if plugs.count(1) == N else "OFF")
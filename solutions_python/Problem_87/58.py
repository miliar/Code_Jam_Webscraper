#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
lines = [x.strip().split(' ') for x in indata[1:]]

def solve(X, S, R, t, N, data):

	totalwalkway = sum([(w[1] - w[0]) for w in data])
	normaldistance = X - totalwalkway

	walkways = [[float(w[1] - w[0]), float(w[2])] for w in data]
	walkways.append([float(normaldistance), 0])
	walkways.sort(key=lambda x: x[1])
	#print walkways

	time = 0
	for i in range(0, len(walkways)):
		w = walkways[i]
		#Can we run all the way
		if t >= w[0] / (w[1]+R):
			thistime = w[0] / (w[1]+R)
			t -= thistime
			time += thistime
		else:
			#Can't run all the way, will run for as much as possible
			distancerun = t*(w[1]+R)
			walktime = (w[0] - distancerun) / (w[1] + S)
			thistime = t + walktime
			t = 0
			time += thistime
		#print time,t
	return time
		

	#normaltime = normaldistance / S
	#walkwaytime = sum([(w[1] - w[0])/(S+w[2]) for w in data])
	#timewithoutrun = normaltime + walkwaytime
	

for j in range(0, numcases):
	X = int(lines[0][0])
	S = int(lines[0][1])
	R = int(lines[0][2])
	t = int(lines[0][3])
	N = int(lines[0][4])
	data = [[int(x) for x in l] for l in lines[1:N+1]]
	assert(N == len(data))
	lines = lines[N+1:]

	sol = solve(X, S, R, t, N, data)

	print "Case #" + str(j+1) + ": " + str(sol)

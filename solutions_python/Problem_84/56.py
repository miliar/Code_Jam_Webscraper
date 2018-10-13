#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
lines = [x.strip().split(' ') for x in indata[1:]]

def solve(data):
	for i in range(0, len(data)-1):
		#Process each row of image
		numblue = len(filter(lambda x: x=='#', data[i]))
		if numblue % 2 != 0:
			return ["Impossible"]
		for j in range(0, len(data[i])):
			if data[i][j] == '#' and data[i+1][j] != '#':
				return ["Impossible"]
		for j in range(0, len(data[i])-1):
			if data[i][j] == '#':
				if data[i][j+1] != '#':
					return ["Impossible"]
				else:
					data[i] = data[i][:j] + '/\\' + data[i][j+2:]
					data[i+1] = data[i+1][:j] + '\\/' + data[i+1][j+2:]
	numblue = len(filter(lambda x: x=='#', data[-1]))
	if numblue > 0:
		return ["Impossible"]
	return data

for j in range(0, numcases):
	R = int(lines[0][0])
	C = int(lines[0][1])
	data = [l[0] for l in lines[1:R+1]]
	assert(R == len(data))
	lines = lines[R+1:]
	#print data

	sol = solve(data)

	print "Case #" + str(j+1) + ":"
	for line in sol:
		print line

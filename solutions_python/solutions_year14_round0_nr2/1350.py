# Solution to "Cookie Clicker Alpha" for Google Code Jam 2014
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import string

def inputData():
	with open(sys.argv[1], 'r') as infile:
		numCases = int(infile.readline())
		for c in range(numCases):
			data = (float(x) for x in infile.readline().split())
			yield data


outfile = open(sys.argv[2], 'w')

for case,(c,f,x) in enumerate(inputData()):
	rate = 2.0
	time = 0
	while c*(rate/f + 1) < x:
		time += c/rate
		rate += f
	answer = time + x/rate
	outfile.write("Case #%d: %.7f\n"%(case+1, answer))

outfile.close()
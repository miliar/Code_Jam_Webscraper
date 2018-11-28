# Mac OS X 10.6.7 2011 MacBook Pro, pypy 1.5.0-alpha0 GCC 4.0.1
# Python 2.7.1 measured 250946 pystones/sec
from __future__ import division
import time, sys, re, math, multiprocessing
if len(sys.argv) > 1:
	inData = open(sys.argv[1]).read().strip()
else:
	inData = """3
4
.11.
0.00
01.1
.10.
3
.10
0.1
10.
4
.11.
0.00
01.1
.10."""

def parseLine(x, c):
	x=x[1:]
	teamData = {}
	for i in range(len(x[0])):
		teamData[i] = {}
	for teamNo, data in enumerate(x):
		for teamNo2, out in enumerate(data):
			if out == ".": continue
			else: out = out == "1"
			teamData[teamNo][teamNo2] = out
	#print teamData
	teamWP = []
	for i in teamData.iteritems():
		d = i[1]
		played = len(d.values())
		won = len(filter(lambda x: x, d.values()))
		teamWP.append(won/played)
	#print teamWP
	teamOWP = []
	for i in teamData.iteritems():
		d = i[1]
		out = 0
		for v in d.keys():
			owpC = filter(lambda x: x[0] != i[0], teamData[v].iteritems())
			owp = len(filter(lambda x: x[1], owpC))/len(owpC)
			out += owp
		out /= len(d.keys())
		teamOWP.append(out)
	#print teamOWP
	teamOOWP = []
	for i in teamData.iteritems():
		out = 0
		for v in i[1].keys():
			out += teamOWP[v]
		out /= len(i[1].keys())
		teamOOWP.append(out)
	#print teamOOWP
	print "Case #"+str(c+1)+":"
	for t in range(len(teamWP)):
		print 0.25 * teamWP[t] + 0.50 * teamOWP[t] + 0.25 * teamOOWP[t]
	
if __name__ == "__main__":
	inData = inData.split("\n")
	nextIn = []
	c = 0
	for i in inData[1:]:
		if re.match("^[0-9]+$", i):
			if len(nextIn) > 0:
				parseLine(nextIn, c)
				c += 1
				nextIn = []
			nextIn.append(i)
		else:
			nextIn.append(i)
	if len(nextIn) > 0:
		parseLine(nextIn, c)
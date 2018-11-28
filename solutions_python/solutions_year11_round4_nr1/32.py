#!/usr/bin/python -OO

import sys;
import math;

def readia():
	return [int(x) for x in sys.stdin.readline().strip().split()];
def readsa():
	return sys.stdin.readline().strip().split();
def readi():
	return int(sys.stdin.readline().strip());
def reads():
	return sys.stdin.readline().strip();
def perr(s):
	print >>sys.stderr, s;

class Walk:
	def __init__(self, (beg, end, speed)):
		self.length = float(end - beg);
		self.speed = float(speed);
	def __str__(self):
		return "(%d %d)" % (self.length, self.speed);

def main():
	T = readi();
	for t in range(T):
		(totalLen, walkSpeed, runSpeed, runTime, numWalks) = readia();
		walks = [];
		for i in xrange(numWalks):
			walks.append(Walk(tuple(readia())));

		walkLen = sum(w.length for w in walks);
		if walkLen < totalLen:
			walks.append(Walk((0, totalLen - walkLen, 0))); 
		walks.sort(cmp = lambda x, y : cmp(x.speed, y.speed));
		#print " ".join(str(x) for x in walks);

		timeToRun = float(runTime);
		totalTime = 0.0;
		for w in walks:
			if timeToRun <= 0.0:
				totalTime += w.length / (w.speed + walkSpeed);
				continue;

			rt = w.length / (w.speed + runSpeed);
			if rt <= timeToRun:
				totalTime += rt;
				timeToRun -= rt;
				continue;

			len1 = w.length - timeToRun * (w.speed + runSpeed);
			totalTime += timeToRun;
			timeToRun = -1.0;
			totalTime += len1 / (w.speed + walkSpeed);
		print "Case #%d: %0.9f" % (t + 1, totalTime);
main();

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

def wp(matr, k, exclude):
	wins = 0;
	total = 0;
	for i in xrange(0, len(matr[k])):
		if i == exclude:
			continue;

		c = matr[k][i];
		if c == '1':
			wins += 1;
			total += 1;
		elif c == '0':
			total += 1;
	#print "wins: ", wins, ", total: ", total;
	return float(wins)/float(max(total, 1));
	#return float(wins)/float(total);

def owp(matr, k):
	res = 0.0;
	total = 0;
	for i in xrange(0, len(matr)):
		if i != k and matr[i][k] != '.':
			#print "add ", wp(matr, i, k);
			res += wp(matr, i, k);
			total += 1;
	#print "div by ", total;
	res /= max(total, 1);
	#print "opw ", k, res;
	return res;

def oowp(matr, owps, k):
	res = 0.0;
	total = 0;
	for i in xrange(len(owps)):
		if i != k and matr[i][k] != '.':
			res += owps[i];
			total += 1;
	return res / max(total, 1);

def main():
	T = readi();
	for t in xrange(T):
		n = readi();
		matr = [];
		for i in xrange(n):
			matr.append(tuple(reads()));
		owps = [];
		for i in xrange(n):
			owps.append(owp(matr, i));
		print "Case #%d:" % (t + 1);
		for i in xrange(n):
			#print i, wp(matr, i, -1), owps[i], oowp(matr, owps, i);
			val = 0.25 * wp(matr, i, -1) + 0.5 * owps[i] + 0.25 * oowp(matr, owps, i);
			print val;





			
main();

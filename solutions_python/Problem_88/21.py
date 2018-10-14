#!/usr/bin/python -OO

import sys;
import math;
import array;

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


def calc_sums(matr, r, c, K):
	sumwir = 0;
	sumwic = 0;
	sumwi = 0;

	for i in xrange(K):
		for j in xrange(K):
			if (i == 0 and j == 0) or (i == 0 and j == K - 1) or (i == K - 1 and j == 0) or (i == K - 1 and j == K - 1):
				continue;
			wi = matr[r + i][c + j];
			sumwi += wi;
			sumwir += i * wi;
			sumwic += j * wi;
	return (sumwir, sumwic, sumwi);

def calcK(matr, rows, cols):
	K = min(rows, cols);
	while K >= 3:
		for r in xrange(rows - K + 1):
			for c in xrange(cols - K + 1):
				(sumwir, sumwic, sumwi) = calc_sums(matr, r, c, K);
				if 2 * sumwir != (K - 1) * sumwi:
					continue;
				if 2 * sumwic != (K - 1) * sumwi:
					continue;
				return (K, r, c);
		K -= 1;
	return (0, 0, 0);


def main():
	T = readi();
	for t in range(T):
		(rows, cols, d) = readia();
		matr = [];
		for r in xrange(rows):
			rr = [d + int(c) for c in reads()];
			if len(rr) != cols:
				raise Exception("bad test " + str(t));
			matr.append(array.array('L', rr));
		#print "\n".join(str(r) for r in matr);		
		(K, r, c) = calcK(matr, rows, cols);
		resStr = "Case #%d: " % (t + 1);
		if K >= 3:
			resStr += str(K);
			#resStr += " %d %d" % (r, c);
		else:
			resStr += "IMPOSSIBLE";
		print resStr;
main();

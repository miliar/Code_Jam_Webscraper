
import sys
import time
import operator
import math
import re


timeit = 1
debugv = 0
startTime = 0

outFile = open('output.txt', 'w')
inFile = sys.stdin
inFile = open('C-test.in', 'r')
inFile = open('C:/Users/quentin/Downloads/C-small-attempt0.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/C-small-practice.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/C-large.in', 'r')

def main():
	T = int(inFile.readline())
	startTime = time.clock()
	for case in range(1,T+1):
		out("Case #{}: ".format(case))
		doCase(case)
		out("\n")


EPS = 0.0000000001


def out(m):
	outFile.write(m)
	sys.stdout.write(m)

import itertools

def doCase(case):
	N, Q = [int(x) for x in inFile.readline().split()]
	H = []
	for i in range(N-1):
		H.append([int(x) for x in inFile.readline().split()])
	inFile.readline()
	D = []
	for i in range(N-1):
		D.append(int(inFile.readline().split()[i+1]))
	inFile.readline()
	inFile.readline()
	best = []
	best.append(0)
	base = 0
	for i in range(1, N):
		iV = N-i-1
		b = best[i-1] + D[iV] / H[iV][1]
		base += D[iV] / H[iV][1]
		d = 0
		j = i-1
		while j >= 0:
			jV = N-j-2
			d += D[jV]
			#print(j, b,jV, iV,H[iV][0], d, d / H[iV][1] + best[j])
			if H[iV][0] < d:
				break
			b = min(b, d / H[iV][1] + best[j])
			j-=1
		best.append(b)
		#print(best, "--------------------------")
	out(str(best[-1]))



def debugln(m):
	debug(m)
	debug('\n')

def debug(m):
	if debugv:
		sys.stdout.write(str(m))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if re.search('d', sys.argv[1]):
			debugv = 1
		if re.search('i', sys.argv[1]):
			inFile = sys.stdin

	main()
	if timeit:
		sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime))


import sys
import time
import operator
import math
import re
import heapq
from collections import deque

timeit = 1
debugv = 0
startTime = 0

outFile = open('output.txt', 'w')
inFile = sys.stdin
inFile = open('B-test.in', 'r')
inFile = open('C:/Users/quentin/Downloads/B-small-attempt0.in', 'r')
inFile = open('C:/Users/quentin/Downloads/B-large.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/B-large-practice.in', 'r')

def main():
	T = int(inFile.readline())
	startTime = time.clock()
	for case in range(1,T+1):
		out("Case #{}: ".format(case))
		doCase(case)
		out("\n")



def out(m):
	outFile.write(m)
	sys.stdout.write(m)

def cobin(k,n):
	#debug(str(k)+" parmi "+str(n)+"\n")
	return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))

import queue
def isTydy(N):
	i = 9
	while N > 0:
		if i < N%10:
			return False
		i = N%10
		N = N // 10
	return True


def  best(N):
	N = str(N)
	safe = 0
	k = int(N[0])
	for i in range(1, len(N)):
		if k < int(N[i]):
			safe = i
			k = int(N[i])
		elif k > int(N[i]):
			return int(N[:safe] + str(int(N[safe]) - 1) + ('9'*(len(N) - safe-1)))
	return int(N)

def doCase(case):
	N = int(inFile.readline())

	out(str(best(N)))




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

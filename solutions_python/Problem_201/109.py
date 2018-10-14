
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
inFile = open('C:/Users/quentin/Downloads/C-small-1-attempt0.in', 'r')
inFile = open('C:/Users/quentin/Downloads/C-small-2-attempt0.in', 'r')
inFile = open('C:/Users/quentin/Downloads/C-large.in', 'r')

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

def solve(n, k):
	k -= 1
	if k == 0:
		return n//2, (n-1)//2

	if n % 2 == 0:
		if k % 2 == 0:
			return solve(n//2 - 1, k//2)
		else:
			return solve(n//2, k//2 + 1)
	if k % 2 == 0:
		return solve(n//2, k//2)
	else:
		return solve(n//2, k//2 + 1)



def doCase(case):
	N, K = [int(i) for i in inFile.readline().split()]
	a,b = solve(N,K)
	out(str(a)+' '+str(b))



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

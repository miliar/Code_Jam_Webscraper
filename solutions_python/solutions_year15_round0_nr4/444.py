
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
inFile = open('D-test.in', 'r')
inFile = open('C:/Users/quentin/Downloads/D-small-attempt1.in', 'r')
#inFile = open('D-large.in', 'r')

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


def doCase(case):
	X, R, C = [int(x) for x in inFile.readline().split()]

	if R < C:
		R, C = C, R

	if X == 1:
		out("GABRIEL")
		return
	if (R*C) % X != 0:
		out("RICHARD")
		return
	if X > R and X > C:
		out("RICHARD")
		return
	if X == 3 and C == 1:
		out("RICHARD")
		return
	if X == 4 and C == 1:
		out("RICHARD")
		return
	if X == 4 and C == 2 and R == 4:
		out("RICHARD")
		return
	if X == 4 and C == 2 and R == 3:
		out("RICHARD")
		return
	if X == 4 and C == 3 and R == 3:
		out("RICHARD")
		return



	out("GABRIEL")
	return
	if X == 2:
		out("GABRIEL")
	if X == 4:
		out("GABRIEL")
	if X == 3:
		if R == 3 and C == 2:
			out("GABRIEL")

	return




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
		sys.stdout.flush() 
		sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime)) 
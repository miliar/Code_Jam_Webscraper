
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
inFile = open('test.in', 'r')
inFile = open('D:/Downloads/A-small-attempt0.in', 'r')
inFile = open('D:/Downloads/A-large.in', 'r')

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

def pgcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a

def doCase(case):
	N, C = [int(x) for x in inFile.readline().split()]
	Files = [int(x) for x in inFile.readline().split()]
	Files = sorted(Files)
	Files.reverse()
	mid = int(math.floor(C/2.0))
	count = 0
	while len(Files) and Files[0] > mid:
		withId = 1
		while withId < len(Files) and Files[withId] + Files[0] > C:
			withId += 1
		if withId < len(Files):
			del(Files[withId])			
		del(Files[0])
		count += 1
	if len(Files):
		count += int(math.ceil(len(Files)/2.0))
	out(str(count))







def debug(m):
	if debugv:
		sys.stdout.write(m)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if re.search('d', sys.argv[1]):
			debugv = 1
		if re.search('i', sys.argv[1]):
			inFile = sys.stdin

	main()
	if timeit:
		sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime)) 
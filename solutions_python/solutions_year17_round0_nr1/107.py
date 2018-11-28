
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
inFile = open('A-test.in', 'r')
inFile = open('C:/Users/quentin/Downloads/A-small-attempt0.in', 'r')
inFile = open('C:/Users/quentin/Downloads/A-large.in', 'r')

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

def shift(S, k, i):
	for j in range(i, i+k):
		s = '-' if S[j]=='+' else '+'
		S = S[:j]+s+S[j+1:]
	return S
def doCase(case):
	S, k = inFile.readline().split()
	k = int(k)
	count=0
	for i in range(len(S)-k+1):
		if S[i]=='-':
			S = shift(S,k,i)
			count+=1
	if '-' in S:
		out('IMPOSSIBLE')
	else:
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
		sys.stdout.flush()
		sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime))

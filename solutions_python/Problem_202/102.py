
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
inFile = open('C:/Users/quentin/Downloads/D-small-attempt2.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/D-large.in', 'r')
#inFile = open('C:/Users/quentin/Downloads/D-large-practice.in', 'r')
#inFile = open('/Users/quentinbramas/Downloads/D-large-practice.in', 'r')


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
	N, K = [int(x) for x in inFile.readline().split()]
	T = []
	for i in range(N):
		T.append(['.']*N)
	for i in range(K):
		t, y, x = inFile.readline().split()
		T[int(x)-1][int(y)-1] = t
	score = N + max(0,N-1) + max(0,N-2) + 1

	Added = []
	oSet = N-1
	for x in range(N-1):
		if T[x][0] == '.':
			Added.append('+ '+str(1)+' '+str(x+1))
			T[x][0] = '+'
		if T[x][0] == 'o' or T[x][0] == 'x':
			oSet = x
	if T[oSet][0] == 'x' or T[oSet][0] == '+' or T[oSet][0] == '.':
		Added.append('o '+str(1)+' '+str(oSet+1))
		T[oSet][0] = 'o'

	if T[N-1][0] == '.':
		if oSet == N-1:
			Added.append('o '+str(1)+' '+str(N))
			T[N-1][0] = 'o'
		else:
			Added.append('+ '+str(1)+' '+str(N))
			T[N-1][0] = '+'

	for i in range(N-2):
		Added.append('x '+str(i+1+1)+' '+str((i+oSet+1)%(N)+1))
		T[(i+oSet+1)%(N)][i+1] = 'x'
	if N > 1:
		if (N-1+oSet)%(N) == N-1 or (N-1+oSet)%(N) == 0:
			Added.append('x '+str(N)+' '+str((N-1+oSet)%(N)+1))
			T[(N-1+oSet)%(N)][N-1] = 'x'
		else:
			Added.append('o '+str(N)+' '+str((N-1+oSet)%(N)+1))
			T[(N-1+oSet)%(N)][N-1] = 'o'
	for i in range(N-1):
		if (i+oSet)%(N) == N-1:
			continue
		if (i+oSet)%(N) == 0:
			continue
		Added.append('+ '+str(N)+' '+str((i+oSet)%(N)+1))
		T[(i+oSet)%(N)][N-1] = '+'
	out(str(score) + ' ' + str(len(Added)))
	print('---------')
	for y in range(N):
		for x in range(N):
			sys.stdout.write(T[x][y]+' ')
		sys.stdout.write('\n')
	for i in Added:
		out('\n'+i)


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

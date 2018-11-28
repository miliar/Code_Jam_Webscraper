from time import time

def nextCase():
	fileName = "B-large.in"
	T = None
	N = None
	for line in open(fileName, 'r').readlines():
		if None == T: T = int(line)
		elif None == N: 
			N, M = tuple([int(x) for x in line.split(' ')])
			i = 0
			R = [None for j in range(N)]
		elif N != i: 
			R[i] = [int(x) for x in line.split(' ')]
			i += 1
			if N == i:
				N = None
				yield R



def _solve(T):
	N, M = len(T), len(T[0])

	levels = sorted({T[i][j] for i in range(N) for j in range(M)})
	def highest(threshold):
		W = [T[i][j] for i in range(N) for j in range(M) if threshold > T[i][j]]
		return max(W) if 0 != len(W) else 0

	max(levels)
	H = max(levels) + 1

	stop = False
	for L in reversed(levels):
		stop = True
		Tnext = [[T[i][j] for j in range(M)] for i in range(N)]
		for i in range(N):
			flag = max(T[i][j] for j in range(M)) <= L
			if flag: 
				for j in range(M): 
					if T[i][j] == L: stop, Tnext[i][j] = False, H
		for i in range(M):
			flag = max(T[j][i] for j in range(N)) <= L
			if flag: 
				for j in range(N): 
					if T[j][i] == L: stop, Tnext[j][i] = False, H

		T = Tnext
		
				
	return "YES" if 0 == highest(H) else "NO"

def solve(T):
	N, M = len(T), len(T[0])

	P = [[False for j in range(M)] for i in range(N)]
	for i in range(N):
		rowMax = max([T[i][j] for j in range(M)])
		for j in range(M):
			P[i][j] = (T[i][j] == rowMax)

	for i in range(M):
		colMax = max([T[j][i] for j in range(N)])
		for j in range(N):
			P[j][i] = True if (T[j][i] == colMax) else P[j][i]

	flag = True
	for i in range(N):
		for j in range(M):
			if not P[i][j]:
				flag = False
				break
		if not flag: break
		
				
	return "YES" if flag else "NO"

start = time()

i = 1
for T in nextCase():
	print("Case #%d: %s" % (i, solve(T)))
	i += 1


#print(time() - start)

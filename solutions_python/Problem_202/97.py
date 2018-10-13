r'''
args = ' '.join([
	r'',
])
import os
import sys
os.system(sys.executable + " %s %s"%(__file__, args))
#os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

import sys
input = """\
2
35 1
o 1 30
20 0
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2
85 2
o 1 47
+ 1 22
""".splitlines(keepends=True)
output = sys.stdout

if 1:
	input = open(r'C:\Users\user1\Desktop\D-small-attempt4.in').readlines()
	#input = open(r'C:\Users\user1\Desktop\C-Large.in').readlines()
	output = open(r'C:\Users\user1\Desktop\D.out', "w")
	
input = iter(input)


from collections import defaultdict
from copy import deepcopy

import random
#for s in dir(random):print(s)
#print(random.sample(range(10), 10))
#raise

def solve(N,E):
	
	C = [0]*N
	R = [0]*N
	Mo = [['.']*N for _ in range(N)]
	X = [[0]*N for _ in range(N)]
	for t,r,c in E:
		if t in 'xo':
			R[r] = 1
			C[c] = 1
			X[r][c] = 1
		Mo[r][c] = t
	#import pdb; pdb.set_trace()5
	#for r in random.sample(range(N), N):
	#	for c in random.sample(range(N), N):
	for r in range(N):
		for c in range(N):
			if R[r] == 0 and C[c] == 0:
				R[r] = 1
				C[c] = 1
				X[r][c] = 1
	
	#[print(x) for x in X]
	Sq = {}
	for i in range(N):
		for j in range(N):
			Sq[(i-j,i+j)] = (i,j)

	R = set()
	L = set()
	
	P = [[0]*N for _ in range(N)]
	for t,r,c in E:
		if t in '+o':
			R.add(r-c)
			L.add(r+c)
			P[r][c] = 1
	
	#for r in random.sample(range(N), N):
	#	for c in random.sample(range(N), N):
	for r in range(N):
		if r % 2:
			r = N - (r+1)//2
		for c in range(N):
			if (r-c) not in R and (r+c) not in L:
				R.add(r-c)
				L.add(r+c)
				P[r][c] = 1
	#print(P)5
	M = [['.']*N for _ in range(N)]
	
	#print(sum([sum(l) for l in X]))
	#print(sum([sum(l) for l in P]))
	
	
	score = 0
	for r in range(N):
		for c in range(N):
			if X[r][c] and P[r][c]:
				M[r][c] = 'o'
				score += 2
			elif X[r][c]:
				M[r][c] = 'x'
				score += 1
			elif P[r][c]:
				M[r][c] = "+"
				score += 1
	#[print('\t'.join(m)) for m in M]
	#print()
	#[print(m) for m in M]
	add = []
	for r in range(N):
		for c in range(N):
			if M[r][c] != Mo[r][c]:
				add += [(M[r][c],r,c)]
			if M[r][c] == '.' and Mo[r][c] != '.':
				raise
			if M[r][c] != Mo[r][c] and M[r][c]!='o' and Mo[r][c]!='.':
				print(M[r][c],Mo[r][c])
				raise
	
	return score,add
	
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	N,M = map(int, next(input).split())
	E = []
	for m in range(M):
		t,r,c = next(input).split()
		r,c = int(r),int(c)
		E += [(t,r-1,c-1)]
	random.seed(0)
	best = 0
	for i in range(1):
		score,add = solve(N,E)
		if score > best:
			best = score
			best_add = add
			#if score == 101:raise
	score = best
	add = best_add
	print("Case #%d:"%case, score, len(add), file=output)
	for t,r,c in add:
		print(t,r+1,c+1, file=output)
	
	
#'''

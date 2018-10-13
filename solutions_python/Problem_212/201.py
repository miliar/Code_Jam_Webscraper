r'''
args = ' '.join([
	r'',
])
import os
import sys
os.system(sys.executable + " %s %s"%(__file__, args))
#os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

input = """\
5
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
4 4
1 2 3 5
7 4
1 2 3 5 8 7 3
""".splitlines(keepends=True)


import sys
output = sys.stdout
if 1:
	input = open(r'A-small-attempt0.in').readlines()
	input = open(r'A-large.in').readlines()
	output = open("A.out", "w")
	
input = iter(input)


import math
from collections import defaultdict,deque

sys.setrecursionlimit(1500)
		
import itertools
# print(math.floor(2.5))
# print(math.ceil(2.5))
# raise

def solve(N,P,G):
	print((N,P,G))
	
	C = defaultdict(int)
	for n in G:
		C[n%P] += 1
		
	if P == 2:
		return C[0] + (C[1]+1)//2
		
	if P == 3:
		res = C[0]
		n = min(C[1], C[(-1)%P])
		res += n
		C[1] -= n
		C[(-1)%P] -= n
		n = max(C[1], C[(-1)%P])
		return res+(n+2)//3
		
	res = C[0]
	n = min(C[1], C[(-1)%P])
	res += n
	
	C[1] -= n
	C[(-1)%P] -= n
	m = max(C[1], C[(-1)%P])
	
	n = C[2]//2
	C[2] -= n*2
	res += n
	
	
	
	if C[2] != 0 and m>=2:
		res += 1
		m -= 2
		C[2] = 0
	if C[2] != 0:
		return res + 1
	
	n = (m+3)//4
	res += n
	return res
	
def calc(p,P):
	score = 0
	sum = 0
	for n in p:
		if sum % P == 0:
			score += 1
		sum += n
	return score
def _solve(N,P,G):
	best = 0
	for p in itertools.permutations(G,N):
		best = max(calc(p,P),best)
	return best 
	
	
import time

caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	#N = int(next(input).strip())
	N,P = [int(s) for s in next(input).split()]
	G = [int(s) for s in next(input).split()]
	t0 = time.time()
	
	res = solve(N,P,G)
	#print("Case #%d:"%case, '%0.20lf'%res, file=output)
	print("Case #%d:"%case, res, file=output)
	print(time.time()-t0)
	sys.stdout.flush()
#'''

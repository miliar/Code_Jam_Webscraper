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
6
2 8
9 5
4684 7920 3600 5203 1730 6820 845 2970
990 2527 3600 2821 476 2000 1350 3743
2 1
500 300
900
660
2 1
500 300
1500
809
2 2
50 100
450 449
1100 1101
2 1
500 300
300
500
2 8
10 10
11 13 17 11 16 14 12 18
14 13 17 11 16 14 12 18
3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900
""".splitlines(keepends=True)

import sys
output = sys.stdout
if 1:
	input = open(r'B-small-attempt1.in').readlines()
	input = open(r'B-large.in').readlines()
	output = open("B.out", "w")
	
input = iter(input)

import math
# print(math.ceil(18/1.1), 13/1.1)
# print(math.floor(18/0.9), 13/0.9)
# raise

# def Round(d):
	# n = int(d)
	# r = d - n
	# r = int(r*10)
	# if r == 9:
		# n += 1
	# elif r > 1:
		# n = 0
	# return n
# print(Round(0.9))
# print(Round(1.5))
# print(Round(0.89))
# print(Round(2.1))
# raise

from collections import defaultdict

def search(G,S,i,low,high):
	if i == len(G) or S[i]==len(G[i]): return low, high
	
	l,h = G[i][S[i]]
	if h<l:
		S[i] += 1
		return 1,-1
		
	if h<low:
		S[i] += 1
		return 1,-1
	
	if high<l:
		return 1,-1
		
	l,h = search(G,S,i+1,max(low,l),min(high,h))
	
	if l<=h:
		S[i] += 1
	return l,h
	
# G = [
# [(9, 9), (9, 10)],
# [(10, 12), (11, 12)],
# ]
# S = [0,0]
# l,h = search(G,S,0,-float('inf'),float('inf'))
# print(l,h)
# print(S)
# print()

# l,h = search(G,S,0,-float('inf'),float('inf'))
# print(l,h)
# print(S)
#raise
#raise

def solve(N,P,R,I):
	for i,l in enumerate(I):
		#l = [n for n in l if int(n*10/R[i])%10 in (0,1,9)]
		l.sort()#(reverse=True)
		#print(l)
	#return []
	
	
	G = []
	for i in range(N):
		l = [(math.ceil(n/1.1/R[i]),math.floor(n/0.9/R[i])) for n in I[i]]
		G += [l]
		print(l)
	#print(G)
	
	count = 0
	S = [0]*N
	for k in range(P):
		#l,h = search(G,S,0,-float('inf'),float('inf'))
		l,h = search(G,S,1,G[0][k][0],G[0][k][1])
		if l == h == -1:
			S[i] += 1
		if l<=h:
			count += 1
		#print(l,h,S)
	return count
	
		
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	N,P = map(int, next(input).split())
	*R, = map(int, next(input).split())
	I = []
	for i in range(N):
		*l, = map(int, next(input).split())
		I += [l]
		
	res = solve(N,P,R,I)
	print("Case #%d:"%case, res, file=output)
#'''
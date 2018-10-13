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
5
4 2
5 2
6 2
1000 1000
1000 1
""".splitlines(keepends=True)
output = sys.stdout

if 1:
	input = open(r'C:\Users\user1\Desktop\C-small-2-attempt0.in').readlines()
	input = open(r'C:\Users\user1\Desktop\C-Large.in').readlines()
	output = open(r'C:\Users\user1\Desktop\C.out', "w")
	
input = iter(input)

from collections import defaultdict
def solve(N,K):
	B = defaultdict(int, {N:1})
	while 1:
		#print(B,K)
		b = max([b for b in B.keys() if B[b]>0])
		k = min(B[b],K)
		
		if K <= B[b]:
			break
		
		B[(b-1)//2]   += k
		B[b//2] += k
		
		B[b] = 0
		K -= k
	
	return b//2, (b-1)//2
	
	#for i,_ in enumerate(N[:-1]):
	
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	N,K = map(int, next(input).split())
	res = solve(N,K)
	print("Case #%d:"%case, *res, file=output)
	
#'''

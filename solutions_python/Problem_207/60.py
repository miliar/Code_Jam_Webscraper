r'''
args = ' '.join([
	r'',
])
import os
import sys
#os.system(sys.executable + " %s %s"%(__file__, args))
os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

# import ctypes
# print(ctypes.cdll.test.test(8))
# raise

input = """\
4
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2
""".splitlines(keepends=True)




import sys
output = sys.stdout
if 1:
	input = open(r'B-small-attempt1.in').readlines()
	#input = open(r'').readlines()
	output = open("B.out", "w")
	
input = iter(input)

import math
from collections import defaultdict

sys.setrecursionlimit(1500)
	
def solve(N,R,O,Y,G,B,V):
	l = [(R,'R'),(Y,'Y'),(B,'B')]
	l.sort()
	if l[2][0] > l[1][0] + l[0][0]:
		return 'IMPOSSIBLE'
		
	res = ''
	n = l[1][0] + l[0][0] - l[2][0]
	for i in range(n):
		res += l[2][1] + l[0][1] + l[1][1]
	for i in range(l[1][0]-n):
		res += l[2][1] + l[1][1]
	for i in range(l[0][0]-n):
		res += l[2][1] + l[0][1]
	
	# r = b = y = 0
	# for c in res:
		# if c=='R': r += 1
		# if c=='B': b += 1
		# if c=='Y': y += 1
	
	# print(res)
	# if r != R: raise
	# if b != B: raise
	# if y != Y: raise
	
	return res
	
import time
# raise
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	#Hd,Ad,Hk,Ak,B,D = map(int, next(input).split())
	N,R,O,Y,G,B,V = map(int, next(input).split())
	t0 = time.time()
	print(N,R,O,Y,G,B,V)
	res = solve(N,R,O,Y,G,B,V)
	print("Case #%d:"%case, res, file=output)
	print(time.time()-t0)
	sys.stdout.flush()
#'''

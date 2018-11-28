# coding: cp932
# coding: cp932
import sys
import math
f   = file(sys.argv[1])
out = file(sys.argv[2], 'w')

caseCnt = int(f.readline())

for case in range(1, caseCnt+1):
	R, T = map(int, f.readline().split())
	cnt = 0
	
	a = 2
	b = 2*R - 1
	c = T
	ans = int(2 * c / (b + math.sqrt(b**2 + 4 * c * a)))
	print>>out, 'Case #%d:'%case, ans
	#while (R+1)**2 - R**2 <= T:
	#	cnt += 1
	#	T -= (R+1)**2 - R**2
	#	R += 2
	
	#print cnt
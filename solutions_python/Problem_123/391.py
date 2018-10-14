# coding: cp932
import sys
import math
f   = file(sys.argv[1])
out = file(sys.argv[1][:-3] + '.out', 'w')

caseCnt = int(f.readline())

for case in range(1, caseCnt+1):
	A, N = map(int, f.readline().split())
	m    = map(int, f.readline().split())
	
	assert len(m) == N
	
	m.sort()
	
	op = 0
	ops = [N]
	try:
		for i, r in enumerate(m):
			op2 = 0
			while A <= r:
				A = 2 * A - 1
				op2 += 1
				if op2 >= N - i:
					op += op2
					raise StopIteration()
			op += op2
			
			A += r
			ops += [op + N - i - 1]
	except StopIteration:
		pass
		
	
	print>>out, 'Case #%d:'%case, min(ops + [op])
	
	#print op
	
	#a = 2
	#b = 2*R - 1
	#c = T
	#ans = int(2 * c / (b + math.sqrt(b**2 + 4 * c * a)))
	#print>>out, 'Case #%d:'%case, ans
	##while (R+1)**2 - R**2 <= T:
	##	cnt += 1
	##	T -= (R+1)**2 - R**2
	##	R += 2
	#
	##print cnt
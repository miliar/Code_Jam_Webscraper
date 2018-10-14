from math import ceil
from gmpy import is_square
def pal(n):
	return str(n)[::-1] == str(n)
		

T = int(raw_input())
count = 0

for _ in range(T):
	
	inp = raw_input().split()
	A = int(inp[0])
	B = int(inp[1])
	pals = 0
	sqa = pow(A,0.5)
	sqb = pow(B,0.5)
	
	#mm = sqb - int(sqb)
	#if mm > 0.0000000001:
	#if is_square(B):
	#	mm = 1
	#else:
	#	mm = 0

	for i in range(int(ceil(sqa)), int(sqb)+1):
		if pal(int(pow(i,2))) and pal(i):
			pals+=1
			#print i, pow(i,2)

	count += 1
	T -= 1
	print 'Case #'+str(count)+':', pals

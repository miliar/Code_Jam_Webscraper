import sys
#sys.stdin = open('B-large.in', 'r')
#sys.stdout = open('B.out','w')

T = int(input())
for p in range(T):
	C, F, X = map(float, input().split())
	D = 2
	S = 0
	while X / D > C/D + X / (D+F):
		S += C/D
		D += F
	S += X / D
	print("Case #%d: %.7f" % (p+1, S))
	

	

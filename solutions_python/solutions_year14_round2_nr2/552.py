import sys
sys.stdin = open('B-small-attempt0.in', 'r')
sys.stdout = open('B.out','w')

for p in range(int(input())):
	A, B, K = map(int, input().split())
	S = 0
	for i in range(A):
		for j in range(B):
			if i & j < K:
				S += 1
	print("Case #%d: %d" % (p+1, S))
	

	

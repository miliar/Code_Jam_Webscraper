T = int(input())
for I in range(1, T+1):
	a, b, k = input().split(" ")
	A, B, K = int(a), int(b), int(k)
	
	result = 0
	for i in range(0, A):
		for j in range(0, B):
			if (i & j < K):
				result += 1
	
	print("Case #%d: %d" % (I, result))
	
T = int(input())
for t in range(T):
	N, K = input().split()
	N = int(N)
	K = int(K)

	while K>0:
		if N % 2 == 1:
			N = (N-1)//2
			K -= 1
			K = int((K+1)/2)
			if K == 0:
				print("Case #" + str(t+1) + ": " + str(N) + " " + str(N))
		else:
			K -= 1
			if K % 2 == 1:
				N = int(N/2)
				K = int((K+1)/2)
			else:
				N = int(N/2)-1
				K = int(K/2)
			if K == 0:
				print("Case #" + str(t+1) + ": " + str(N+1) + " " + str(N))

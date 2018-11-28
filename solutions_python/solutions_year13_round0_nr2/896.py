with open('input.txt', 'r') as inFile, open('output.txt', 'w') as outFile:
	
	T = int(inFile.readline())
	for c in range (T):
		N, M = list(map(int, inFile.readline().strip().split()))
		A = []
		B = []
		for i in range (N):
			A.append(list(map(int, inFile.readline().strip().split())))
			for j in range (M):
				if not i:
					B.append([])
				B[j].append(A[i][j])
		ans = 'YES'
		for i in range (N):
			for j in range (M):
				if len(A[i]) != 1 and len(B[j]) != 1 and A[i][j] < max(max(A[i][:j], A[i][j + 1:])) and B[j][i] < max(max(B[j][:i], B[j][i + 1:])):
					ans = 'NO'
					break
			if ans == 'NO':
				break
		outFile.write('Case #{0}: {1}\n'.format(c + 1, ans))

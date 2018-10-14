T = int(input())

def to_base_k(n, k):
    s=[]
    while n > 0:
        s.append(str(n%k))
        n=n//k
    return ''.join(s[::-1])
	
for I in range(1, T+1):
	A, B = input().split(" ")
	M, N = int(A), int(B)
	S = ['']*M
	for i in range(0, M):
		S[i] = input()
	
	max, nMax = 0, 0
	
	for i in range(0, N**M):
		ser = ['']*N
		tries = ['']*N
		for j in range(0, N):
			tries[j] = set()
			ser[j] = []
		indices = to_base_k(i, N)
		indices = '0'*(M-len(indices)) + indices
###		print(indices)
		for j in range(0, M):
			ser[int(indices[j])].append(S[j])
###		print(ser)
		for j in range(0, len(ser)):
			for s in ser[j]:
				for k in range(0, len(s)+1):
					tries[j].add(s[:k])
###		print(tries)
		tot = 0
		for j in range(0, len(tries)):
			tot += len(tries[j])
		if tot > max:
			nMax = 1
			max = tot
		elif tot == max:
			nMax += 1
	
	result = nMax
	
	print("Case #%d: %s %s" % (I,max, result))

import gcj

def flips(B, i, K):
	for j in range(K):
		x = i + j
		if B[x] == 0:
			B[x] = 1
		else:
			B[x] = 0

def linear(B, N, K):
	f = 0
	for i in range(N - K + 1):
		#print(P, i)
		if B[i] == 0:
			flips(B, i, K)
			f += 1

	if min(B) != max(B):
		return -1
	return f

def flip (x, start, l):
	f = ((1 << l) - 1) << start
	#print("Flip ", bin(x), "with", bin(f), bin(x^f), l)
	return x ^ f

def dfs(x, N, K):
	M = [-1] * (1 << N)
	M[x] = 0
	Q = [x]
	while M[0] == -1 and len(Q) > 0:
		#print("Q = ", Q)
		s = Q.pop(0)
		for i in range(N - K + 1):
			xx = flip(s, i, K)
			if M[xx] == -1:
				M[xx] = M[s] + 1
				Q.append(xx)

	return M[0]



ifile, ofile = gcj.get_files('A')


T = int(ifile.readline().strip())
for t in range(T):
	fields = ifile.readline().split()
	P = fields[0]
	N = len(P)
	K = int(fields[1])
	x = 0
	B = [0] * N
	for p in P:
		x *= 2
		if p == '-':
			x += 1
	for i in range(N):
		if P[i] == '+':
			B[i] = 1
	#print(P,"->",x)

	#ans = dfs(x, N, K)
	ans = linear(B, N, K)
	#if attempt != ans:
	#	print("ALARMA", P, attempt, ans)

	if ans == -1:
		ans = "IMPOSSIBLE"
	else:
		ans = str(ans)
	
	gcj.print_answer(ofile, t, ans)
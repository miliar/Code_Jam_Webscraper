def check(N, i):
	for j in range(i, len(N)):
		if N[j] > N[i]: return False
		if N[j] < N[i]: return True
	return False

T = int(input())
for t in range(T):
	N = list(map(int, list(input())))
	M = list()
	if N[0] == 1 and check(N, 0):
		M = '9'*(len(N)-1)
	else:
		for i in range(len(N)):
			if check(N, i):
				M.append(str(N[i]-1))
				M.append('9'*len(N[i+1:]))
				break
			else:
				M.append(str(N[i]))
	print("Case #" + str(t+1) + ": " + ''.join(M)) 

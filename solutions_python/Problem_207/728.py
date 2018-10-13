def f(N, R, O, Y, G, B, V) :
	L = []
	D = {'R':R,'O':O,'Y':Y,'G':G,'B':B,'V':V}
	for key in D.keys() :
		if D[key] > N/2:
			return "IMPOSSIBLE"	
	most = -1
	for key in D.keys():
		if D[key] > most and D[key] > 0:
			K = key
			most = D[key]
	L.append(K)
	D[K] -= 1
	N -= 1			
	temp = 1
	while (N > 0) :
	#	print(L)
	#	print(D)
		most = -1
		for key in D.keys() :
			if D[key] > most and L[temp-1] != key and D[key] > 0:
				K = key
				most = D[key]
		L.append(K)
		D[K] -= 1
		temp += 1
		N -= 1
	if L[0] == L[-1] :
		L[-1], L[-2] = L[-2], L[-1]
		if L[-2] == L[-3] or L[0] == L[-1] :
			return "IMPOSSIBLE"
	if max(D.values()) > 0:
		return "IMPOSSIBLE"
	else :
		return "".join(L)
T = int(input())
for case in range (1, T+1):
	N, R, O, Y, G, B, V = tuple(map(int, input().split(" ")))
	result = f(N, R, O, Y, G, B, V)
	print("Case #", case, ": ", result, sep = "")
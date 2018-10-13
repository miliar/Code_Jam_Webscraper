def solve(N,X,S):
	S.sort()
	i = 0
	j = N-1
	discs = 0
	while i < j:
		if (S[i] + S[j] <= X):
			i+=1
			j-=1
		else:
			j-=1
		discs+=1
	if i == j:
		discs+=1
	return discs

T = int(raw_input())
for test in xrange(1,T+1):
	N, X = map(int, raw_input().split())
	S = map(int, raw_input().split())
	print "Case #" + str(test) + ": " + str(solve(N,X,S))
def pancake(S,K):
	S = list(S)
	cnt = 0
	for i in range(len(S)-K+1):
		if S[i] == "-":
			for j in range(K):
				S[i+j] = "+" if S[i+j] == "-" else "-"
			#print(S)
			cnt+=1
	if "-" in S:
		return "IMPOSSIBLE"
	else:
		return str(cnt)


T = int(input())
for t in range(1,T+1):
	iStr = input().split()
	S = iStr[0].strip()
	K = int(iStr[1])
	print("Case #"+str(t)+": "+pancake(S,K))
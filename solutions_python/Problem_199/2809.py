T = int(input())


for i in range(1,T+1):

	S, K = input().split(" ")
	K    = int(K)
	S    = list(S)
	count = 0

	if(S=="+"*len(S)):
		print("Case #"+str(i)+": 0")
	else:
		for j in range(0, len(S)-K+1):
			if S[j]=="-":
				count+=1
				for x in range(j, j+K):
					if(S[x]=="+"):
						S[x]="-"
					else:
						S[x]="+"
			else:
				continue
	if "-" in S:
		print("Case #"+str(i)+": IMPOSSIBLE")
	else:
		print("Case #"+str(i)+": "+str(count))



N=int(input())
for I in range(N):
	temp=input().split()
	count=0
	S=[True if i=="+" else False for i in temp[0]]
	K=int(temp[1])
	for i in range(len(S)-K+1):
		if not S[i]:
			count+=1
			for j in range(i,i+K):
				S[j]=not S[j]
		#print(S)
	print("Case #"+str(I+1)+": ",end="")
	if False in S:
		print("IMPOSSIBLE")
	else:
		print(count)
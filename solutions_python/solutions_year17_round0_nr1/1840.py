T=int(input())
t=1
while t<=T:
	S,K=input().split()
	K=int(K)
	maxlen=len(S)
	pos=S.find('-')
	flips=0
	while pos+1 and pos+K<=maxlen:
		i=0
		while i<K:
			S=list(S)
			if S[pos+i]=='+':
				S[pos+i]='-'
			else:
				S[pos+i]='+'
			i=i+1
		flips=flips+1
		S=''.join(S)
		# print(S)
		# print("flips: "+str(flips))
		# print("pos: "+str(pos))
		pos=S.find('-')
	if pos+1:
		print("Case #"+str(t)+": IMPOSSIBLE")
	else:
		print("Case #"+str(t)+": "+str(flips))
	t=t+1
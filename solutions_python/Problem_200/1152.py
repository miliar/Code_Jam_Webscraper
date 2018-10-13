def go():
	file=open("/home/yuxh/Desktop/b/B-large.in")
	T=int(file.readline()[:-1])
	for i in range(T):
		N=int(file.readline()[:-1])
		ans=str(magic(N))       	 
		print("case #"+str(i+1)+": "+ans)
	
def magic(N):
	S="0"+str(N)
	k=None
	for i in range(len(S)-1):
		if int(S[i])>int(S[i+1]):
			k=i
			break
	if not k:
		return N
	for i in range(k):
		if int(S[k-i])>int(S[k-i-1]):
			w=k-i
			break
	ans=S[:w]+str(int(S[w])-1)+"9"*(len(S)-w-1)
	return int(ans)
    
go()

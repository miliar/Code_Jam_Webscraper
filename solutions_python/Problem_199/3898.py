def flip(val):
	if val == '-':
		return '+'
	else:
		return '-'

T=int(input())
for z in range(0,T):
	S,K = map(str,input().split())
	S=list(S)
	K = int(K)
	n=0
	try:
		for i in range(0,len(S)):
			if S[i]=='-':
				for j in range(0,K):
					S[i+j] = flip(S[i+j])
				n+=1
				#print (S)
	except IndexError:
		print ("Case #"+str(z+1)+":"+" IMPOSSIBLE")
	else:
		print ("Case #"+str(z+1)+": "+str(n))
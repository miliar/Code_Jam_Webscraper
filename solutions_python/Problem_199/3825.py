def chng(x):
	for i,j in enumerate(x):
		if j=='-':
			x[i]='+'
		else:
			x[i]='-'
	return x
for i in xrange(1,input()+1):
	S,K=raw_input().split(' ')
	S=list(S)
	K=int(K)
	Som=0
	for j in xrange(len(S)-K+1):
		#print '#####'
		if S[j]=='-':
			#print S[j:j+K],
			S[j:j+K]=chng(S[j:j+K])
			#print S[j:j+K]
			Som+=1
	S=''.join(S) 
	#print S
	if S[-K:]=="+"*K:print "Case #%d: %d"%(i,Som)
	else: print "Case #%d: IMPOSSIBLE"%(i)
		
	
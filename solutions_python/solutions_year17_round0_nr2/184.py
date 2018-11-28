
T = int(raw_input())

def ans(S):
	if sorted(S)==list(S) : return S
	i=0
	while S[i]==S[i+1] : i+=1
	if S[i]<S[i+1] : return S[:i+1] + ans(S[i+1:])
	else : 
		if S[0]=='1' : return '9'*(len(S)-1)
		return str(int(S[0])-1) + '9'*(len(S)-1)
		
for test in xrange(1, T+1):
	print "Case #%d: %s"%(test, ans(raw_input()))



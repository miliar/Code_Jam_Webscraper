def solve(x,s,S,M,D):
	#print '#',x,s,D
	if x not in M: M[x]=s
	elif M[x]>=s: return False
	if S[x][0]+s>=D:
		#print x,s
		return True
	if s<=0: return False
	#print range(x+1,len(S))
	sy=[y for y in range(x+1,len(S)) if S[x][0]+s>=S[y][0]]
	for y in reversed(sorted(sy)):
		if solve(y,min(S[y][1],S[y][0]-S[x][0]),S,M,D): return True
	return False
for T in range(input()):
	S=[map(int, raw_input().split()) for N in range(input())]
	D=input()
	M={}
	#print S,D
	y=solve(0,S[0][0],S,M,D)
	if y: y='YES'
	else: y='NO'
	print "Case #%d: %s" % (T+1,y)
	

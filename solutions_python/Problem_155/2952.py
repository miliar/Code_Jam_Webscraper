
N=int(raw_input())
for case in range(1,N+1):
	tokens=raw_input().split()
	Smax=int(tokens[0])
	S=map(int,list(tokens[1]))
	d=0
	standing=S[0]
	for i in range(1,Smax+1):
		if i>standing and S[i]>0:
			d += i-standing
			standing += i-standing
		standing += S[i]		
	print "Case #{0}: {1}".format(case, d)

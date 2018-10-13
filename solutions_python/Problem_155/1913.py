T=int(raw_input())
for z in xrange(T):
	S,V=raw_input().split();S=int(S)
	e=0;su=0
	for i in xrange(S):
		su+=int(V[i])
		if su<i+1: e+=1+i-su;su=i+1
	print "Case #%d: %d"%(z+1,e)


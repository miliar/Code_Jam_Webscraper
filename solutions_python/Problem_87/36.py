for test in range(input()):
	X,S,R,t,N = map(int,raw_input().split())
	t = float(t)
	B = [0]*N
	E = [0]*N
	w = [0]*N
	for i in range(N):
		B[i],E[i],w[i] = map(int,raw_input().split())
	seg = []
	p = 0
	for i in range(N):
		if B[i]>p:
			seg += [(0,B[i]-p)]
			p = B[i]
		seg += [(w[i],E[i]-p)]
		p = E[i]
	if (X>p):
		seg += [(0,X-p)]
	
	seg.sort()
	
	ans = 0
	for w,l in seg:
		rt = min(t,float(l)/(w+R))
		ans += rt + (l-rt*(w+R))/(w+S)
		t -= rt
	
	print "Case #%d: %.20f" % (test+1,ans)

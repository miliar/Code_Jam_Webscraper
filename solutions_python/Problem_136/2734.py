T=int(input())
for t in range(1,T+1):
	(C,F,X)=map(float,raw_input().split())
	s = 0.0
	n = 0
	dmin = X/2
	while True:
		n = n+1
		s = s + 1/(2+(n-1)*F)
		d = C*s + X/(2+n*F)
		if d > dmin:
			break
		dmin = d
	print("Case #%d: %.7f" % (t, dmin))
for case in range(1, int(input())+1):
	(MK,N) = list(map(int,input().split()))
	d = dict()
	for i in range(N):
		(K,S) = list(map(int,input().split()))
		d[K]=S
	mt = 0
	for k in sorted(d):
		ct = (MK - k) / d[k]
		if (ct > mt):
			mt = ct
	result = MK / mt
		

		
	print ("Case #%d: %s" % (case,result))

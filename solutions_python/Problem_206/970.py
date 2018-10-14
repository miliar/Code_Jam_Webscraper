for i in range(int(input())):
	D, N = map(int,input().split())
	mx = 0
	for _ in range(N):
		pl, v = map(int,input().split())
		mx = max(mx,(D-pl)/v)
	print('Case #' + str(i+1) + ':',D/mx)

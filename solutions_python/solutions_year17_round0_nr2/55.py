T = int(raw_input())

for t in range(T):
	N = int(raw_input())
	ans = 0
	
	x = [0] * 20
	x[0] = 1
	for i in range(19):
		x[i+1] = x[i] * 10 + 1
	
	cnt = 0
	for i in range(20):
		while cnt < 9 and ans + x[19-i] <= N:
			ans = ans + x[19-i]
			cnt = cnt + 1
	
	print 'Case #' + str(t+1) + ': ' + str(ans)

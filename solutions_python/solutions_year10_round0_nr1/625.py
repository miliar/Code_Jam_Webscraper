T = int(raw_input())
for case in range(1, T+1):
	N, K = map(int, raw_input().split())
	twoN = 2**N
	
	if K % twoN == twoN - 1:
		state = 'ON'
	else:
		state = 'OFF'
	
	print 'Case #' + str(case) + ': ' + state

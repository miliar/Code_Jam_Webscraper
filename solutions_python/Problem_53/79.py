
N = int(raw_input())

for i in range(1, N+1):
	N, K = tuple(map(lambda x : int(x), raw_input().split()))
	tt_switch = 2**N - 1
	
	if K < tt_switch:
		on = False
	else:
		on = (K - tt_switch) % (tt_switch + 1) == 0
		
	print 'Case #%d: %s' % (i, 'ON' if on else 'OFF')
	
	
	

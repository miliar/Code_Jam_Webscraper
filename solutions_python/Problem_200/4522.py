
T = int(raw_input())

def check_if_tidy(N):
	digits = [int(i) for i in str(N)]
	prev = 0
	for k in digits:
		if k < prev:
			return False
		else:
			prev = k
	return True

index = 1

for _ in xrange(0, T):
	N = int(raw_input())
	if N<10:
		print 'Case #%d: %d' % (index, N)
	else:
		while True:
			
			if check_if_tidy(N):
				print 'Case #%d: %d' % (index, N)				
				break
			N -= 1
	index += 1
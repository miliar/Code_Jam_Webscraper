from sys import stdin

# sum is xor
			
T = int(stdin.readline())
for ti in xrange(1, T + 1):
	N = int(stdin.readline())
	arr = [int(x) for x in stdin.readline().split()]
	ans = 0
	for x in range(2**N):
		sean_sum = 0
		sean = 0
		patrick = 0
		sean_size = 0
		for i in range(N):
			if x & (1 << i):
				sean ^= arr[i]
				sean_sum += arr[i]
				sean_size += 1
			else:
				patrick ^= arr[i]
		if sean == patrick and sean_size != N and sean_size != 0 and sean_sum > ans:
			ans = sean_sum		
	if ans == 0:
		ans = 'NO'
	print 'Case #' + str(ti) + ': ' + str(ans)
	


import math

T = int(raw_input())

for case in range(1, T+1):
	L, P, C = map(int, raw_input().split())
	n = 1

	# Use a loop because, in the worst case, there are ~30 iterations for 10^9
	
	n = math.ceil(max(math.log(float(P)/L, C) - 1, 0))

	print 'Case #' + str(case) + ': ' + str(int(math.ceil(math.log(n+1, 2))))


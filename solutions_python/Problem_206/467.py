T = int(input())

for t in range(1, T + 1):
	D, N = [int(s) for s in input().split(" ")]
	
	max_time = 0
	for n in range(1, N + 1):
		K, S = [int(s) for s in input().split(" ")]
		time = (D - K) / S
		max_time = max(max_time, time)
	
	print("Case #{}: {}".format(t, D / max_time))
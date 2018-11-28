t = int(input())

for case in range(1, t + 1):
	D, N = map(int, input().split(" "))
	H = []
	for i in range(N):
		H.append(tuple(map(int, input().split(" "))))

	max_time = 0

	for h in H:
		time = (D - h[0]) / h[1]
		max_time = max(max_time, time)

	print("Case #%d: %.6f" % (case, D / max_time))
def find_max_speed(d, arr):
	max_t = -1
	for elem in arr:
		k = elem[0]
		s = elem[1]
		dist = d - k
		t = float(dist) / s
		if t > max_t:
			max_t = t
	return float(d)/max_t


t = int(input())
for i in range(1, t + 1):
	arr = list()
	d, n = [int(a) for a in raw_input().split(" ")]
	for j in range(n):
		k, s = [int(a) for a in raw_input().split(" ")]
		arr.append((k, s))

	print("Case #{}: {}".format(i, find_max_speed(d, arr)))
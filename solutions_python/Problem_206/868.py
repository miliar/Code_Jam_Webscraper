
t = int(input())

for i in range(1, t + 1):
	n, m = [int(s) for s in input().split(" ")]
	
	h = []
	for s in range(m):
		h.append([int(s) for s in input().split(" ")]);
	h = [(n - a[0]) / a[1] for a in h]
	h = n / max(h)
	
	print("Case #{}: {:.6f}".format(i, h))


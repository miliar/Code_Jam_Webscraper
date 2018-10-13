t = int(input())
for c in range(t):
	n = [int(x) for x in input()]
	size = len(n)
	
	i = 0
	last = n[0]
	while i < size:
		if n[i] < last:
			last = n[i]
			break
		last = n[i]
		i += 1
	if i < size:
		i -= 1
		while i > 0:
			if n[i]-1 >= n[i-1]:
				break
			i -= 1
		n[i] -= 1
		for j in range(i+1, size):
			n[j] = 9

	print("Case #%d: " % (c+1), end="")
	leadZ = True
	for k in n:
		if k != 0:
			leadZ = False
		if not leadZ:
			print(k, end="")
	print()

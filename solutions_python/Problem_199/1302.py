nc = int(input())
for i in range(nc):
	pancakes, size = [s for s in input().split()]
	size = int(size)
	pancakes = list(pancakes)
	counter = 0
	for k in range(0, len(pancakes) - size + 1):
		if pancakes[k] == "-":
			counter += 1
			for idx in range(k,k+size):
				pancakes[idx] = "+" if pancakes[idx] == "-" else "-"
	for s in pancakes:
		if s == "-":
			counter = -1
	print("Case #{}: {}".format(i+1, counter if counter != -1 else "IMPOSSIBLE"))


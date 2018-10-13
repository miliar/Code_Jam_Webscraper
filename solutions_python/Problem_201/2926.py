

def find_stall():
	minim = 0
	maxim = 0
	index_best = -1
	# print("\n")
	# print(stalls)
	for i in range(n+1):
		if stalls[i] == 1:
			continue
		delta_i, delta_d = 0, 0
		for j in reversed(range(1, i)):
			# print(j)
			if stalls[j] == 0:
				delta_i += 1
			else:
				break
		for j in range(i+1, n+1):
			if stalls[j] == 0:
				delta_d += 1
			else:
				break
		aux1 = min(delta_i, delta_d)
		aux2 = max(delta_i, delta_d)
		if aux1 > minim:
			index_best = i
			minim = aux1
			maxim = aux2
		elif aux1 == minim:
			if aux2 > maxim:
				index_best = i
				minim = aux1
				maxim = aux2
	# print("Index best: {}".format(index_best))
	stalls[index_best] = 1
	# print(stalls)
	return minim, maxim


T = int(input())
for t in range(1, T+1):
	# print("*"*40)
	line = input().split(" ")
	n, k = int(line[0]), int(line[1])
	stalls = [1] + [0]*n + [1]
	for _ in range(k):
		a, b  = find_stall()
	print("Case #{}: {} {}".format(t, b, a))

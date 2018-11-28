nb_cases = int(input())
for i in range(nb_cases):
	n, k = [int(s) for s in input().split()]
	partitions = [[0,n+1]]
	for a in range(k):
		newp = []
		bestp = 0
		bestmin = -1
		bestmax = -1
		bestsplit = -1
		for pidx in range(len(partitions)):
			p = partitions[pidx]
			if (p[1] - p[0] == 1):
				continue
			middle = int(p[0] + int((p[1]-p[0])/2))
			pmin = min(middle-p[0]-1, p[1]-middle-1)
			pmax = max(middle-p[0]-1, p[1]-middle-1)
			if pmin > bestmin or (pmin == bestmin and pmax > bestmax):
				bestmin = pmin
				bestmax = pmax
				bestp = pidx
				bestsplit = middle
		for pidx in range(len(partitions)):
			if pidx != bestp:
				newp.append(partitions[pidx])
			else:
				newp.append([partitions[pidx][0], bestsplit])
				newp.append([bestsplit, partitions[pidx][1]])
		if a == k-1:
			print("Case #{}: {} {}".format(i+1, bestmax, bestmin))
		else:
			partitions = newp
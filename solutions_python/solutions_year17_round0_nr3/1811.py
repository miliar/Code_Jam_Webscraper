#skleton
T = int(input())
for t in range(T):
	line = input().split(' ')
	N = int(line[0])
	K = int(line[1])

	occupied = [False for x in range(N)]
	Ls = [x for x in range(N)]
	Rs = [y for y in range(N-1, -1, -1)]
	min_LR = [min(Ls[x], Rs[x]) for x in range(N)]
	max_LR = [max(Ls[x], Rs[x]) for x in range(N)]
	min_val = 0

	for k in range(K):
		min_val_pos = min_LR.index(max(min_LR))
		candidate = [min_val_pos]
		for q in range(N):
			if(min_LR[q] == min_LR[min_val_pos]):
				candidate.append(q)
		for q in range(1, len(candidate)):
			if(max_LR[min_val_pos] < max_LR[candidate[q]]):
				min_val_pos = candidate[q]

		min_val = min_val_pos

		if(k == K-1):
			print("Case #{0}: {1} {2}".format(t+1, max_LR[min_val], min_LR[min_val]))
			break
		
		tmp = min_val
		while((not occupied[tmp]) and (tmp > 0)):
			tmp -= 1

		L_pos = tmp
		
		tmp = min_val
		while(tmp < N and occupied[tmp] == False):
			tmp += 1
		
		R_pos = tmp

		for x in range(L_pos, min_val):
			Rs[x] = min(Rs[x],(min_val-x-1))
		for x in range(min_val+1, R_pos):
			Ls[x] = min(Ls[x], (x-min_val-1))

		Ls[min_val] = 0
		Rs[min_val] = 0

		min_LR = [min(Ls[x], Rs[x]) for x in range(N)]
		max_LR = [max(Ls[x], Rs[x]) for x in range(N)]

		occupied[min_val] = True
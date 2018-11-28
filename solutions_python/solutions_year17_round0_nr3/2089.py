def insert(free):
	nfree = sorted(free)[-1]
	nseg = free[nfree]
	if nseg == 1:
		del free[nfree]
	else:
		free[nfree] -= 1
	n2 = int(nfree/2)
	if nfree % 2:
		if not n2 in free:
			free[n2] = 2
		else:
			free[n2] += 2
		return n2, n2
	else:
		if not n2 in free:
			free[n2] = 1
		else:
			free[n2] += 1
		if not n2-1 in free:
			free[n2-1] = 1
		else:
			free[n2-1] += 1
		return n2, n2-1
t = int(input())
for i in range(1, t + 1):
	n = input().split(" ")
	k = (int(n[1]))
	n = (int(n[0]))
	free = {n:1}
	for j in range(k):
		ls, rs = insert(free);
	print("Case #{}: {} {}".format(i, ls, rs))

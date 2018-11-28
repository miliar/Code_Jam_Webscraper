with open('input.in') as f:
	t = int(f.readline())
	for i in range(t):
		a1 = int(f.readline()) - 1
		b1 = []
		for j in range(4): b1.append(map(int,f.readline().split()))
		a2 = int(f.readline()) - 1
		b2 = []
		for j in range(4): b2.append(map(int,f.readline().split()))
		ans = list(set(b1[a1]) & set(b2[a2]))
		if len(ans) == 1:
			print("Case #{}: {}".format(i+1,ans[0]))
		elif len(ans) == 0:
			print("Case #{}: Volunteer cheated!".format(i+1))
		else:
			print("Case #{}: Bad magician!".format(i+1))



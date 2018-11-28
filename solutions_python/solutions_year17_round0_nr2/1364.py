T = int(input())

for j in range(T):
	N = int(input())
	d = list(map(int,str(N)))

	# d[i] < d[i-1]
	# d[i-1] - 1, d[i+k] = 9 for all k > 0

	for i in reversed(range(1, len(d))):
		if d[i] < d[i-1]:
			d[i-1] -= 1
			for k in range(i, len(d)):
				d[k] = 9


	ans = int("".join(map(str,d)))
	print("Case #" + str(j+1) + ": " + str(ans))
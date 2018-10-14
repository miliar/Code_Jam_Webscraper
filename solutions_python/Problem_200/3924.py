T = int(input())
for t in range(1, T + 1):
	N = int(input())
	n = list(reversed([int(s) for s in str(N)]))
	modified = False
	for i in range(len(n) - 1):
		if n[i] < n[i+1] or (n[i] == n[i+1] and n[i] == 0):
			n[i] = 9
			n[i+1] = 9 if n[i+1] == 0 else n[i+1] - 1
			modified = True
	if modified:
		n[0] = 9
	result = int(''.join(list(reversed([str(x) for x in n]))))
	print("Case #{}: {}".format(t, result))
for t in range(int(input())):
	N = list(input())
	r = len(N)
	for i in range(len(N)-1, 0, -1):
		if N[i-1] > N[i]:
			N[i-1] = chr(ord(N[i-1])-1) # N[i-1]--
			r = i
	l = (N[0] == '0')
	result = ''.join(N[l:r] + ['9'] * (len(N)-r))
	print("Case #{}: {}".format(t + 1, result))
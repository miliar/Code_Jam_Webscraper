T = input()
for i in range(1,T+1):
	M = raw_input().split()
	N = list(M[0])
	ans = [0] * len(N)
	for j in range(len(N)):
		ans[j] = ord(N[j]) - ord('0')
	for j in range(len(N)-1):
		k = len(N) - j - 1
		if ans[k] < ans[k-1]:
			ans[k] = 9
			ans[k-1] -= 1
	for j in range(len(N)-1):
		if ans[j] > ans[j+1]:
			for k in range(j+1,len(N)):
				ans[k] = 9
	print "Case #%d:"%i,
	counter = 0
	for j in range(len(N)):
		if ans[j] == 0:
			counter += 1
		else:
			break
	print ''.join(str(ans[i]) for i in range(counter,len(ans)))
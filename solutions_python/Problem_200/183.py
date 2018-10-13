TC = int(input())
for tc in range(TC):
	N = input()
	ans = ""
	for i, x in enumerate(N):
		if i == len(N)-1 or int(N[i+1:]) >= int(N[i] * (len(N)-i-1)):
			ans += N[i]
		else:
			ans += '%d%s' % (int(N[i])-1, '9' * (len(N)-i-1))
			break
	print('Case #%d: %d' % (tc+1, int(ans)))

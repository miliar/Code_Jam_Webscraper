def func(n, s):
	ans = 0
	tmp = 0
	for i in range(n):
		tmp = tmp + 1 - int(s[i])
		ans = max(ans, tmp)
	return ans
	
T = int(raw_input())

for t in range(T):
	n, s = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' + str(func(int(n), s))

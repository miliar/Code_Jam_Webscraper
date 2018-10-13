def func():
	r = int(raw_input())
	ans = [0] * 17
	
	for i in range(4):
		a = map(int, raw_input().split(' '))
		if i == r-1:
			for x in a:
				ans[x] = 1
	
	return ans

T = int(raw_input())

for t in range(T):
	a = func()
	b = func()
	
	cnt = 0
	ans = 0
	for i in range(1, 17):
		if a[i] == 1 and b[i] == 1:
			cnt += 1
			ans = i
	
	if cnt == 0:
		print 'Case #' + str(t+1) + ': ' + 'Volunteer cheated!'
	elif cnt >= 2:
		print 'Case #' + str(t+1) + ': ' + 'Bad magician!'
	else:
		print 'Case #' + str(t+1) + ': ' + str(ans)

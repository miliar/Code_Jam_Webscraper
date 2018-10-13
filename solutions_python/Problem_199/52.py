tn = int(raw_input())

for tt in range(1, tn + 1):
	tmp = raw_input().split()
	a = list(tmp[0])
	n = len(a)
	k = int(tmp[1])
	ans = 0
	for i in range(n):
		if a[i] == '-':
			if i > n - k: ans = -1
			else:
				for j in range(i, i + k):
					a[j] = '+' if a[j] == '-' else '-'
				ans += 1
	print "Case #%d:" % tt,
	if ans == -1:
		print "IMPOSSIBLE"
	else:
		print ans
	
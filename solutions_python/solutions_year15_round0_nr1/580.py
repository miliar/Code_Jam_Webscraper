t = int(input())
for i in range(t):
	s, m = input().split()
	s = int(s)
	a = list(map(int, m))
	res = 0
	cur = a[0]
	for j in range(s):
		if a[j+1] > 0 and cur + res < j + 1:
			res = j + 1 - cur
		cur += a[j+1]
	print('Case #%d: %d' % (i + 1, res))
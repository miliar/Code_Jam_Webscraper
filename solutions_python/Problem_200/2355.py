t = int(input())
for i in range(t):
	n = list(input())
	d = len(n)
	mark = d
	for j in range(d - 1, 0, -1):
		if int(n[j - 1]) > int(n[j]):
			n[j - 1] = chr(ord(n[j - 1]) - 1)
			mark = j
	for j in range(mark, d):
		n[j] = 9
	print('Case #%d:' % (i + 1), int(''.join(map(str, n))))

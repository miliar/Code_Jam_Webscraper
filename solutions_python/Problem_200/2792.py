T = int(input())
for t in range(T):
	n = input()
	n = [x for x in n]
	found = -1
	for i, c in enumerate(n):
		if i > 0 and c < n[i - 1]:
			found = i
			break
	if found >= 0:
		delta = 1
		for i in range(found-1, -1, -1):
			n[i] = chr(ord(n[i]) - delta)
			delta = 0
			if n[i] < '0' or (i > 0 and n[i]<n[i-1]):
				n[i] = '9'
				delta = 1
		n[found:] = ['9' for c in n[found:]]
		start = 0
		for i, c in enumerate(n):
			if c != '0':
				start = i
				break
		result = ''.join(n[start:])

	else:
		result = ''.join(n)

	print('Case #%s: %s' % (t+1, result))


t = int(raw_input())
for x in range(1, t + 1):
	r, c = map(int, raw_input().split(' '))
	cake = [None] * r
	cur = '?'
	for i in range(r):
		cur = '?'
		cake[i] = list(raw_input())
		for j in range(c):
			if cake[i][j] != '?':
				cur = cake[i][j]
				break
		if cur != '?':
			for j in range(c):
				if cake[i][j] == '?':
					cake[i][j] = cur
				else:
					cur = cake[i][j]
	for i in range(r):
		if cake[i][0] == '?':
			for j in range(c):
				cur = '?'
				k = 0
				while i + k < r:
					if cake[i + k][j] != '?':
						cur = cake[i + k][j]
						break
					k += 1
				if cur != '?':
					while k > 0:
						k -= 1
						cake[i + k][j] = cur
				if cake[i][j] == '?':
					k = 0
					while i - k >= 0:
						if cake[i - k][j] != '?':
							cur = cake[i - k][j]
							break
						k += 1
					if cur != '?':
						while k >= 0:
							cake[i - k][j] = cur
							k -= 1
	print("Case #%d:"%(x))
	for i in range(r):
		print(''.join(cake[i]))

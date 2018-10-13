t = int(input())

for case in range(1,t+1):
	a0, a1 = [int(x) for x in input().split()]
	arr = []
	for i in range(a0+a1):
		p = [int(x) for x in input().split()]
		arr.append((p, 0 if i < a0 else 1))

	arr = sorted(arr)

	ans = 0
	coda = [720,720]
	rest = [[],[]]

	for i in range(len(arr)):
		if arr[i][1] != arr[i-1][1]:
			ans += 1
		else:
			tmp = arr[i][0][0]-arr[i-1][0][1]
			tmp = tmp if tmp >= 0 else tmp + 1440
			rest[arr[i][1]].append(tmp)
		coda[arr[i][1]] -= arr[i][0][1] - arr[i][0][0]

	rest[0] = sorted(rest[0])
	rest[1] = sorted(rest[1])
	for i in range(2):
		can_do = len(rest[i])
		for j in range(len(rest[i])):
			coda[i] -= rest[i][j]
			if coda[i] < 0:
				can_do = j
				break
		ans += (len(rest[i])-can_do)*2

	print('Case #%d: %d' % (case, ans))

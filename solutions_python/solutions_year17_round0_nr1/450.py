t = int(input())

for c in range(t):
	pstr, k = input().split()
	k = int(k)
	size = len(pstr)
	pstr = [a == "+" for a in pstr]

	i = 0
	flips = 0
	while i <= size-k:
		if not pstr[i]:
			flips += 1
			for j in range(i, i+k):
				pstr[j] = not pstr[j]
		i += 1
	
	print("Case #%d: " % (c+1), end="")
	ok = True
	for x in range(size-k, size):
		if not pstr[x]:
			print("IMPOSSIBLE")
			ok = False
			break
	if ok:
		print(flips)


T = int(raw_input())



for i in range(T):
	
	inp = raw_input().split()
	pancks = list(inp[0])
	chunck = int(inp[1])
	

	l = len(pancks)
	# print l
	# print range(l- 2)

	cnt = 0

	for idx in range(l - chunck + 1):
		if pancks[idx] == '+':
			continue

		cnt += 1
		for j in range(idx, idx + chunck):
			if pancks[j] == '+':
				pancks[j] = '-'
			else:
				pancks[j] = '+'



	result = str(cnt)
	if '-' in pancks:
		result = "IMPOSSIBLE"
	print "Case #" + str(i+1) + ": " + result

T = int(input())
for tc in range(1, T+1):
	n = [int(x) for x in input()]
	n.reverse()
	h = 9
	for i in range(len(n)):
		if i+1 < len(n) and n[i] < n[i+1]:
			for j in range(0,i+1):
				n[j] = h
			n[i+1] = n[i+1] - 1

	n = [str(x) for x in n]
	n = int(''.join(reversed(n)))
	print('Case #{0}: {1}'.format(str(tc), str(n)))



cases = int(input())

for tc in range(cases):
	a = input().split(" ")
	w = int(a[1])
	b = list()
	for i in a[0]:
		b.append(i)
	k = 0
	for ci in range(0, len(a[0])-w+1):
		if b[ci] == '-':
			k += 1
			for fi in range(ci, ci+w):
				if b[fi] == '-': b[fi] = '+'
				else: b[fi] = '-'
			#print(b)
	
	if '-' in b: print('Case #' + str(tc+1) + ': IMPOSSIBLE')
	else: print('Case #' + str(tc+1) + ': ' + str(k))
	
Cases = int(input())
Colors = "ROYGBV"

for Case in range(Cases):
	x = list(map(int,input().split()))
	x = x[1:]
	n = sum(x)
	# print(x)

	r,y,b = x[0], x[2], x[4]

	Z = [(r,'R'),(y,'Y'),(b,'B')]
	Z.sort(reverse=True)

	bad = False
	if 2*Z[0][0] > n:
		bad = True
	else:
		seq = ['?']*n
		fr = 0
		for i in range(Z[0][0]):
			seq[2*i] = Z[0][1]
			fr = (2*i)%n
		for j in range(Z[1][0]):
			while seq[fr] != '?':
				fr += 1
				fr %= n
			seq[fr] = Z[1][1]
			fr += 2
			fr %= n

		for k in range(Z[2][0]):
			while(seq[fr] != '?'):
				fr += 1
				fr %= n
			seq[fr] = Z[2][1]

	ans = ''.join(seq)

	if bad:
		print('Case #%d: IMPOSSIBLE' % (Case+1))
	else:
		print('Case #%d: %s' % (Case+1, ans))
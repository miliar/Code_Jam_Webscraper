cases = int(input())

res = []
for ii in range(cases):
	s, move = input().split(' ')
	move = int(move)
	s = list(s)
	tmp = 0
	while True:
		try:
			s=s[s.index('-'):]
			if len(s)<move:
				#print('impossible')
				res.append((ii+1, 'IMPOSSIBLE'))
				break
		except ValueError:
			res.append((ii+1, tmp))
			#print('ok')
			#print(ii+1, tmp)
			break

		tmp+=1
		for i, _ in enumerate(s):
			if s[i]=='-':
				s[i]='+'
			else:
				s[i]='-'
			#print(s, s[i], i, tmp)
			if i==move-1:
				break
		
	#res.append((ii+1, tmp))


for el in res:
	print('Case #',el[0],': ', el[1], sep='')
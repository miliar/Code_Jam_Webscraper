fo = open('result_big.txt','w')
with open('A-large.in.txt') as f:
	lines = f.readlines()
	for i,line in enumerate(lines[1:]):
		s,k = line.strip().split(' ')
		k = int(k)
		c=0
		s = list(s)
		l = len(s)
		count = 0
		while c<l:
			if s[c]=='-':
				if c+k<=l:
					# print
					# print s
					for _ in range(c,c+k):
						s[_] = '-' if s[_]=='+' else '+'
					# print s
					count+=1
				else:
					count = -1
					break
			c+=1
		res = str(count) if count>=0 else 'IMPOSSIBLE'
		fo.write('Case #{}: {}\n'.format(i+1, res))

fo.close()
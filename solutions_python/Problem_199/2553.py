def countmin(st, k):	
	st = list(st)
	flip=lambda x:'-'if x=='+'else'+'
	l = len(st);c=0
	if k > len(st):
		return 'IMPOSSIBLE'
	for i in range(l-k+1):					
		if st[i] == '-':
			c+=1
			for j in range(i, i+k):
				st[j] = flip(st[j])
	jnd = ''.join(st[l-k:])		
	if (jnd == '+'*k):							
		return c			
	else:
		return 'IMPOSSIBLE'	

if __name__ == '__main__':
	f = open('out.out', 'w')
	with open('A-large.in', 'r') as fle:
		r = fle.readlines()
		t = int(r[0][:-1])
		for i in range(1, t+1):					
			st, k = r[i].split(' ')
			k = int(k[:-1])
			f.write('Case #' + str(i) + ': '+ str(countmin(st, k)) + '\n')			
			# print st, k, countmin(st, k)

		f.close()	 
		
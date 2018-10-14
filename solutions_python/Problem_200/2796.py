 
T = int(raw_input())
for t in range(1,T+1):
	a = [int(_) for _ in raw_input()]
	b = [0]*len(a)

	m = a[0]

	flag = False

	for i in range(len(a)):
		
		if a[i] >= m:
			m = a[i]
			b[i] = m
		else:
			j=i-1
			while j>=0 and b[j]==m:
				b[j] = m-1
				i = j+1
				j -= 1
			flag = True	
			break

	if flag is True:
		for j in range(i,len(a)):
			b[j] = 9		

	# i=0
	# while b[i]==0:
	# 	i += 1

	if b[0]==0:
		b = b[1:]

	if b[0]==0:
		for i in range(len(b)):
			b[i] = 9

	print 'Case #%d: %s'%(t,''.join(map(str,b)))


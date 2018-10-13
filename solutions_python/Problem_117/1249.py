def solve_problem(N,M,a):
	for i in range(N*M):
		j= i/M*M
		for k in range(M):
			if a[j+k] > a[i]:
				l= i-M
				while l >= 0:
					if a[l] > a[i]:
						return 'NO'
					l-= M
				l= i+M
				while l < N*M:
					if a[l] > a[i]:
						return 'NO'
					l+= M
				break
	return 'YES'
		
file= open('lawnmower.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
j= 0
for i in range(1,T+1):
	j+= 1
	line= input[j].split(' ')
	N= int(line[0])
	M= int(line[1])
	a= []
	for n in range(N):
		j+= 1
		b= input[j].split(' ')
		for m in range(M):
			a.append(int(b[m]))
	print 'Case #' + str(i)	+ ': ' + solve_problem(N,M,a)

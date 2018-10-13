f = open('A-large.in.txt','r')
g = open('output.txt', 'w')

C = int(f.readline())

for i in range(C):
	count = 0
	A, N = f.readline().strip().split()
	A = int(A)
	N = f.readline().strip().split()
	for j in range(len(N)):
		N[j] = int(N[j])
	N.sort() 
	for j in range(len(N)):
		prevcount = count
		oldA = A
		breakcheck = 0
		if A > N[j]:
			A += N[j]
		else:
			while A <= N[j]:
				A += A - 1
				count += 1
				if count - prevcount >= len(N) - j:
					count = prevcount + 1
					A = oldA
					breakcheck = 1
					break
			if breakcheck == 0:
				A += N[j]
			else:
				breakcheck = 0
	if count > len(N):
		count = len(N)
	g.write('Case #%d: %d\n' % (i+1,count))
	
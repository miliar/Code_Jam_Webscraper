def solve_problem(a1,a2,rows1,rows2):
	c= 0
	for n in rows1[a1-1]:
		if n in rows2[a2-1]:
			c+= 1
			m= n
	if c==0: 
		return 'Volunteer cheated!'
	if c>1:
		return 'Bad magician!'
	return m

file= open('magic_trick.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
for i in range(T):
	a1= int(input[i*10+1])
	a2= int(input[i*10+6])
	rows1= []
	for j in range(2,6):
		rows1.append(input[i*10+j].split())
	rows2= []
	for j in range(7,11):
		rows2.append(input[i*10+j].split())
	print 'Case #' + str(i+1)	+ ': ' + solve_problem(a1,a2,rows1,rows2)

def solve_problem(C,F,X):
	f= 2.0
	t= 0
	while X/f > X/(f+F) + C/f:
		t+= C/f
		f+= F
	return t + X/f

file= open('cookie_clicker_alpha.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
for i in range(1,T+1):
	input[i]= input[i].split()
	C= float(input[i][0])
	F= float(input[i][1])
	X= float(input[i][2])
	print 'Case #' + str(i)	+ ': ' + str(solve_problem(C,F,X))

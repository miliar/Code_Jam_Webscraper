import math

def solve_problem(r,t):
	n = (int(math.sqrt((2*r - 1)*(2*r - 1) + 8*t)) - 2*r + 1)/4
	if n*(2*r + 1) + 2*n*(n - 1) > t:
		n-= 1
	return str(n)

file= open('bullseye.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
for i in range(1,T+1):
	line= input[i].split(' ')
	r= int(line[0])
	t= int(line[1])
	print 'Case #' + str(i)	+ ': ' + solve_problem(r,t)
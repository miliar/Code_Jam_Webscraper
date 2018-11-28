
def solve_problem(S_max, s):
	n= 0
	m= int(s[0])
	for k in range(1, S_max+1):
		s_k= int(s[k])
		if s_k and k > m:
			n+= k - m
			m= k
		m+= s_k
	return n 

file= open('standing_ovation.in')
input= file.read().split('\n')
file.close()

T= int(input[0])
for i in range(1, T+1):
	line= input[i].split(' ')
	S_max= int(line[0])
	s= line[1]
	print 'Case #' + str(i)	+ ': ' + str(solve_problem(S_max, s))
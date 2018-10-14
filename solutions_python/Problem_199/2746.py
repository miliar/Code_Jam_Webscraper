
def solution(S, K):
	l= len(S)
	s= list(S)
	n= 0
	for i in range(l):
		if s[i] == '-' and i + K > l:
			return 'IMPOSSIBLE'
		elif s[i] == '-':
			n+= 1
			for j in range(K):
				if s[i + j] == '-':
					s[i + j]= '+'
				else:
					s[i + j]= '-'
	return str(n)

file= open( __file__.split('.')[0]+'.in')
lines= file.read().split('\n')
file.close()

T= int(lines[0])
for i in range(1, T + 1):
	parts = lines[i].split()
	S= parts[0]
	K= int(parts[1])
	print 'Case #'+str(i)+': '+solution(S, K)
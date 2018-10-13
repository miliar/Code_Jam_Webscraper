
def solution(N):
	N= list(N)
	i= 1
	while i < len(N):
		if N[i-1] > N[i]:
			N[i-1]= str(int(N[i-1])-1)
			for j in range(i, len(N)):
				N[j]= '9'
			if i > 1:
				i-= 2
		i+= 1
	i= 0
	while i < len(N) and N[i]=='0':
		i+= 1
	return ''.join(N[i:])

file= open( __file__.split('.')[0]+'.in')
lines= file.read().split('\n')
file.close()

T= int(lines[0])
for i in range(1, T+1):
	N= lines[i]
	print 'Case #'+str(i)+': '+solution(N)
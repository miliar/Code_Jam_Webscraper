def solve(C,F,X):
	best=99999
	farms=0
	current=X/2
	while current<=best:
		best=current
		farms+=1
		current=0
		for j in range(farms):
			current+=C/(2+j*F)
		current+=X/(2+(j+1)*F)
	return best

n=input()
for i in range(1,n+1):
	C,F,X=map(float,raw_input().split(' '))
	res=solve(C,F,X)
	print 'Case #%d: %.7f'%(i,res)
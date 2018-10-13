T=int(raw_input())+1


for i in range (1,T):
	inp=raw_input()
	D=float(inp.split(' ')[0])
	N=int(inp.split(' ')[1])+1

	inp=raw_input()
	K=float(inp.split(' ')[0])
	S=float(inp.split(' ')[1])
	time=(D-K)/S
	for j in range (2,N):
		inp=raw_input()
		position=float(inp.split(' ')[0])
		Speed=float(inp.split(' ')[1])
		temp=(D-position)/Speed
		if temp>time:
			time=temp
	print 'Case #%d: %f'%(i,D/time)





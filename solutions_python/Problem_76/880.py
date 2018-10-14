def binary(x):
	y=''
	i=0
	while i<30:	
		y=str(x%2) + y
		x=x/2
		i+=1
	return y

g=raw_input()

for r in range(int(g)):
	n=raw_input()
	t=raw_input().split(' ')
	t_bin=[binary(int(x)) for x in t]



	flag=1
	for i in range(30):
		xor=0
		for k in range(int(n)):
			xor=xor+int(t_bin[k][i])
		if xor%2!=0:
			flag=0
			break
	if flag==0:
		print('Case #' + str(r+1) + ': NO')
	else:
		t_num=[int(x) for x in t]
		sean=sum(t_num)-min(t_num)
		print('Case #' + str(r+1) +': ' +str(sean))
		
	
	

def satisfy(data):
	x=data%10
	data=data/10
	flag=True
	while (data>0):
		if x>=(data%10):
			x=data%10
			data=data/10
			
		else:
			flag=False
			break
	return flag
t=int(raw_input())
for i in range(0,t):
	data=int(raw_input())
	while (data>0):
		if satisfy(data):
			break
		else:
			data-=1
	print "Case #"+str(i+1)+": "+str(data)

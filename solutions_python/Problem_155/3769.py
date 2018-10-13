for i in range(int(input())):
	a=input().split()
	count,j,d,fj=0,0,0,0
	while j < int(a[0]):
		if(int(a[1][j]) != 0):
			d=d+int(a[1][j])
			fj+=1
		else:
			count+=1
			d,fj=0,0
			
		if int(a[1][j+1]) == 0:
			j=j+d-fj+1
		else:
			j+=1
	print("Case #%d: %d" %(i+1, count))
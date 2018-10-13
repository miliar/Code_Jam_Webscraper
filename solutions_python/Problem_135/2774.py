f=open(r'cheb_A_smallinput.in', 'r')
n=f.readline()
n=n.rsplit( )[0]
n=int(n)
# print n
for i in range(1, n+1) :
	ans1=f.readline()
	ans1=ans1.rsplit( )[0]
	ans1=int(ans1)
	mat1 = [[] for j in range(4)]
	line1=f.readline()
	line1=line1.rstrip("\n\r ")	
	line1=line1.split(' ')
	mat1[0] = map(int, line1)
	line2=f.readline()
	line2=line2.rstrip("\n\r ")	
	line2=line2.split(' ')
	mat1[1] = map(int, line2)
	line3=f.readline()
	line3=line3.rstrip("\n\r ")	
	line3=line3.split(' ')
	mat1[2] = map(int, line3)
	line4=f.readline()
	line4=line4.rstrip("\n\r ")	
	line4=line4.split(' ')
	mat1[3] = map(int, line4)
	# print mat1[ans1-1]
	ans2=f.readline()
	ans2=ans2.rsplit( )[0]
	ans2=int(ans2)
	mat2 = [[] for j in range(4)]
	line1=f.readline()
	line1=line1.rstrip("\n\r ")	
	line1=line1.split(' ')
	mat2[0] = map(int, line1)
	line2=f.readline()
	line2=line2.rstrip("\n\r ")	
	line2=line2.split(' ')
	mat2[1] = map(int, line2)
	line3=f.readline()
	line3=line3.rstrip("\n\r ")	
	line3=line3.split(' ')
	mat2[2] = map(int, line3)
	line4=f.readline()
	line4=line4.rstrip("\n\r ")	
	line4=line4.split(' ')
	mat2[3] = map(int, line4)
	# print mat2[ans2-1]
	common = set(mat1[ans1-1]).intersection(mat2[ans2-1])
	commonlist = list(common)
	L = len(commonlist)
	if(L==1) : 
		num = commonlist[0]
		print 'Case #{0}: {1}'.format(i, num)
	elif(L==0) :
		print 'Case #{0}: Volunteer cheated!'.format(i)
	elif(L>1) :
		print 'Case #{0}: Bad magician!'.format(i)
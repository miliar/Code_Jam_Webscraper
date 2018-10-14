lines=[]
file = open('A2.in','r')
allLines = file.readlines()
file.close()
for line in allLines:
	a = line.split()
	lines.append(a)

N=int(lines[0][0])
#print N
count=1
for c in range(1,N+1):
	flag=0
	seq=lines[count]
	count+=1
	n=int(seq[0])
	m=int(seq[1])
	#print n,m
	nums=[]
	for j in range(n):
		candies=lines[count]		#gives all of the integers 
		#print 'candies',candies
		num=[0 for i in range(m)] 
		for i in range(m):
			num[i]=candies[0][i]
			#print 'num,i',num,i
			#print 'num',num
		nums.append(num)
		count+=1
	#print nums
	inp=[[0 for i in range(m)] for i in range(n)]
	#print inp
	for i in range(n):
		for j in range(m):
			if nums[i][j]=='.':
				inp[i][j]=1
			else:
				inp[i][j]=0

	#print inp
	flag=0
	for i in range(n):
		for j in range(m):
			if inp[i][j]==0:
				try:
					if inp[i][j+1]==0 and inp[i][j+1]==0 and inp[i+1][j+1]==0 and inp[i+1][j]==0:	
						inp[i][j]=inp[i+1][j+1]='/';inp[i+1][j]=inp[i][j+1]="\\"
				except IndexError:
					flag=1
	if flag==1:	
		print 'Case #%d:' % (c),'Impossible'
	else:
		print 'Case #%d:' % (c)
		for i in range(n):
			strs=''
			for j in range(m):
				try:	
					strs+=inp[i][j]
				except TypeError:
					strs+='.'
			print strs
'''	mat=[[0 for i in range(6)] for i in range(n)]
	for i in range(n):
		games=0;win=0
		for j in range(n):
			if inp[i][j]==0:
				games+=1
			elif inp[i][j]==1:
				games+=1;win+=1
		#print 'games',games
		if games<>0: mat[i][2]=float(win)/float(games)	
		else:	mat[i][2]=0	
		mat[i][1]=win	
		mat[i][0]=games
	for i in range(n):
		tot=0
		for j in range(n):
			if inp[i][j]<>-1:	
				if inp[i][j]==1:
					a=0
				else:
					a=1
				b=mat[j][0]-1
				#print mat[j][1],a
				if b<>0:
					tot+=float(mat[j][1]-a)/float(b)
				else:
					tot+=0
		avg=float(tot)/float(mat[i][0])
		mat[i][3]=avg
	for i in range(n):
		sums=0
		for j in range(n):
			if inp[i][j]<>-1:	
				sums+=mat[j][3]
		mat[i][4]=float(sums)/float(mat[i][0])
	for i in range(n):
		mat[i][5]=0.25*mat[i][2]+0.50*mat[i][3]+0.25*mat[i][4]
		#print '%.6f' %(mat[i][5])
	
	print 'Case #%d:' % (c)
	for i in range(n):	
		print '%.6f' %(mat[i][5])
	'''

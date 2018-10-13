t=int(input())
for tc in range(t):
	r,c = map(int,input().split())
	row=[None]*26
	for i in range(r):
		row[i] = input()
	uc = [0]*26
	has=[0]*25
	rc=[]
	for  i in range(25):
		rc.append([])
	for i in range(r):
		for j in range(c):
			if row[i][j]!='?':
				# uc[int(row[i][j])-int('A')] = 1
				has[i]=1
				rc[i].append(row[i][j])
	# print(rc)
	# print(has)
	ans=[]
	nhasr = []
	for i in range(r):
		ans.append([None]*c)
	com = [0]*26
	for i in range(r):
		if has[i]==1:
			k=0
			com[i]=1
			for j in range(c):
				if row[i][j]=='?' or row[i][j]==rc[i][k]:
					ans[i][j]=rc[i][k]
				else:
					k+=1
					ans[i][j]=rc[i][k]
		else:
			nhasr.append(i)
	# print(ans)
	# print(nhasr)

	for i in nhasr:
		if i==0:
			for j in range(c):
				ans[i][j]=ans[i+1][j]
				if(has[i+1]==1):
					com[i]=1
		else: 
			for j in range(c):
				ans[i][j]=ans[i-1][j]
				if(has[i-1]==1):
					com[i]=1
	for i in range(len(nhasr)-1,-1,-1):
		if(com[i]==0):
			for j in range(c):
				if i!=r-1:
					ans[i][j] =  ans[i+1][j]

	print("Case #"+ str(tc+1)+":")
	for i in range(r):
		for j in range(c):
			print(ans[i][j],end='')
		print()


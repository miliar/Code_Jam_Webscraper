import sys
t=int(raw_input())
for nn in range(t):
	r,c=map(int,raw_input().split())
	data=[]
	for i in range(r):
		data.append(raw_input())
	ok = True
	for i in range(r):
		st=False
		cnt=0
		for j in range(c):
			if data[i][j]=='#':
				if st==False:
					st=True
					cnt+=1
				else:
					cnt+=1
			else:
				if st==True:
					if cnt%2!=0:
						ok=False
				cnt=0
				st=False

		if cnt%2!=0:
			ok=False

	for i in range(c):
		st=False
		cnt=0
		for j in range(r):
			if data[j][i]=='#':
				if st==False:
					st=True
					cnt+=1
				else:
					cnt+=1
			else:
				if st==True:
					if cnt%2!=0:
						ok=False
				cnt=0
				st=False
		if cnt%2!=0:
			ok=False
	
	sys.stdout.write("Case #%d:\n"%(nn+1))
	if not ok:
		print "Impossible"
	else:
		store=[]
		for i in range(r):
			res=''
			st=False
			for j in range(c):
				if data[i][j]=='.':
					res=res+'.'
					st=False
				else:
					if not st:
						if i>0 and j<c and  store[i-1][j]=='/' and store[i-1][j+1]=='\\':
							res=res+'\\'
							st=True
						else:
							res=res+'/'
							st=True
					else:
						if i>0  and j>=0 and store[i-1][j]=='\\' and store[i-1][j-1]=='/':
							res=res+'/'
							st=False
						else:
							res=res+'\\'
							st=False
			print res
			store.append(res)




	



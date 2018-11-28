def readinput():
	global t
	global inp
	global n,k
	i=0
	for line in open('input.txt'):
		if i==0:
			t=int(line)
			i=1
		elif i==1:
			n,k=line.split()
			n,k=int(n),int(k)
			i=2
		else:
			line=line.replace('\n','')
			inp.append(list(line))

def writetofile(res):
	with open('output.txt','a') as myfile:
		for item in res:
			myfile.write("Case #"+str(i)+": "+str(item[0])+" "+str(item[1])+"\n")
			i+=1

def do(inp,r,c):
	for i in range(r):
			check=0
			if i<r-1:
				for item in inp[i+1]:
					if item != '?':
						check=1
						break
			for j in range (c):
				
				if inp[i][j] ==' ?':continue
				
				tempi=i-1
				tempj=j
				#top
				while tempi >= 0 and inp[tempi][tempj] == '?':
					inp[tempi][tempj]=inp[i][j]
					tempi-=1
				#left
				tempi=i
				tempj=j-1
				while tempj>= 0 and inp[tempi][tempj] == '?':
					inp[tempi][tempj]=inp[i][j]
					tempj-=1
				#right
				if  j+1< c and inp[i][j+1] == '?':
					inp[i][j+1]=inp[i][j]	
				
				# bottom
				if i+1<r and check==0 :
					inp[i+1][j]=inp[i][j]

				
	return inp

if __name__=='__main__':
	global t
	global inp
	global r,c
	inp=[]
	# readinput()
	t=int(raw_input())
	for _ in range(t):
		inp=[]
		r,c=raw_input().split()
		r,c=int(r),int(c)
		for k in range(r):
			s=list(raw_input())
			inp.append(s)

		inp = do(inp,r,c)
		inp=do(inp,r,c)
		print "Case #"+str(_+1)+":"
		for i in range(r):
			print "".join(inp[i])


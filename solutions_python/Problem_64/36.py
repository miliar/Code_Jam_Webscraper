def isok(col,c,board,i,j):
	v=map(int,[board[ii][j+c-1] for ii in range(i,i+c)])
	h=map(int,[board[i+c-1][jj] for jj in range(j,j+c)])
	#print v,h
	if (c-int(col))%2==1:
		return all([cc<2 for cc in (v+h)]) and not any(v[::2]) and not any(h[::2]) and all(v[1::2]) and all(h[1::2])
	else:
		return all([cc<2 for cc in (v+h)]) and all(v[::2]) and all(h[::2]) and not any(v[1::2]) and not any(h[1::2])

#print isok('0',3,["0101","1010","0101","1010"],0,0)

def invalida(board,i,j,c):
	c+=1
	for ii in range(i,i+c):
		board[ii]=board[ii][:j]+"2"*c+board[ii][j+c:]

def uniq(seq):  
    # order preserving 
    checked = [] 
    for e in seq: 
        if e not in checked: 
            checked.append(e) 
    return checked

f="C-small-attempt0"
fin=open(f+".in")
fout=open(f+".out",'w')
for case in range(1,int(fin.readline())+1):
	m,n=map(int,fin.readline().strip().split())
	board=[]
	for _ in range(m):
		num=int(fin.readline().strip(),16)
		board.append(''.join(str((num>>i)&1) for i in xrange(n-1,-1,-1)))
	#invalida(board,1,1,1)
	#print board
	maxc=2
	szes=[]
	while maxc>0:
		maxc=0
		for i in range(m):
			for j in range(n):
				col=board[i][j]
				if col!='2':
					c=1
					while i+c<=m and j+c<=n and isok(col,c,board,i,j): c+=1
					c-=1
					if c>maxc:
						maxc=c
						maxij=(i,j)
		#print maxij,maxc
		invalida(board,maxij[0],maxij[1],maxc-1)
		#for l in board: print l
		#print
		if maxc: szes.append(maxc)
	res=len(set(szes))
	#print szes
	#print "Case #%d: %d"%(case,res)
	fout.write("Case #%d: %d\n"%(case,res))
	for s in uniq(szes): fout.write("%d %d\n"%(s,len(filter(lambda x:x==s,szes))))



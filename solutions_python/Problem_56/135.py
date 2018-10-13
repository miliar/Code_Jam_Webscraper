from string import translate
f="A-large"
fin=open(f+".in")
fout=open(f+".out",'w')

def alignright(l):
	return 

for case in range(1,int(fin.readline())+1):
	n,k=map(int,fin.readline().strip().split())
	board=[fin.readline().strip() for _ in range(n)]
	board=map(lambda l:translate(l,None,'.').rjust(n,'.'), board)
	#for l in board: print l
	#print
	res={'R':False,'B':False}
	for char in ('R','B'):
		for i in range(n):
			for j in range(n):
				if board[i][j]==char:
					ii,jj,count=i,j,0
					while ii<n and board[ii][jj]==char: count+=1; ii+=1
					if count>=k: res[char]=True
					ii,jj,count=i,j,0
					while jj<n and board[ii][jj]==char: count+=1; jj+=1
					if count>=k: res[char]=True
					ii,jj,count=i,j,0
					while ii<n and jj<n and board[ii][jj]==char: count+=1; ii+=1; jj+=1
					if count>=k: res[char]=True
					ii,jj,count=i,j,0
					while ii<n and jj>=0 and board[ii][jj]==char: count+=1; ii+=1; jj-=1;
					if count>=k: res[char]=True
		"""matrix=[[(0,0,0,0)]*n for _ in range(n)]
		for i in range(n):
			for j in range(n):
				if board[i][j]==char:
					if i==0 and j==0: matrix[0][0]=(1,1,1,1)
					elif i==0: matrix[0][j]=(1,matrix[0][j-1][1]+1,1,1)
					elif j==0: matrix[i][0]=(matrix[i-1][0][0]+1,1,1,matrix[i-1][1][3]+1)
					else:
						if j<n-1: matrix[i][j]=(matrix[i][j-1][0]+1,matrix[i-1][j][1]+1,matrix[i-1][j-1][2]+1, matrix[i-1][j+1][3]+1)
						else: matrix[i][j]=(matrix[i][j-1][0]+1,matrix[i-1][j][1]+1,matrix[i-1][j-1][2]+1,1)
					if matrix[i][j][0]>=k or matrix[i][j][1]>=k or matrix[i][j][2]>=k or matrix[i][j][3]>=k: res+=char
		#for l in matrix: print l
		#print"""
	if res['R'] and res['B']: prin='Both'
	elif res['R']: prin='Red'
	elif res['B']: prin='Blue'
	else: prin='Neither'
	print "Case #%d: %s"%(case,prin)
	fout.write("Case #%d: %s\n"%(case,prin))

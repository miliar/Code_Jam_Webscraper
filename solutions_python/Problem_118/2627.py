def CheckSym(M,Sym):
	#Check for rows
	for i in range(0,4):
		rowflag=0
		for j in range(0,4):
			if((M[i][j]!=Sym) and (M[i][j]!='T')):
				rowflag=1				
				break;
		if(rowflag==0):
			return True;
	
	for i in range(0,4):
		colflag=0
		for j in range(0,4):
			if((M[j][i]!=Sym) and (M[j][i]!='T')):
				colflag=1				
				break;
		if(colflag==0):
			return True;

	d1flag=0
	for i in range(0,4):
		if((M[i][i]!=Sym) and (M[i][i]!='T')):
			d1flag=1				
			break;
	if(d1flag==0):
		return True;

	d2flag=0
	for i in range(0,4):
		if((M[i][3-i]!=Sym) and (M[i][3-i]!='T')):
			d2flag=1				
			break;
	if(d2flag==0):
		return True;
	return False

def CheckDraw(M):
	for i in range(0,4):
		for j in range(0,4):
			if(M[i][j]=='.'):
				return False;
	return True;



f=open('input','r')
n=int(f.readline())
#print n

L=0
while L<n:
	M=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(0,4):
		S=f.readline().rstrip()
		j=0		
		for c in S:
			M[i][j]=c
			j=j+1

	#for i in range(0,4):
	#	l=""
	#	for j in range(0,4):
	#		l=l+M[i][j]
	#	print l
	f.readline()
	if(CheckSym(M,'X')==True):
		print "Case #"+str(L+1)+": X won"
	elif(CheckSym(M,'O')==True):
		print "Case #"+str(L+1)+": O won"
	elif(CheckDraw(M)==True):
		print "Case #"+str(L+1)+": Draw"
	else:
		print "Case #"+str(L+1)+": Game has not completed"			
	L=L+1

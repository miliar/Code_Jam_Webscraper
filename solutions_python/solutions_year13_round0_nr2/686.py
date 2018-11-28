test=input()
matrix =[]
row=[]
column=[]
flag=0
def max(a,b):
	if a>b:
		return a
	else :
		return b
for i in range (0,101):
	row.append(0)
	column.append(0)
	matrix.append([])
	for j in range(0,101):
		matrix[i].append(0)
for i in range(1,test+1):
	flag=1
	strings=raw_input();
	string=strings.split(" ")
	N=int(string[0])
	M=int(string[1])
	for j in range(0,N):
		strings=raw_input();
	        string=strings.split(" ")
		for k in range(0,M):
			matrix[j][k]=int(string[k])
	for j in range(0,N):
		row[j]=matrix[j][0]
		for k in range(0,M):
			row[j]=max(row[j],matrix[j][k])
	for j in range(0,M):
		column[j]=matrix[0][j]
		for k in range(0,N):
			column[j]=max(column[j],matrix[k][j])
	for j in range(0,N):
		for k in range(0,M):
			if(matrix[j][k]!=row[j]	and matrix[j][k]!=column[k]):
				flag=0
	if(flag==1):
		print "Case #"+str(i)+": YES"
	else:
		print "Case #"+str(i)+": NO"			

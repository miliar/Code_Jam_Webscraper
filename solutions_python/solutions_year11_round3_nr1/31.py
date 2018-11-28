import random

d=0

p=list()

f=open('tile.in','r')
cases= f.readline()


def inrange(i,j,r,c):
	if i+1>=r or j+1>=c:
		return False
	return True
	
def ingrid(i,j,matrix):
	if matrix[i][j]=='#' and matrix[i+1][j]=='#' and matrix[i][j+1]=='#' and matrix[i+1][j+1]=='#':
		return True
	return False

for i in range(1,int(cases)+1):
	print "Case #"+str(i)+":\n",
	array = f.readline().strip()
	arr = array.split(" ")
	rcarray = [int(x) for x in arr]
	r=rcarray[0]
	c=rcarray[1]

	matrix=list()

	for i in range(0,r):
		row = f.readline().strip()
		matrix.append(row)

	flag=0

	for i in range(0,r):
		s=list(matrix[i])
		matrix[i]=s


	for i in range(0,r):
		#print matrix[i]
		for j in range(0,c):
			if( matrix[i][j] == '#' ):
				if inrange(i,j,r,c)==False:
					flag=1
				elif ingrid(i,j,matrix)==False:
					flag=1
				else:
	                                matrix[i][j]='/'
	                                matrix[i][j+1]='\\'
	                                matrix[i+1][j]='\\'
	                                matrix[i+1][j+1]='/'
					
						
	if flag:
		print "Impossible"
	else:
		for i in range(0,r):
			print "".join(matrix[i])
				
		
	
	



		

	


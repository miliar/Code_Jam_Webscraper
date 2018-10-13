def solve(matrix):
	for i in range(R):
		for j in range(C):
			if matrix[i][j]=="#":
				if i==R-1 or j==C-1 or matrix[i][j+1]!="#" or matrix[i+1][j]!="#" or matrix[i+1][j+1]!="#":
					#print "NO AT ",i,j,matrix
					return "no"
				else:
					#print i,j,matrix[i][j]
					matrix[i][j]="/"
					matrix[i][j+1]="\\"
					matrix[i+1][j]="\\"
					matrix[i+1][j+1]="/"
	#print "matrix",matrix
	return matrix

f=open("in.txt")
f_out=open("out.txt",'w')

Tests=int(f.readline().strip())
for case in range(1,Tests+1):
	R,C=map(int,f.readline().strip().split())
	#print R,C
	
	matrix=[]
	for i in range(R):
		matrix.append(list(f.readline().strip()))
	
	#print matrix
	ans=solve(matrix)
	
	f_out.write("Case #%d:\n" %(case))
	if ans=="no":
		f_out.write("Impossible\n")
	else:
		f_out.write("\n".join(["".join(i) for i in ans])+"\n")
	
	#f_out.write("Case #%d:\n%s\n" %(case,str("\n".join([str(i) for i in RPI]))))

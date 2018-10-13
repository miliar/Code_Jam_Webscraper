import copy
inf=open('D-small-attempt0.in','r')
outf=open('small3.out','w')
opt=[[[False for col in range(4)] for row in range(4)] for depth in range(4)]
for i in range(4):
	for j in range(4):
		opt[0][i][j]=True
for i in range(1,4):
	for j in range(4):
		for k in range(4):
			if i+1 > (j+1)*(k+1) or (j+1)*(k+1)%(i+1)!=0 or i>min((j+1),(k+1)):
				opt[i][j][k]=False
			else:
				opt[i][j][k]=True
# for i in range(4):
# 	print(opt[i])

count_case=int(inf.readline())
for i in range(count_case):
	num_o=inf.readline().split()
	num_l=[]
	for o in num_o:
		num_l.append(int(o))
	result="GABRIEL" if opt[num_l[0]-1][num_l[1]-1][num_l[2]-1] else "RICHARD"
	outf.write("Case #"+str(i+1)+": "+str(result)+'\n')
inf.close()
outf.close()



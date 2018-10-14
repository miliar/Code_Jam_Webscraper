#sleep=[False,False,False,False,False,False,False,False,False,False]
o_file=open("C-small-1-attempt0.out","a")
x=0
y=0
with open("C-small-1-attempt0.in","r") as i_file:
	T=int(i_file.readline())
	for line in i_file:
		x +=1;
		NList=[int(j) for j in line.split()]
		N=NList[0]
		K=NList[1]
		A=[]
		A.insert(0,N)
#		print(NList)
#		print(N)
#		print(K)
		while(K!=0):
			ind=A.index(max(A))
			y=max(A)
			if(y%2==0):
				A[ind]=y//2-1
				A.insert(ind+1,y//2)
			else:
				A[ind]=y//2
				A.insert(ind+1,y//2)
			K-=1
		ma=max([A[ind],A[ind+1]])
		mi=min([A[ind],A[ind+1]])
		#print(ma,mi)
		o_file.write("Case #"+str(x)+": "+str(ma)+" "+str(mi)+"\n")
o_file.close()
#sleep=[False,False,False,False,False,False,False,False,False,False]
o_file=open("B-large.out","a")
x=0
y=0
with open("B-large.in","r") as i_file:
	T=int(i_file.readline())
	for line in i_file:
		x +=1;
		NList=[int(j) for j in line.split()]
		f=NList[0]
		NList=[int(d) for d in str(f)]
		f=NList[0]
		k=0
#		print(f)
#		print(NList[k])
		while(sorted(NList)!=NList):
			while f<=NList[k]:
				f=NList[k]
				k=k+1
				if(k==len(NList)):
					break
			while NList[k-1]==f:
				k=k-1
				if(k==0):
					break
			if(k==0):
				if(NList[0]==1):
					k=-1
					del NList[0]
				else:
					NList[k]-=1
			else:
				NList[k]-=1
			for j in range(k+1,len(NList)):
				NList[j]=9
		y=int(''.join(map(str,NList)))
		o_file.write("Case #"+str(x)+": "+str(y)+"\n")
o_file.close()
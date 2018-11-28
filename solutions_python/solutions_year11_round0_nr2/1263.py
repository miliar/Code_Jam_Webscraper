#lets code...
fob=open('d:/magica.in','r')
out=open('d:/magica.txt','w')
cases=fob.readline()#get num of cases
cases=int(cases)
#loop through the cases
for h in range(cases):
	 line=fob.readline()
	 line=line.split()
	 C=int(line[0])
	 D=int(line[C+1])
	 N=int(line[C+D+2])
	 
	 #extract combining elements
	 cList=[]
	 for x in range(C):
		 cList.append(line[x+1])
	 #extract opposing elements
	 oList=[]
	 for y in range(D):
		 oList.append(line[C+y+2])
	 #extract invocation sequence
	 seq=line[C+D+3]
	 
	 final=[]
	 for i in range(len(seq)):
		 Base=seq[i]
		 if len(final)==0:
			 final.append(Base)
		 else:
			 prev=final[len(final)-1]
			 #test for combination
			 cFlag=False
			 for x in range(len(cList)):
				 if (prev in cList[x][0] or prev in cList[x][1] ) and (Base in cList[x][0] or Base in cList[x][1]) and (Base!=prev):
					 final[len(final)-1]=cList[x][len(cList[x])-1]
					 cFlag=True
				 elif (prev in cList[x]) and (Base in cList[x]) and (Base==prev):
					 newBase=Base+Base
					 if newBase in (cList[x][0]+cList[x][1]):
						 final[len(final)-1]=cList[x][len(cList[x])-1]
						 Base=cList[x][len(cList[x])-1]
						 cFlag=True
			 #test for opposition
			 flag=False
			 if cFlag!=True:
				 for x in range(len(oList)):
					 if Base in oList[x]:
						 flag=True
						 opposite=oList[x].replace(Base,'')
						 for j in final[::-1]:
							 if opposite in j:
								 final=[]	 
						 if len(final)!=0:
							 final.append(Base)
				 if flag!=True:
					 final.append(Base)
	 output='['+', '.join(final)+']'
	 output="Case #"+str(h+1)+": "+output+"\n"
	 out.write(output)
out.close()
fob.close()

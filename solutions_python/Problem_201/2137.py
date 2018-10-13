from collections import Counter
output=list()
def Problem3():
	f=open('small_input3.txt');
	n=f.readline()
	#print(n)
	for i in range(int(n)):
		inp=list(map(int,f.readline().split()))
		calc(inp[0],inp[1])
	f.close()
	writeOutput()

def calc(N,K):
	l=[1]
	l.extend([0]*N)
	l.append(1)
	mini_tuple=list()
	maxi_tuple=list()
	tmp1=0
	tmp2=0
	for i in range(K):
		mini_tuple=list()
		maxi_tuple=list()
		ind=0
		for j in range(1,len(l)-1):
			if l[j]==0:
				for k in range(j-1,-1,-1):
					if l[k]==1:
						Ls=j-k-1
						break
				for k in range(j+1,len(l)):
					if l[k]==1:
						Rs=k-j-1
						break
				mini_tuple.append([min(Ls,Rs),j])
				maxi_tuple.append([max(Ls,Rs),j])
		mini_tuple_sorted=sorted(mini_tuple,key=lambda x:x[0])
		max_mini_tuple=mini_tuple_sorted[-1][0]

		dct=dict(Counter([x[0] for x in mini_tuple]))
		#print(dct)
		if dct[max_mini_tuple]>1:
			local_list=list()
			for x in mini_tuple:
				if x[0]==max_mini_tuple:
					local_list.append(x[1])
			maxi_tuple_sorted=sorted(maxi_tuple,key=lambda x:x[0])
			max_val=-1
			max_ind=-1
			for x in maxi_tuple_sorted:				
				if x[1] in local_list and x[0]>max_val:
					max_val=x[0]
					max_ind=x[1]
			ind=max_ind

		else:
			for x in mini_tuple:
				if x[0]==max_mini_tuple:
					ind=x[1]
					break

		tmp1=[x[0] for x in mini_tuple if x[1]==ind][0]
		tmp2=[x[0] for x in maxi_tuple if x[1]==ind][0]
		l[ind]=1
		#print(l)
		#input()
		#print(mini_tuple,maxi_tuple,max_mini_tuple)
		#input()
	output.append([tmp2,tmp1])

def writeOutput():
	f=open('small_output3.txt','w')
	for i in range(len(output)):
		f.write("Case #"+str(i+1)+": "+str(output[i][0])+' '+str(output[i][1])+'\n')
	f.close()

Problem3()
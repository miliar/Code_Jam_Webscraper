from math import floor, log
def stalls(A,k):
	for n in range(k):
		b=max(A.keys())
		if b%2==0:
			L=int(b/2-1)
			R=int(b/2)
		else:
			L=max(int(floor(b/2)),0)
			R=L
		A[b]-=1
		if L not in A.keys():
			A[L]=1
		else:
			A[L]+=1
		if R not in A.keys():
			A[R]=1
		else:
			A[R]+=1
		if A[b]==0:
			del(A[b])
		#print(A)
	return(max(L,R),min(L,R))
f=open(r'C:\Users\PRANAV CHAKRA VARTHY\Desktop\C-small-2-attempt2.in') # opens in read mode C-small-1-attempt1.in
g=open(r'C:\Users\PRANAV CHAKRA VARTHY\Desktop\cj3small.out','w') # opens in write mode
f.readline()
count=1
for i in f: #reads every line
	k=i.strip('\n') #inputs every line by stripping '\n'
	strn=k.split()
	A={int(strn[0]):1}
	# for j in range(int(strn[0]))
		# A.append(0)
	ans=stalls(A,int(strn[1])) # computes the function
	g.write('Case #'+str(count)+': '+str(ans[0])+' '+str(ans[1]))#writes in file
	g.write('\n') # goes to new line
	count+=1

f.close()	
g.close()